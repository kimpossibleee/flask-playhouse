from flask import render_template, flash, redirect, url_for
from app.models import User
from app import db
from . import bp as app
from app.forms import RegisterForm, LoginForm

@app.route('/signin')
def signin():
    form = LoginForm()
    return render_template('signin.jinja', form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        email = User.query.filter_by(email=email)
        if not email and not user:
            u = User(username=username, email=email, password=form.password.data)
            u.commit()
            flash(f'{username} registered')
            return redirect(url_for('main.home'))
        if user:
            flash(f'{username} already take, please try again')
        elif email:
            flash(f'{email} already take, please try again')
    return render_template('register.jinja', form = form)
