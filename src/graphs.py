import pandas as pd
from datetime import datetime, timezone


def strToLocalDateTime(s):
	try:
		dateObj = datetime.strptime(s, '%b %d, %Y, %I:%M:%S %p')
		return dateObj.replace(tzinfo=timezone.utc).astimezone(tz=None)
	except:
		return 0


def kmToMiles(km):
	try:
		return round(km * .62137, 2)
	except:
		return 0
		
			
def getActivityData():
	"""
	Parse activities CSV, only for bike rides.
	"""
	df = pd.read_csv('./strava_data/activities.csv')
	dates = ['x']
	heartRates = ['Avg heart rate']
	distances = ['Distance']
	durations = ['Duration']
	sinceIncludingYear = datetime.now().year-3
	
	for i, row in df.iterrows():
		try:
			date = strToLocalDateTime(row['Activity Date'])
			if date.year > sinceIncludingYear and row['Activity Type'] == 'Ride' and row['Average Heart Rate'] > 0:
				dates.append(date.strftime('%Y-%m-%d'))
				distances.append(kmToMiles(row['Distance']))
				heartRates.append(int(row['Average Heart Rate']))
				durations.append(int(row['Elapsed Time']/60))
		except Exception as ex:
			print(f'Problem processing CSV row # {i}: {ex}, data: {row}')
	
	regions = []
	for y in range(sinceIncludingYear, datetime.now().year+1): 
		if y % 2 == 0:
			klass = 'alt1'
		else:
			klass = 'alt2'
		
		regions.append({
			'start': f'{y}-01-01',
			'end': f'{y}-12-31',
			'class':klass
		})
	
	return {
		'dates': dates,
		'heartRates': heartRates,
		'distances': distances,
		'durations': durations,
		'regions': regions,
	}