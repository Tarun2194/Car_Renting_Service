import json
import os.path
from werkzeug.utils import secure_filename

from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify

from form import SignUpForm, LoginForm

app = Flask(__name__)
app.secret_key = "kjjjgjgkjlhuaiy7u"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('sign_up.html', form=form)

@app.route('/signup1', methods=['GET', 'POST'])
def signup1():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('sign_up1.html', form=form)

@app.route('/signup2', methods=['GET', 'POST'])
def signup2():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('sign_up2.html', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template("success.html")

@app.route('/cars')
def cars():
    return render_template("cars.html")

if __name__ == '__main__':
    app.run(debug=True)
