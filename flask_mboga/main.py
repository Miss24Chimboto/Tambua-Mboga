from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


@app.route("/Recipe")
def recipe():
    return "<h1>Recipe</h1>"

@app.route("/Nutritional Value")
def nutritional_valuesource():
    return "<h1>Nutritional Value</h1>"

if __name__ == '__main__':
    app.run(debug=True)
