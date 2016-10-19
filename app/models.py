from app import db

# join table for ingredients and products
iptable = db.Table('iptable',
        db.Column('ing_id', db.Integer, db.ForeignKey('ingredient.id')),
        db.Column('pro_id', db.Integer, db.ForeignKey('product.id')))

# join table for ingredients and recipes
irtable = db.Table('irtable',
        db.Column('ing_id', db.Integer, db.ForeignKey('ingredient.id')),
        db.Column('rec_id', db.Integer, db.ForeignKey('recipe.id')))

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    season = db.Column(db.String(80))
    products = db.relationship('Product', secondary=iptable, backref='ingredients', lazy='dynamic')
    recipes = db.relationship('Recipe', secondary=irtable, backref='ingredients', lazy='dynamic')
    nutrition = db.relationship('Nutrition', backref='ingredient', lazy='dynamic', uselist=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    origin = db.Column(db.String(100))
    cooktime = db.Column(db.Integer)
    nutrition = db.relationship('Nutrition', backref='recipe', lazy='dynamic', uselist=False)
    lifestyle = db.relationship('Lifestyle', backref='recipe', lazy='dynamic', uselist=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    description = db.Column(db.String(200))
    similarproducts = db.relationship('Product', lazy='dynamic')
    nutrition = db.relationship('Nutrition', backref='product', lazy='dynamic', uselist=False)
    lifestyle = db.relationship('Lifestyle', backref='product', lazy='dynamic', uselist=False)

class LifeStyle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight_management = db.Column(db.Boolean)
    dietary_restricion = db.Column(db.String(80))
    gluten_free = db.Column(db.Boolean)
    carb_free = db.Column(db.Boolean)
    vegetarian = db.Column(db.Boolean)
    vegan = db.Column(db.Boolean)

class Nutrition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serving_size = db.Column(db.String(80))
    calories = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    carbs = db.Column(db.Integer)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    products = db.relationship('Product', backref='category', lazy='dynamic')
    recipes = db.relationship('Recipe', backref='category', lazy='dynamic')

