"""models file"""
from app import db

# join table for ingredients and lifestyles
iltable = db.Table('iltable',
        db.Column('ing_id', db.Integer, db.ForeignKey('ingredient.id')),
        db.Column('lif_id', db.Integer, db.ForeignKey('lifestyle.id')))

# join table for recipes and lifestyles
rltable = db.Table('rltable',
        db.Column('rec_id', db.Integer, db.ForeignKey('recipe.id')),
        db.Column('lif_id', db.Integer, db.ForeignKey('lifestyle.id')))

# join table for products and lifestyles
pltable = db.Table('pltable',
        db.Column('pro_id', db.Integer, db.ForeignKey('product.id')),
        db.Column('lif_id', db.Integer, db.ForeignKey('lifestyle.id')))

class Ingredient(db.Model):
    """ Ingredient table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    img = db.Column(db.String(200))
    calories = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    carbs = db.Column(db.Integer)
    ingredientlists = db.relationship('Ingredientlist', backref='ingredient', lazy='dynamic')
    lifestyles = db.relationship('Lifestyle', secondary=iltable, backref='ingredients', lazy='dynamic')

    def __init__(self, name, img='', calories=0, protein=0, fat=0, carbs=0, lifestyles=[]):
        self.name = name
        self.img = img
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        if lifestyles:
            for lifestyle in lifestyles:
                self.lifestyles.append(lifestyle)

    def __repr__(self):
        return 'Ingredient: {}'.format(self.name)


class Recipe(db.Model):
    """ Recipe table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    img = db.Column(db.String(200))
    time = db.Column(db.Integer)
    instructions = db.Column(db.String(10000))
    servings = db.Column(db.Integer)
    ingredientlists = db.relationship('Ingredientlist', backref='recipe', lazy='dynamic')
    lifestyles = db.relationship('Lifestyle', secondary=rltable, backref='recipes', lazy='dynamic')

    def __init__(self, name, img='', time=0, instructions='', servings=0, lifestyles=[]):
        self.name = name
        self.img = img
        self.time = time
        self.instructions = instructions
        self.servings = servings
        if lifestyles:
            for lifestyle in lifestyles:
                self.lifestyles.append(lifestyle)

    def __repr__(self):
        return 'Recipe: {}'.format(self.name)


class Product(db.Model):
    """ Product table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    img = db.Column(db.String(200))
    servingsize = db.Column(db.String(100))
    calories = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    satfat = db.Column(db.Integer)
    transfat = db.Column(db.Integer)
    carbs = db.Column(db.Integer)
    sugar = db.Column(db.Integer)
    lifestyles = db.relationship('Lifestyle', secondary=pltable, backref='products', lazy='dynamic')

    def __init__(self, name, img='', servingsize=0, calories=0, protein=0, fat=0, satfat=0,
                 transfat=0, carbs=0, sugar=0, lifestyles=[]):
        self.name = name
        self.img = img
        self.servingsize = servingsize
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.satfat = satfat
        self.transfat = transfat
        self.carbs = carbs
        self.sugar = sugar
        if lifestyles:
            for lifestyle in lifestyles:
                self.lifestyles.append(lifestyle)

    def __repr__(self):
        return 'Product: {}'.format(self.name)


class Lifestyle(db.Model):
    """ Lifestyle table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    img = db.Column(db.String(200))
    description = db.Column(db.String(500))
    weight_management = db.Column(db.Boolean)
    gluten_free = db.Column(db.Boolean)
    ketogenic = db.Column(db.Boolean)
    vegetarian = db.Column(db.Boolean)
    vegan = db.Column(db.Boolean)
    cheap = db.Column(db.Boolean)
    dairy_free = db.Column(db.Boolean)

    def __init__(self, name, img='', description='', weight_management=False,  gluten_free=False,
                 ketogenic=False, vegetarian=False, vegan=False, cheap=False, dairy_free=False):
        self.name = name
        self.img = img
        self.description = description
        self.weight_management = weight_management
        self.gluten_free = gluten_free
        self.ketogenic = ketogenic 
        self.vegetarian = vegetarian
        self.vegan = vegan
        self.cheap = cheap
        self.dairy_free = dairy_free

    def __repr__(self):
        return 'Lifestyle: {}'.format(self.name)

class Ingredientlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    unit = db.Column(db.String(50))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    def __init__(self, amount=0, unit='', recipe=None, ingredient=None):
        self.amount = amount
        self.unit = unit
        if recipe:
            recipe.ingredientlists.append(self)
        if ingredient:
            ingredient.ingredientlists.append(self)

    def __repr__(self):
        return 'Ingredientlist: {}'.format(self.id)
