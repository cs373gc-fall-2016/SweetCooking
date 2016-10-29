#!/usr/bin/envalpython3

# -------
# imports
# -------
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)
import unittest
from unittest import main, TestCase
from app.models import Ingredient, Recipe, Product, Lifestyle


# ----------------
# TestIngredient
# ----------------
class TestIngredient(TestCase):

    def setUp(self):
        db.create_all()
        ingredient1 = Ingredient('name1')
        ingredient2 = Ingredient('name2', 5, 'all of the seasons')
        db.session.add(ingredient1)
        db.session.add(ingredient2)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all(self):
        ingredients = Ingredient.query.all()
        self.assertEqual(len(ingredients), 2)
        
    def test_filter_1(self):
        ingredient = Ingredient.query.filter(Ingredient.name == 'name1').first()
        self.assertEqual(ingredient.price, 0)

    def test_filter_2(self):
        ingredient = Ingredient.query.filter(Ingredient.price == 5).first()
        self.assertEqual(ingredient.name, 'name2')

    def test_add_delete(self):
        ingredient = Ingredient('name3')
        db.session.add(ingredient)
        db.session.commit()
        self.assertEqual(len(Ingredient.query.all()), 3)
        Ingredient.query.filter(Ingredient.name == 'name3').delete()
        db.session.commit()
        self.assertEqual(len(Ingredient.query.all()), 2)
        
# ----------------
# TestRecipe
# ----------------
class TestRecipe(TestCase):

    def setUp(self):
        db.create_all()
        recipe1 = Recipe('name1')
        recipe2 = Recipe('name2', 5, 'Amurrica', 10)
        db.session.add(recipe1)
        db.session.add(recipe2)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all(self):
        recipes = Recipe.query.all()
        self.assertEqual(len(recipes), 2)
        
    def test_filter_1(self):
        recipe = Recipe.query.filter(Recipe.name == 'name1').first()
        self.assertEqual(recipe.price, 0)

    def test_filter_2(self):
        recipe = Recipe.query.filter(Recipe.price == 5).first()
        self.assertEqual(recipe.name, 'name2')

    def test_add_delete(self):
        recipe = Recipe('name3')
        db.session.add(recipe)
        db.session.commit()
        self.assertEqual(len(Recipe.query.all()), 3)
        Recipe.query.filter(Recipe.name == 'name3').delete()
        db.session.commit()
        self.assertEqual(len(Recipe.query.all()), 2)
        
# ----------------
# TestProduct
# ----------------
class TestProduct(TestCase):

    def setUp(self):
        db.create_all()
        product1 = Product('name1')
        product2 = Product('name2', 5, 'super fancy creamcakes!')
        db.session.add(product1)
        db.session.add(product2)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all(self):
        products = Product.query.all()
        self.assertEqual(len(products), 2)
        
    def test_filter_1(self):
        product = Product.query.filter(Product.name == 'name1').first()
        self.assertEqual(product.price, 0)

    def test_filter_2(self):
        product = Product.query.filter(Product.price == 5).first()
        self.assertEqual(product.name, 'name2')

    def test_add_delete(self):
        product = Product('name3')
        db.session.add(product)
        db.session.commit()
        self.assertEqual(len(Product.query.all()), 3)
        Product.query.filter(Product.name == 'name3').delete()
        db.session.commit()
        self.assertEqual(len(Product.query.all()), 2)
        
# ----------------
# TestLifestyle
# ----------------
class TestLifestyle(TestCase):

    def setUp(self):
        db.create_all()
        lifestyle1 = Lifestyle()
        lifestyle2 = Lifestyle(True, 'nadda', True, True)
        db.session.add(lifestyle1)
        db.session.add(lifestyle2)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all(self):
        lifestyles = Lifestyle.query.all()
        self.assertEqual(len(lifestyles), 2)
        
    def test_filter_1(self):
        lifestyle = Lifestyle.query.filter(Lifestyle.dietary_restriction == 'none').first()
        self.assertEqual(lifestyle.price, 0)

    def test_filter_2(self):
        lifestyle = Lifestyle.query.filter(Lifestyle.gluten_free == True).first()
        self.assertEqual(lifestyle.dietary_restriction, 'nadda')

    def test_add_delete(self):
        lifestyle = Lifestyle(dietary_restriction='delete me')
        db.session.add(lifestyle)
        db.session.commit()
        self.assertEqual(len(Lifestyle.query.all()), 3)
        Lifestyle.query.filter(Lifestyle.dietary_restriction == 'delete me').delete()
        db.session.commit()
        self.assertEqual(len(Lifestyle.query.all()), 2)
        
# ----
# main
# ----
if __name__ == "__main__":
    main()
