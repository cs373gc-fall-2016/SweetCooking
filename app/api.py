from app import app
from .models import *
from flask import jsonify
import flask_restful
import pdb

api = flask_restful.Api(app)

class IngredientHandler(flask_restful.Resource):
  def get(self):
    pdb.set_trace()
    ingredients = Ingredient.query.all()
    ii = {}
    for ingredient in ingredients:
      ii[ingredient.id] = ingredient.name
    return jsonify(ii)

api.add_resource(IngredientHandler, '/api/ingredients/')   

