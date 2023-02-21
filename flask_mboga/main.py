from flask import Flask, render_template, url_for, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = '611e204927d4e611f723b1935726c350a1c05ade'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/recipe")
def recipe():
    return render_template('recipe.html')

@app.route("/nutritional_value")
def nutritional_valuesource():
    return render_template('nutrtional_value.html')

@app.route("/register")
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route("/login")
def login():
        form = LoginForm()
        return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
