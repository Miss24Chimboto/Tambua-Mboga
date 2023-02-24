from datetime import datetime
from flask_mboga import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Vegetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    recipe = db.relationship('Recipe', backref='recipes')
    nutrion = db.relationship('NutritionalValue', backref='nutrients')

    def __repr__(self):
        return f"Vegetable('{self.name}')"


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ingredients = db.Column(db.Text, nullable=False)
    method = db.Column(db.Text, nullable=False)
    vegetable_id = db.Column(db.Integer, db.ForeignKey('vegetable.id'), nullable=False)

    def __repr__(self):
        return f"Recipe('{self.title}', '{self.date_posted}')"


class NutritionalValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    nutritional_score = db.Column(db.Integer, nullable=False)
    nutrients = db.Column(db.Text, nullable=False)
    vegetable_id = db.Column(db.Integer, db.ForeignKey('vegetable.id'), nullable=False)

    def __repr__(self):
        return f"NutritionalValue('{self.title}', '{self.date_posted}')"
