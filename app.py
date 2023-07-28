from flask import Flask, render_template   
from waitress import serve


app = Flask(__name__)

from src.graphs import getActivityData

@app.route("/")
def home():
	return render_template("home.html", data=getActivityData())

if __name__ == '__main__':
	#app.run()
	serve(app, host='0.0.0.0', port=80)