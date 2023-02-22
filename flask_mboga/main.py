from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '611e204927d4e611f723b1935726c350a1c05ade'


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
