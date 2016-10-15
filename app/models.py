from app import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), primary_key=True)
    price = db.Column(db.Integer)
    info = db.Column(db.String(200))
    quantity = db.Column(db.Integer)
