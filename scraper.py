from app import *
from app.models import *
import json
import re
import urllib.request
from keys import *

USDAURL = 'http://api.nal.usda.gov/ndb'
SPOONURL = 'https://spoonacular-recipe-food-nutrition-v1.p.mashape.com'
PRODUCTS = ['candy', 'cake', 'pasta', 'chips', 'ice cream', 'cookies', 'burger', 'pizza',
            'eggs', 'bacon', 'cereal', 'hot pockets', 'ramen', 'oatmeal', 'mac and cheese',
            'burritos', 'tacos', 'sandwhich', 'salad', 'gatoraid', 'soda', 'wine', 'beer']
spoonheaders = {'X-Mashape-Key': SPOONKEY}
productsearch = SPOONURL + '/food/products/search?'
productvalues = {'number': 25, 'offset': 0, 'query': 'nothing'}
productid = SPOONURL + '/food/products/'
recipesearch = SPOONURL + '/recipes/random?'
recipevalues = {'limitLicense': 'false', 'number': 50}
specrecipesearch = SPOONURL + '/recipes/search/?'
specrecipevalues = {'limitLicense': 'false', 'query' : ''}

usdasearch = {'format': 'json', 'max': 1, 'ds': 'Standard Reference', 'api_key': USDAKEY, 'q': ''}
usdasearchurl = USDAURL + '/search/?'
usdareport = {'ndbno': 0, 'format': 'json', 'api_key': USDAKEY}
usdareporturl = USDAURL +'/reports/?'

def makeLifestyles():
    print('Making Lifestyles')
    lifestyles = []
    lifestyles.append(Lifestyle('Weight Management', weight_management=True))
    lifestyles.append(Lifestyle('Gluten Free', gluten_free=True))
    lifestyles.append(Lifestyle('Ketogenic', ketogenic=True))
    lifestyles.append(Lifestyle('Vegetarian', vegetarian=True))
    lifestyles.append(Lifestyle('Vegan', vegan=True))
    lifestyles.append(Lifestyle('Cheap', cheap=True))
    lifestyles.append(Lifestyle('Dairy Free', dairy_free=True))
    lifestyles.append(Lifestyle('Everyday'))
    for lifestyle in lifestyles:
        db.session.add(lifestyle)
    db.session.commit()

def makeProducts():
    print('Making Products')
    for product in PRODUCTS:
        productvalues['query'] = product
        searchurl = productsearch+urllib.parse.urlencode(productvalues)
        req = urllib.request.Request(searchurl, headers=spoonheaders)
        results = urllib.request.urlopen(req).read().decode()
        results = json.loads(results)
        results = results['products']
        for result in results:
            name = result['title']
            pid = result['id']
            indsearchurl = productid + str(pid)
            req = urllib.request.Request(indsearchurl, headers=spoonheaders)
            indproduct = urllib.request.urlopen(req).read().decode()
            indproduct = json.loads(indproduct)
            info = indproduct['nutrition_widget']
            calories = getCalories(info)
            protein = getProtein(info)
            fat = getFat(info)
            carbs = getCarbs(info)
            satFat = getSatFat(info)
            transFat = getTransFat(info)
            sugar = getSugar(info)
            servingsize = indproduct['serving_size'] if indproduct['serving_size'] else 'unknown'
            img = indproduct['images'][0]
            lfs = processProdBadges(indproduct['badges'])
            newproduct = Product(name, img=img, servingsize=servingsize, calories=calories, protein=protein,
                                 fat=fat, satfat=satFat, transfat=transFat, carbs=carbs, sugar=sugar,
                                 lifestyles=lfs)
            db.session.add(newproduct)
        db.session.commit()

def makeRecipes():
    print('Making Recipes')
    vals = urllib.parse.urlencode(recipevalues)
    recurl = recipesearch+vals
    req = urllib.request.Request(recurl, headers=spoonheaders)
    results = urllib.request.urlopen(req).read().decode()
    results = json.loads(results)
    results = results['recipes']
    for result in results:
        name = result['title']
        #see if we already have this recipe
        if len(Recipe.query.filter_by(name=name).all()):
            continue
        img = result['image']
        time = result['readyInMinutes']
        instructions = result['instructions']
        if instructions:
            trim = re.search('\s+(.+)[\.\!\?]\s', result['instructions'])
            instructions = trim.group(1) if trim else instructions
        else:
            instructions = 'No instructions found'
        servings = result['servings'] if result['servings'] else 1
        lfs = getLifestylesForRecipes(result)
        ingredients = result['extendedIngredients']
        ingredients = getIngredients(ingredients)
        rec = Recipe(name=name, img=img, time=time, instructions=instructions, servings=servings,
                     lifestyles=lfs)
        for ingredient, amount, unit in ingredients:
            inglist = Ingredientlist(amount=amount, unit=unit, recipe=rec, ingredient=ingredient)
            db.session.add(inglist)
        db.session.commit()

