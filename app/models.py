"""DB models file"""
from app import db

# join table for ingredients and lifestyles
iltable = db.Table('iltable', db.Column('ing_id', db.Integer, db.ForeignKey('ingredient.id')), db.Column('lif_id', db.Integer, db.ForeignKey('lifestyle.id')))

# join table for recipes and lifestyles
rltable = db.Table('rltable', db.Column('rec_id', db.Integer, db.ForeignKey('recipe.id')), db.Column('lif_id', db.Integer, db.ForeignKey('lifestyle.id')))

# join table for products and lifestyles
pltable = db.Table('pltable', db.Column('pro_id', db.Integer, db.ForeignKey('product.id')), db.Column('lif_id', db.Integer, db.ForeignKey('lifestyle.id')))

#Ingredient pillar
class Ingredient(db.Model):
    """ Ingredient table default types"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    img = db.Column(db.String(200))
    calories = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    carbs = db.Column(db.Integer)
    ingredientlists = db.relationship('Ingredientlist', backref='ingredient', lazy='dynamic')
    lifestyles = db.relationship('Lifestyle', secondary=iltable, backref='ingredients', lazy='dynamic')

    #set all of the initial/default values
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

#Recipe pillar
class Recipe(db.Model):
    """ Recipe table default types"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    img = db.Column(db.String(200))
    time = db.Column(db.Integer)
    instructions = db.Column(db.String(10000))
    servings = db.Column(db.Integer)
    ingredientlists = db.relationship('Ingredientlist', backref='recipe', lazy='dynamic')
    lifestyles = db.relationship('Lifestyle', secondary=rltable, backref='recipes', lazy='dynamic')

    #set all of the initial/default values
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

#Product pillar
class Product(db.Model):
    """ Product table default types"""
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

    #set all of the initial/default values
    def __init__(self, name, img='', servingsize=0, calories=0, protein=0, fat=0, satfat=0, transfat=0, carbs=0, sugar=0, lifestyles=[]):
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

#Lifestyle pillar
class Lifestyle(db.Model):
    """ Lifestyle table default types"""
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

    #set all of the initial/default values
    def __init__(self, name, img='', description='', weight_management=False, gluten_free=False, ketogenic=False, vegetarian=False, vegan=False, cheap=False, dairy_free=False):
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

#Ingredient list table to help join ingredeints and recipes
class Ingredientlist(db.Model):
    """Ingredient Table default types"""
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    unit = db.Column(db.String(50))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    #set all of the initial/default values
    def __init__(self, amount=0, unit='', recipe=None, ingredient=None):
        self.amount = amount
        self.unit = unit
        if recipe:
            recipe.ingredientlists.append(self)
        if ingredient:
            ingredient.ingredientlists.append(self)

    def __repr__(self):
        return 'Ingredientlist: {}'.format(self.id)


