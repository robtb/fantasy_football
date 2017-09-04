from flask import render_template
from app import app
from database import DatabaseInterface


@app.route('/')
@app.route('/index')
def index():
    dbi = DatabaseInterface('c:/sqlite/chinook/sample.db')
    players = dbi.get_lastyear_stats('WR')
    return render_template('base.html', title='Home', players=players)
