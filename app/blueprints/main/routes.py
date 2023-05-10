from . import bp as app
from flask import render_template
from app.resources.countries import Country
import random

@app.route('/')
def home():
    return render_template('index.jinja')

@app.route('/about')
def about():
    return render_template('about.jinja', title='About')

@app.route('/buzz')
def buzz():
    def random_ten_countries():
        random.shuffle(Country)
        country_list = Country[:10]
        return country_list
    return render_template('buzz.jinja', title='Trending', countries=random_ten_countries())
