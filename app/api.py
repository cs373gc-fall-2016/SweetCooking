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
        'recipes_name': [Recipe.query.filter_by(id=x.recipe_id).first().name for x in ingredient.ingredientlists],
        'recipe_id': [x.recipe_id for x in ingredient.ingredientlists],
        'lifestyles_name': [x.name for x in ingredient.lifestyles],
        'lifestyles_id': [x.id for x in ingredient.lifestyles],
      }
    
    return jsonify(ingredient_response)


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
        'ingredients_name': [Ingredient.query.filter_by(id=x.ingredient_id).first().name for x in recipe.ingredientlists],
        'ingredients_id': [x.ingredient_id for x in recipe.ingredientlists],
        'lifestyles_name': [x.name for x in recipe.lifestyles],
        'lifestyles_id': [x.id for x in recipe.lifestyles],
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
        'lifestyles_name': [x.name for x in product.lifestyles],
        'lifestyles_id': [x.id for x in product.lifestyles],
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


class LifestyleHandler(flask_restful.Resource):
  def get(self, lifestyle_id):
    lifestyle = Lifestyle.query.filter_by(id=lifestyle_id)
    lifestyle = lifestyle.first()
    lifestyle_response = {}

    if lifestyle:
      lifestyle_response = {
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
        'recipes_name': [x.name for x in lifestyle.recipes],
        'recipe_id': [x.id for x in lifestyle.recipes],
        'products_name': [x.name for x in lifestyle.products],
        'products_id': [x.id for x in lifestyle.products],
      }

    return jsonify(lifestyle_response)

api.add_resource(LifestyleHandler, '/api/lifestyles/<int:lifestyle_id>')  

  

