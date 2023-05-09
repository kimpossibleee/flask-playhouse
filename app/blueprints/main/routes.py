from . import bp as app
from flask import render_template
from app.resources.countries import Country

@app.route('/')
def home():
    return render_template('index.jinja')

@app.route('/about')
def about():
    return render_template('about.jinja', title='About')

@app.route('/buzz')
def buzz():
    def get_ten_countries():
        country_list = (Country)[:10]
        return country_list
    return render_template('buzz.jinja', title='Trending', countries=get_ten_countries())
