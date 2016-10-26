""" Sweet Cooking Team Fall 2016 Test Harness """
#!/usr/bin/envalpython3

# -------
# imports
# -------
import os
import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import *
from app.models import *

# ----------
# TestModels
# ----------
class TestModels(unittest.TestCase):
    """ test models """

    @classmethod
    def setUpClass(cls):
        """ setup basic stuf for tests """
        if os.path.isfile('app.db'):
            os.remove('app.db')
        db.create_all()

        # setup a small database
        sammich = Recipe('ham sandwhich', 'sammich.jpg', 5, 'Put stuff between bread', 1)
        bread = Ingredient('bread', 'bread.jpg', 50, 3, 0, 10)
        ham = Ingredient('ham', 'ham.jpg', 100, 10, 2, 0)
        mustard = Ingredient('mustard', 'mustard.jpg')
        ingl1 = Ingredientlist(2, 'slice', sammich, bread)
        ingl2 = Ingredientlist(1, 'slice', sammich, ham)
        ingl3 = Ingredientlist(5, 'oz', sammich, mustard)
        fatty = Lifestyle('unhealthy', 'fatty.jpg')
        sammich.lifestyles.append(fatty)
        bread.lifestyles.append(fatty)
        ham.lifestyles.append(fatty)
        mustard.lifestyles.append(fatty)
        candy = Product('super awesome candy', 'candy.jpg', 5, 90001, 0, 5000, 3000, 2000, 15, 15, (fatty,))
        db.session.add(sammich)
        db.session.add(bread)
        db.session.add(ham)
        db.session.add(mustard)
        db.session.add(ingl1)
        db.session.add(ingl2)
        db.session.add(ingl3)
        db.session.add(fatty)
        db.session.add(candy)
        db.session.commit()

    # # -----
    # # Query
    # # -----
    def test_query_1(self):
        """ test query look up using sammich """
        sammich = Recipe.query.filter_by(name='ham sandwhich').first()
        self.assertEqual(sammich.name, 'ham sandwhich')
        self.assertEqual(sammich.img, 'sammich.jpg')
        
    def test_query_2(self):
        """ test query look up using mustard """
        mustard = Ingredient.query.filter_by(name='mustard').first()
        self.assertEqual(mustard.name, 'mustard')
        self.assertEqual(mustard.img, 'mustard.jpg')
        
    def test_query_3(self):
        """ test query look up using candy """
        candy = Product.query.filter_by(name='super awesome candy').first()
        self.assertEqual(candy.name, 'super awesome candy')
        self.assertEqual(candy.img, 'candy.jpg')
        

# ----
# main
# ----
if __name__ == "__main__":
    unittest.main()
