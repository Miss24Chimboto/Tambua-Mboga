from flask import render_template, url_for, flash, redirect
from flask_mboga import app
from flask_mboga.forms import RegistrationForm, LoginForm
from flask_mboga.models import User, Vegetable, Recipe, NutritionalValue


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/recipe")
def recipe():
    return render_template('recipe.html', title='Recipe')

@app.route("/nutritional_value")
def nutritional_valuesource():
    return render_template('nutritional_value.html', title='Nutritional Value')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Register')

@app.route("/login", methods=['GET', 'POST'])
def login():
        form = LoginForm()
        if form.validate_on_submit():
            if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                flash('You have been logged in!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        return render_template('login.html', form=form, title='Login')

@app.route("/search")
def search():
    #query = request.GET.get('search')
    #req_search = Storage.query.filter_by(req_no=query)
    return render_template('home.html')
"""
@app.route("/recipe")
def recipe():
    return render_template('recipe.html')

@app.route("/results")
def results():
    return render_template('results.html', title='Search results')

@app.route("/nutritional_value")
def nutrtion():
    return render_template('nutritional_value.html')
    """
