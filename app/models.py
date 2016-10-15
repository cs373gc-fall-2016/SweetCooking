from app import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), primary_key=True)
    price = db.Column(db.Integer)
    info = db.Column(db.String(200))
    quantity = db.Column(db.Integer)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), primary_key=True)
    price = db.Column(db.Integer)
    info = db.Column(db.String(200))
    origin = db.Column(db.String(100))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), primary_key=True)
    price = db.Column(db.Integer)
    data = db.Column(db.String(200))
    description = db.Column(db.String(200))

class LifeStyle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight_management = db.Column(db.String(80), primary_key=True)
    price = db.Column(db.Integer)
    info = db.Column(db.String(200))
    quantity = db.Column(db.Integer)
