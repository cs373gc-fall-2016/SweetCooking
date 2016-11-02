from app import app
from .models import *
from flask import jsonify
import flask_restful
import pdb

api = flask_restful.Api(app)

class IngredientHandler(flask_restful.Resource):
  def get(self):
    # pdb.set_trace()
    ingredients = Ingredient.query.all()
    ingredients_lib = {}

    for ingredient in ingredients:
      ingredient_data = []
      ingredient_data.append(ingredient.name)
      ingredient_data.append(str(ingredient.calories))
      ingredient_data.append(str(ingredient.protein))
      ingredient_data.append(str(ingredient.fat))
      ingredient_data.append(str(ingredient.carbs))
      ingredients_lib[ingredient.id] = ingredient_data

    return jsonify(ingredients_lib)

api.add_resource(IngredientHandler, '/api/ingredients/')   

