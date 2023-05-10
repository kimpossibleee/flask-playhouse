from flask import render_template
from . import bp as app

@app.route('/signin')
def signin():
    return render_template(signin.jinja)
