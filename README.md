# Activigraph

Use your exported Strava data to create custom charts of your activities.


### 📖 Installation
```
git clone https://github.com/ecumike/activigraph.git
cd activigraph
```


### Bulk export from Strava
The process for downloading data is described on the Strava website here: [https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export#Bulk], but in essence, do the following:

1. Log in to [Strava](https://www.strava.com/)
2. Select "[Settings](https://www.strava.com/settings/profile)" from the main drop-down menu at top right of the screen
3. Select "[My Account](https://www.strava.com/account)" from the navigation menu to the left of the screen.
4. Under the "[Download or Delete Your Account](https://www.strava.com/athlete/delete_your_account)" heading, click the "Get Started" button.
5. Under the "Download Request", heading, click the "Request Your Archive" button. 
6. Wait for an email to be sent with the download link.
7. Click the link in email to download zip file of your data.
8. Unzip files


### Data setup 
1. Move the unzipped Strava files and directories into the repo `strava_data` directory.


### Env setup
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running in debug mode (auto-reload)
```flask --debug run```

## Load the site at http://127.0.0.1:5000
```

### ⭐️ Support
Give a ⭐️  if this project helped you!

### License
[Apache 2 license - Free to use and modify](LICENSE)