# alexirion$ pylint models.py 
# No config file found, using default configuration
# ************* Module app.models
# C:  5, 0: Line too long (158/100) (line-too-long)
# C:  8, 0: Line too long (154/100) (line-too-long)
# C: 11, 0: Line too long (155/100) (line-too-long)
# C: 24, 0: Line too long (103/100) (line-too-long)
# C: 84, 0: Line too long (137/100) (line-too-long)
# C:118, 0: Line too long (176/100) (line-too-long)
# C:  5, 0: Invalid constant name "iltable" (invalid-name)
# C:  8, 0: Invalid constant name "rltable" (invalid-name)
# C: 11, 0: Invalid constant name "pltable" (invalid-name)
# C: 16, 4: Invalid class attribute name "id" (invalid-name)
# W: 27, 4: Dangerous default value [] as argument (dangerous-default-value)
# R: 27, 4: Too many arguments (8/5) (too-many-arguments)
# R: 14, 0: Too few public methods (0/2) (too-few-public-methods)
# C: 44, 4: Invalid class attribute name "id" (invalid-name)
# W: 54, 4: Dangerous default value [] as argument (dangerous-default-value)
# R: 54, 4: Too many arguments (7/5) (too-many-arguments)
# R: 42, 0: Too few public methods (0/2) (too-few-public-methods)
# R: 68, 0: Too many instance attributes (10/7) (too-many-instance-attributes)
# C: 70, 4: Invalid class attribute name "id" (invalid-name)
# W: 84, 4: Dangerous default value [] as argument (dangerous-default-value)
# R: 84, 4: Too many arguments (12/5) (too-many-arguments)
# R: 68, 0: Too few public methods (0/2) (too-few-public-methods)
# R:103, 0: Too many instance attributes (10/7) (too-many-instance-attributes)
# C:105, 4: Invalid class attribute name "id" (invalid-name)
# R:118, 4: Too many arguments (11/5) (too-many-arguments)
# R:103, 0: Too few public methods (0/2) (too-few-public-methods)
# C:136, 4: Invalid class attribute name "id" (invalid-name)
# R:134, 0: Too few public methods (0/2) (too-few-public-methods)


# Report
# ======
# 115 statements analysed.

# Statistics by type
# ------------------

# +---------+-------+-----------+-----------+------------+---------+
# |type     |number |old number |difference |%documented |%badname |
# +=========+=======+===========+===========+============+=========+
# |module   |1      |1          |=          |100.00      |0.00     |
# +---------+-------+-----------+-----------+------------+---------+
# |class    |5      |5          |=          |100.00      |0.00     |
# +---------+-------+-----------+-----------+------------+---------+
# |method   |10     |10         |=          |100.00      |0.00     |
# +---------+-------+-----------+-----------+------------+---------+
# |function |0      |0          |=          |0           |0        |
# +---------+-------+-----------+-----------+------------+---------+



# External dependencies
# ---------------------
# ::

#     app (app.models)



# Raw metrics
# -----------

# +----------+-------+------+---------+-----------+
# |type      |number |%     |previous |difference |
# +==========+=======+======+=========+===========+
# |code      |116    |75.82 |116      |=          |
# +----------+-------+------+---------+-----------+
# |docstring |6      |3.92  |6        |=          |
# +----------+-------+------+---------+-----------+
# |comment   |13     |8.50  |3        |+10.00     |
# +----------+-------+------+---------+-----------+
# |empty     |18     |11.76 |21       |-3.00      |
# +----------+-------+------+---------+-----------+



# Duplication
# -----------

# +-------------------------+------+---------+-----------+
# |                         |now   |previous |difference |
# +=========================+======+=========+===========+
# |nb duplicated lines      |0     |0        |=          |
# +-------------------------+------+---------+-----------+
# |percent duplicated lines |0.000 |0.000    |=          |
# +-------------------------+------+---------+-----------+



# Messages by category
# --------------------

# +-----------+-------+---------+-----------+
# |type       |number |previous |difference |
# +===========+=======+=========+===========+
# |convention |14     |14       |=          |
# +-----------+-------+---------+-----------+
# |refactor   |11     |11       |=          |
# +-----------+-------+---------+-----------+
# |warning    |3      |3        |=          |
# +-----------+-------+---------+-----------+
# |error      |0      |0        |=          |
# +-----------+-------+---------+-----------+



# Messages
# --------

# +-----------------------------+------------+
# |message id                   |occurrences |
# +=============================+============+
# |invalid-name                 |8           |
# +-----------------------------+------------+
# |line-too-long                |6           |
# +-----------------------------+------------+
# |too-few-public-methods       |5           |
# +-----------------------------+------------+
# |too-many-arguments           |4           |
# +-----------------------------+------------+
# |dangerous-default-value      |3           |
# +-----------------------------+------------+
# |too-many-instance-attributes |2           |
# +-----------------------------+------------+



# Global evaluation
# -----------------
# Your code has been rated at 7.57/10
