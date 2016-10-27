import json 
import unirest

# API Key
key = "OcRwM76HnGmshIbGYAEP5tC5CzWyp1k6xlOjsnzQyvIoZQLcn5"

# header for API call
head = {"X-Mashape-Key": "OcRwM76HnGmshIbGYAEP5tC5CzWyp1k6xlOjsnzQyvIoZQLcn5", "Accept": "application/json"} 

# first part of the url for API call
url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/"

# we can increase the number of recipes returned up to 100
num = "number=" + "10"

# these are the meal types we will use to find recipes 
### we can add more meal types to this list
meal_types = ["taco", "hamburger", "pizza", "fruit"]

# this will get all the recipe ids for each meal type
# Ex {"taco": [recipe ids]}
recipe_ids = {}

# recipes can point to ingredients/life_styles/
# Ex {recipe id: {}}
recipes = {}

# {id: {"name": String, "aisle": String, "image", String, "recipes": [ids]}}
# can point to recipes
ingredients = {}

# holds the recipe id for each type
# can point to recipes
life_styles = {"vegan":[], "dairyFree":[], "glutenFree":[], "cheap":[], "veryPopular":[]}

# haven't figured out this part
products = {}

# get recipe id's for each meal_type
# Get Search Recipes
for i in range(len(meal_types)):
	food = meal_types[i]
	
	# build the url for the API call
	url_string = url + "search?" + num + "&query=" + food
	response = unirest.get(url_string, headers = head)

	for v in response.body["results"]:
		# initialize the empty list for food product recipe ids
		if food not in recipe_ids:
			recipe_ids[food] = []
			
		# add recipe id to list
		arr = recipe_ids[food]
		arr.append(v["id"])	
		recipe_ids[food] = arr

# put all recipes in one dict
# GET Get Recipe Information
nutrition = "/information?includeNutrition=" + "false"
for food_type in recipe_ids:
	print("food type: " + food_type)
	
	for i in range(len(recipe_ids[food_type])):
		# build url for API call
		url_string = url + str(recipe_ids[food_type][i]) + nutrition
		response = unirest.get(url_string, headers = head)
		
		# add recipe to recipe dict
		recipes[recipe_ids[food_type][i]] = response.body

		# add recipe to lifestyle attributes
		if response.body["vegan"] == True and response.body["id"] not in life_styles["vegan"]:
			life_styles["vegan"].append(response.body["id"])
		if response.body["dairyFree"] == True and response.body["id"] not in life_styles["dairyFree"]:
			life_styles["dairyFree"].append(response.body["id"])
		if response.body["glutenFree"] == True and response.body["id"] not in life_styles["glutenFree"]:
			life_styles["glutenFree"].append(response.body["id"])
		if response.body["cheap"] == True and response.body["id"] not in life_styles["cheap"]:
			life_styles["cheap"].append(response.body["id"])
		if response.body["veryPopular"] == True and response.body["id"] not in life_styles["veryPopular"]:
			life_styles["veryPopular"].append(response.body["id"])
		
		# extract ingredients from recipe
		for v in response.body["extendedIngredients"]:
			# if ingredient is new to list gather all data of ingredient
			if v["id"] not in ingredients:
				temp_ing_dict = {}
				temp_ing_dict["name"] = v["name"]
				temp_ing_dict["image"] = v["image"]
				
				# some ingredients don't have an aisle attribute
				if "aisle" in v:
					temp_ing_dict["aisle"] = v["aisle"]
				else:
					temp_ing_dict["aisle"] = None
					
				# create recipe list for ingredient
				temp_ing_recipes = []
				temp_ing_recipes.append(response.body["id"])
				ing_dict["recipes"] = temp_ing_recipes
				
				# add ingredient to ingredient dict
				ingredients[v["id"]] = ing_dict
			# just add the recipe id to ingredient's recipe list
			else:
				ingredients[v["id"]]["recipes"].append(response.body["id"])
	

		
print(ingredients)	
print(life_styles)	

















