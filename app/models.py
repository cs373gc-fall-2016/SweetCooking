"""models file"""
from app import db

#pylint: disable=E1101
#pylint: disable=R0903
#pylint: disable=R0913
#pylint: disable=C0103
# join table for ingredients and products
IPTABLE = db.Table('IPTABLE',
                   db.Column('ing_id', db.Integer,
                             db.ForeignKey('ingredient.id')),
                   db.Column('pro_id', db.Integer, db.ForeignKey('product.id')))

# join table for ingredients and recipes
IRTABLE = db.Table('IRTABLE',
                   db.Column('ing_id', db.Integer,
                             db.ForeignKey('ingredient.id')),
                   db.Column('rec_id', db.Integer, db.ForeignKey('recipe.id')))

class Ingredient(db.Model):
    """ Ingredient table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    season = db.Column(db.String(80))
    products = db.relationship(
        'Product', secondary=IPTABLE, backref='ingredients', lazy='dynamic')
    recipes = db.relationship(
        'Recipe', secondary=IRTABLE, backref='ingredients', lazy='dynamic')
    nutrition = db.relationship(
        'Nutrition', backref='ingredient', lazy='dynamic')

    def __init__(self, name, price=0, season='none'):
        self.name = name
        self.price = price
        self.season = season

    def __repr__(self):
        return 'Ingredient: {}'.format(self.name)


class Recipe(db.Model):
    """ Recipe table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    origin = db.Column(db.String(100))
    cooktime = db.Column(db.Integer)
    nutrition = db.relationship('Nutrition', backref='recipe', lazy='dynamic')
    lifestyle = db.relationship('Lifestyle', backref='recipe', lazy='dynamic')
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, name, price=0, origin='unknown', cooktime=0):
        self.name = name
        self.price = price
        self.origin = origin
        self.cooktime = cooktime

    def __repr__(self):
        return 'Recipe: {}'.format(self.name)


class Product(db.Model):
    """ Product table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    description = db.Column(db.String(200))
    similarproducts = db.relationship('Product', lazy='dynamic')
    nutrition = db.relationship('Nutrition', backref='product', lazy='dynamic')
    lifestyle = db.relationship('Lifestyle', backref='product', lazy='dynamic')
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, name, price=0, description='unknown'):
        self.name = name
        self.price = price
        self.description = description

    def __repr__(self):
        return 'Product: {}'.format(self.name)


class Lifestyle(db.Model):
    """ Lifestyle table"""
    id = db.Column(db.Integer, primary_key=True)
    weight_management = db.Column(db.Boolean)
    dietary_restriction = db.Column(db.String(80))
    gluten_free = db.Column(db.Boolean)
    carb_free = db.Column(db.Boolean)
    vegetarian = db.Column(db.Boolean)
    vegan = db.Column(db.Boolean)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, weight_management=False, dietary_restriction='none', gluten_free=False,
                 carb_free=False, vegetarian=False, vegan=False):
        self.weight_management = weight_management
        self.dietary_restriction = dietary_restriction
        self.gluten_fee = gluten_free
        self.carb_free = carb_free
        self.vegetarian = vegetarian
        self.vegan = vegan

    def __repr__(self):
        return 'Lifestyle: {}'.format(self.id)


class Nutrition(db.Model):
    """ Nutrition table"""
    id = db.Column(db.Integer, primary_key=True)
    serving_size = db.Column(db.String(80))
    calories = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    carbs = db.Column(db.Integer)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, serving_size='none', calories=0, fat=0, protein=0, carbs=0):
        self.serving_size = serving_size
        self.calories = calories
        self.fat = fat
        self.protein = protein
        self.carbs = carbs

    def __repr__(self):
        return 'Nutrition: {}'.format(self.id)


class Category(db.Model):
    """ Category table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    products = db.relationship('Product', backref='category', lazy='dynamic')
    recipes = db.relationship('Recipe', backref='category', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Category: {}'.format(self.name)