#grabs ingredients from the db or makes them if not already in there
def getIngredients(ingredients):
    ings = []
    for ingredient in ingredients:
        name = ingredient['name']
        amount = ingredient['amount']
        unit = ingredient['unitLong']
        ing = Ingredient.query.filter_by(name=name).first()
        if ing:
            ings.append((ing, amount, unit))
            continue
        img = ingredient['image'] if 'image' in ingredient else ''
        usdasearch['q'] = name
        searchurl = usdasearchurl+urllib.parse.urlencode(usdasearch)
        req = urllib.request.Request(searchurl)
        results = urllib.request.urlopen(req).read().decode()
        results = json.loads(results)
        if 'list' not in results:
            continue
        ndbno = results['list']['item'][0]['ndbno']
        usdareport['ndbno'] = ndbno
        reporturl = usdareporturl + urllib.parse.urlencode(usdareport)
        req = urllib.request.Request(reporturl)
        results = urllib.request.urlopen(req).read().decode()
        results = json.loads(results)
        result = results['report']['food']['nutrients']
        result = getIngredientInfo(result)
        ing = Ingredient(name=name, img=img, calories=result['calories'], protein=result['protein'],
                         fat=result['fat'], carbs=result['carbs'])
        db.session.add(ing)
        ings.append((ing, amount, unit))
    db.session.commit()
    return ings

def getLifestylesForRecipes(info):
    lfs = []
    wm = False
    if info['ketogenic']:
        lfs.append(Lifestyle.query.filter_by(ketogenic=True).first())
        wm = True
    if info['vegetarian']:
        lfs.append(Lifestyle.query.filter_by(vegetarian=True).first())
        wm = True
    if info['vegan']:
        lfs.append(Lifestyle.query.filter_by(vegan=True).first())
        wm = True
    if info['glutenFree']:
        lfs.append(Lifestyle.query.filter_by(gluten_free=True).first())
    if info['cheap']:
        lfs.append(Lifestyle.query.filter_by(cheap=True).first())
    if info['dairyFree']:
        lfs.append(Lifestyle.query.filter_by(dairy_free=True).first())
    if wm or info['veryHealthy']:
        lfs.append(Lifestyle.query.filter_by(weight_management=True).first())
    if not lfs:
        lfs.append(Lifestyle.query.filter_by(name='Everyday').first())
    return lfs

def getCalories(info):
    calories = re.search('(\d+) Calorie', info)
    if calories:
        calories = int(calories.group(1))
    return calories if calories else 0

def getProtein(info):
    protein = re.search('(\d+)g Protein', info)
    if protein:
        protein = int(protein.group(1))
    return protein if protein else 0

def getFat(info):
    fat = re.search('(\d+)g Total Fat', info)
    if fat:
        fat = int(fat.group(1))
    return fat if fat else 0

def getCarbs(info):
    carbs = re.search('(\d+)g Carb', info)
    if carbs:
        carbs = int(carbs.group(1))
    return carbs if carbs else 0

def getSatFat(info):
    satFat = re.search('Saturated Fat\D*(\d+)g', info)
    if satFat:
        satFat = int(satFat.group(1))
    return satFat if satFat else 0

def getTransFat(info):
    transFat = re.search('Trans Fat\D*(\d+)g', info)
    if transFat:
        transFat = int(transFat.group(1))
    return transFat if transFat else 0

def getSugar(info):
    sugar = re.search('Sugar\D*(\d+)g', info)
    if sugar:
        sugar = int(sugar.group(1))
    return sugar if sugar else 0

def processProdBadges(badges):
    lfs = []
    wm = False
    if 'ketogenic' in badges:
        lfs.append(Lifestyle.query.filter_by(ketogenic=True).first())
        wm = True
    if 'vegetarian' in badges:
        lfs.append(Lifestyle.query.filter_by(vegetarian=True).first())
        wm = True
    if 'vegan' in badges:
        lfs.append(Lifestyle.query.filter_by(vegan=True).first())
        wm = True
    if 'gluten_free' in badges:
        lfs.append(Lifestyle.query.filter_by(gluten_free=True).first())
    if 'cheap' in badges:
        lfs.append(Lifestyle.query.filter_by(cheap=True).first())
    if 'dairy_free' in badges:
        lfs.append(Lifestyle.query.filter_by(dairy_free=True).first())
    if wm or 'healthy' in badges or 'paleo' in badges or 'primal' in badges:
        lfs.append(Lifestyle.query.filter_by(weight_management=True).first())
    if not lfs:
        lfs.append(Lifestyle.query.filter_by(name='Everyday').first())
    return lfs

# response['report']['food']['nutrients']
def getIngredientInfo(info):
    stuffs = {'Energy': 'calories', 'Protein': 'protein', 'Total lipid (fat)': 'fat', 
              'Carbohydrate, by difference': 'carbs'}
    result = {}
    for nutrient in info:
        if nutrient['name'] in stuffs:
            result[stuffs[nutrient['name']]] = int(float(nutrient['value']))
    return result

def updateIngredientLifestyle():
    print('Updating Ingredient Lifestyles')
    for ing in Ingredient.query.all():
        lfs = []
        for ingl in ing.ingredientlists:
            for lifestyle in ingl.recipe.lifestyles:
                if lifestyle not in lfs:
                    lfs.append(lifestyle)
        everyday = Lifestyle.query.filter_by(name='Everyday').first()
        if everyday not in lfs:
            lfs.append(everyday)
        for lf in lfs:
            ing.lifestyles.append(lf)
        db.session.add(ing)
        db.session.commit()

#makeLifestyles()
#makeProducts()
#for x in range(10):
    #makeRecipes()
updateIngredientLifestyle()
