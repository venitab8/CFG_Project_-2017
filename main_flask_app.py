from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main_equipment_page.html')

@app.route('/search/<condition>')
def enter_values(condition=None):
    return "search page"


@app.route('/results/<condition>')
def results(condition=None):
	return "result page"
