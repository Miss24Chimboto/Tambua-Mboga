from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
