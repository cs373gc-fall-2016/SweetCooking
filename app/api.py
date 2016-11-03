from app import app
from .models import *
from flask import jsonify
import flask_restful
import pdb

api = flask_restful.Api(app)

class IngredientsHandler(flask_restful.Resource):
  def get(self):
    ingredients = Ingredient.query.all()
    
    ingredients_response = {}
    for ingredient in ingredients:
      ingredient_data = {
        'id': ingredient.id,
        'name': ingredient.name,
        'img': ingredient.img,
        'calories': ingredient.calories,
        'protein': ingredient.protein,
        'fat': ingredient.fat,
        'carbs': ingredient.carbs,
      }
      ingredients_response[ingredient.id] = ingredient_data

    return jsonify(ingredients_response)

api.add_resource(IngredientsHandler, '/api/ingredients/')   

class IngredientHandler(flask_restful.Resource):
  def get(self, ingredient_id):
    ingredient = Ingredient.query.filter_by(id=ingredient_id)
    ingredient = ingredient.first()
    ingredient_response = {}

    if ingredient:
      ingredient_response = {
        'id': ingredient.id,
        'name': ingredient.name,
        'img': ingredient.img,
        'calories': ingredient.calories,
        'protein': ingredient.protein,
        'fat': ingredient.fat,
        'carbs': ingredient.carbs,
      }
    
    return jsonify(ingredient_response)

api.add_resource(IngredientHandler, '/api/ingredients/<int:ingredient_id>')  


class RecipesHandler(flask_restful.Resource):
  def get(self):
    recipes = Recipe.query.all()
    recipes_response = {}

    for recipe in recipes:
      recipe_data = {
        'id': recipe.id,
        'name': recipe.name,
        'img': recipe.img,
        'time': recipe.time,
        'instructions': recipe.instructions,
        'servings': recipe.servings,
      }

      recipes_response[recipe.id] = recipe_data

    return jsonify(recipes_response)

api.add_resource(RecipesHandler, '/api/recipes/')   


class RecipeHandler(flask_restful.Resource):
  def get(self, recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id)
    recipe = recipe.first()
    recipe_response = {}
    if recipe:
      recipe_response = {
        'id': recipe.id,
        'name': recipe.name,
        'img': recipe.img,
        'time': recipe.time,
        'instructions': recipe.instructions,
        'servings': recipe.servings,
      }

    return jsonify(recipe_response)

api.add_resource(RecipeHandler, '/api/recipes/<int:recipe_id>') 


class ProductsHandler(flask_restful.Resource):
  def get(self):
    products = Product.query.all()
    products_response = {}

    for product in products:
      product_data = {
        'id': product.id,
        'name': product.name,
        'img': product.img,
        'servingsize': product.servingsize,
        'calories': product.calories,
        'protein': product.protein,
        'fat': product.fat,
        'satfat': product.satfat,
        'transfat': product.transfat,
        'carbs': product.carbs,
        'sugar': product.sugar,
      }
      products_response[product.id] = product_data

    return jsonify(products_response)

api.add_resource(ProductsHandler, '/api/foodproducts/') 

class ProductHandler(flask_restful.Resource):
  def get(self, product_id):
    product = Product.query.filter_by(id=product_id)
    product = product.first()
    product_response = {}

    if product:
      product_response = {
        'id': product.id,
        'name': product.name,
        'img': product.img,
        'servingsize': product.servingsize,
        'calories': product.calories,
        'protein': product.protein,
        'fat': product.fat,
        'satfat': product.satfat,
        'transfat': product.transfat,
        'carbs': product.carbs,
        'sugar': product.sugar,
      }

    return jsonify(product_response)

api.add_resource(ProductHandler, '/api/foodproducts/<int:product_id>') 

class LifestylesHandler(flask_restful.Resource):
  def get(self):
      lifestyles = Lifestyle.query.all()
      lifestyles_response = {}

      for lifestyle in lifestyles:
        lifestyle_data = {
          'id': lifestyle.id,
          'name': lifestyle.name,
          'img': lifestyle.img,
          'description': lifestyle.description,
          'weight_management': lifestyle.weight_management,
          'gluten_free': lifestyle.gluten_free,
          'ketogenic': lifestyle.ketogenic,
          'vegetarian': lifestyle.vegetarian,
          'vegan': lifestyle.vegan,
          'cheap': lifestyle.cheap,
          'dairy_free': lifestyle.dairy_free,
        }
        lifestyles_response[lifestyle.id] = lifestyle_data

      return jsonify(lifestyles_response)

api.add_resource(LifestylesHandler, '/api/lifestyles/')   



  

