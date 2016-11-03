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
      }
    
    return jsonify(ingredient_response)



class RecipesHandler(flask_restful.Resource):
  def get(self):
    recipes = Recipe.query.all()
    recipes_lib = {}

    for recipe in recipes:
      recipe_data = []
      recipe_data.append('<a href=' + recipe.img + '>' + recipe.name + '</a>')
      recipe_data.append(str(recipe.time))
      recipe_data.append(recipe.instructions)
      recipe_data.append(recipe.servings)
      recipes_lib[recipe.id] = recipe_data

    return jsonify(recipes_lib)



class ProductsHandler(flask_restful.Resource):
  def get(self):
    products = Product.query.all()
    products_lib = {}

    for product in products:
      product_data = []
      product_data.append('<a href=' + product.img + '>' + product.name + '</a>')
      product_data.append(product.servingsize)
      product_data.append(product.calories)
      product_data.append(product.protein)
      product_data.append(product.fat)
      product_data.append(product.satfat)
      product_data.append(product.transfat) 
      product_data.append(product.carbs) 
      product_data.append(product.sugar) 
      products_lib[product.id] = product_data

    return jsonify(products_lib)



class LifestylesHandler(flask_restful.Resource):
  def get(self):
    lifestyles = Lifestyle.query.all()
    lifestyles_lib = {}

    for lifestyle in lifestyles:
      lifestyle_data = []
      lifestyle_data.append('<a href=' + lifestyle.img + '>' + lifestyle.name + '</a>')
      lifestyle_data.append(lifestyle.description)
      lifestyle_data.append(lifestyle.weight_management)
      lifestyle_data.append(lifestyle.gluten_free)
      lifestyle_data.append(lifestyle.ketogenic)
      lifestyle_data.append(lifestyle.vegetarian)
      lifestyle_data.append(lifestyle.vegan)
      lifestyle_data.append(lifestyle.cheap)
      lifestyle_data.append(lifestyle.dairy_free)
      lifestyles_lib[lifestyle.id] = lifestyle_data

    return jsonify(lifestyles_lib)


class CSearchHandler(flask_restful.Resource):
  def get(self, query):
    print('kkkkkkkkk')
    print(query)
    if query is None:
      return "query cannot be empty"
    elif query.strip() == "":
      return "query cannot be empty"

    results = []

    ingredients = Ingredient.search(query)
    # recipes = Recipe.search(query)
    # products = Product.search(query)
    # lifestyles = Lifestyle.search(query)

    results.append(ingredients)
    # results.append(recipes)
    # results.append(products)
    # results.append(lifestyles)

    return jsonify(results=results)




api.add_resource(IngredientsHandler, '/api/ingredients/')   
api.add_resource(IngredientHandler, '/api/ingredients/<int:ingredient_id>')  

api.add_resource(RecipesHandler, '/api/recipes/')   
# api.add_resource(RecipeHandler, '/api/recipes/<int:recipe_id>') 

api.add_resource(ProductsHandler, '/api/products/') 
# api.add_resource(ProductHandler, '/api/products/<int:product_id>') 

api.add_resource(LifestylesHandler, '/api/lifestyles/')  
# api.add_resource(LifestyleHandler, '/api/lifestyles/<int:lifestyle_id>') 

api.add_resource(CSearchHandler, '/api/csearch/<string:query>')






  

