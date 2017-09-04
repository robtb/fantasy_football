from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID={}, remember_me={}'.format(form.openid.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
