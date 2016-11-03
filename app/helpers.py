from app.models import *
from functools import *
from sqlalchemy import asc, desc

""" Helper Methods to traverse tables for various parameters"""

def searchAll(terms):
    """
    search all tables
    """
    terms = terms.split(' ')
    result = {'and': {}, 'or': {}}
    result['and']['recipes'] = andRecipes(terms)
    result['and']['ingredients'] = andIngredients(terms)
    result['and']['products'] = andProducts(terms)
    result['and']['lifestyle'] = andLifestyles(terms)
    result['or']['recipes'] = orRecipes(terms)
    result['or']['ingredients'] = orIngredients(terms)
    result['or']['products'] = orProducts(terms)
    result['or']['lifestyle'] = orLifestyles(terms)
    return result

def searchRecipes(terms):
    """
    search all recipes
    """
    terms = terms.split(' ')
    result = {'and': {}, 'or': {}}
    result['and']['recipes'] = andRecipes(terms)
    result['or']['recipes'] = orRecipes(terms)
    return result

def searchIngredients(terms):
    """
    search all recipes
    """
    terms = terms.split(' ')
    result = {'and': {}, 'or': {}}
    result['and']['ingredients'] = andIngredients(terms)
    result['or']['ingredients'] = orIngredients(terms)
    return result

def searchProducts(terms):
    """
    search products table
    """
    terms = terms.split(' ')
    result = {'and': {}, 'or': {}}
    result['and']['products'] = andProducts(terms)
    result['or']['products'] = orProducts(terms)
    return result

def searchLifestyles(terms):
    """
    search lifestyles table
    """
    terms = terms.split(' ')
    result = {'and': {}, 'or': {}}
    result['and']['lifestyles'] = andLifestyles(terms)
    result['or']['lifestyles'] = orLifestyles(terms)
    return result

def andRecipes(terms):
    """
    searches through recipes using and logic
    """
    recipes = []
    results = Recipe.query.filter(reduce(lambda x, y: x and y,
        map(lambda z: z.lower() in str(Recipe.name).lower(), terms), True))
    for result in results:
        recipe = {}
        recipe['id'] = result.id
        recipe['name'] = result.name
        recipe['img'] = result.img
        recipe['time'] = result.time
        recipe['ingredients'] = [x.id for x in result.ingredientlists]
        recipe['lifestyles'] = [x.id for x in result.lifestyles]
        recipe['servings'] = result.servings
        recipe['instructions'] = result.instructions
        recipes.append(recipe)
    return recipes

def orRecipes(terms):
    """
    searches through recipes using or logic
    """
    everything = {}
    for word in terms:
        recipes = []
        results = Recipe.query.filter(word.lower() in str(Recipe.name).lower())
        for result in results:
            recipe = {}
            recipe['id'] = result.id
            recipe['name'] = result.name
            recipe['img'] = result.img
            recipe['time'] = result.time
            recipe['ingredients'] = [x.id for x in result.ingredientlists]
            recipe['lifestyles'] = [x.id for x in result.lifestyles]
            recipe['servings'] = result.servings
            recipe['instructions'] = result.instructions
            recipes.append(recipe)
        everything[word] = recipes
    return everything

def andIngredients(terms):
    """
    searches through ingredients using and logic
    """
    ingredients = []
    results = Ingredient.query.filter(reduce(lambda x, y: x and y,
        map(lambda z: z.lower() in str(Ingredient.name).lower(), terms), True))
    for result in results:
        ingredient = {}
        ingredient['id'] = result.id
        ingredient['name'] = result.name
        ingredient['img'] = result.img
        ingredient['calories'] = result.calories
        ingredient['protein'] = result.protein
        ingredient['fat'] = result.fat
        ingredient['carbs'] = result.carbs
        ingredient['recipes'] = [x.recipe_id for x in result.ingredientlists]
        ingredient['lifestyles'] = [x.id for x in result.lifestyles]
        ingredients.append(ingredient)
    return ingredients

def orIngredients(terms):
    """
    searches through ingredients using or logic
    """
    everything = {}
    for word in terms:
        ingredients = []
        results = Ingredient.query.filter(word.lower() in str(Ingredient.name).lower())
        for result in results:
            ingredient = {}
            ingredient['id'] = result.id
            ingredient['name'] = result.name
            ingredient['img'] = result.img
            ingredient['calories'] = result.calories
            ingredient['protein'] = result.protein
            ingredient['fat'] = result.fat
            ingredient['carbs'] = result.carbs
            ingredient['recipes'] = [x.recipe_id for x in result.ingredientlists]
            ingredient['lifestyles'] = [x.id for x in result.lifestyles]
            ingredients.append(ingredient)
        everything[word] = ingredients
    return everything

def andProducts(terms):
    """
    searches through products using and logic
    """
    products = []
    results = Product.query.filter(reduce(lambda x, y: x and y,
        map(lambda z: z.lower() in str(Product.name).lower(), terms), True))
    for result in results:
        product = {}
        product['id'] = result.id
        product['name'] = result.name
        product['img'] = result.img
        product['calories'] = result.calories
        product['protein'] = result.protein
        product['fat'] = result.fat
        product['satfat'] = result.satfat
        product['transfat'] = result.transfat
        product['carbs'] = result.carbs
        product['sugar'] = result.sugar
        product['lifestyles'] = [x.id for x in result.lifestyles]
        product['servingsize'] = result.servingsize
        products.append(product)
    return products

def orProducts(terms):
    """
    searches through products using or logic
    """
    everything = {}
    for word in terms:
        products = []
        results = Product.query.filter(word.lower() in str(Product.name).lower())
        for result in results:
            product = {}
            product['id'] = result.id
            product['name'] = result.name
            product['img'] = result.img
            product['calories'] = result.calories
            product['protein'] = result.protein
            product['fat'] = result.fat
            product['satfat'] = result.satfat
            product['transfat'] = result.transfat
            product['carbs'] = result.carbs
            product['sugar'] = result.sugar
            product['lifestyles'] = [x.id for x in result.lifestyles]
            product['servingsize'] = result.servingsize
            products.append(product)
        everything[word] = products
    return everything

def andLifestyles(terms):
    """
    searches through lifestyles using and logic
    """
    lifestyles = []
    results = Lifestyle.query.filter(reduce(lambda x, y: x and y,
        map(lambda z: z.lower() in str(Lifestyle.name).lower(), terms), True))
    for result in results:
        lifestyle = {}
        lifestyle['id'] = result.id
        lifestyle['name'] = result.name
        lifestyle['img'] = result.img
        lifestyle['description'] = result.description
        lifestyle['weightmanage'] = result.weight_management
        lifestyle['glutenfree'] = result.gluten_free
        lifestyle['ketogenic'] = result.ketogenic
        lifestyle['vegetarian'] = result.vegetarian
        lifestyle['vegan'] = result.vegan
        lifestyle['cheap'] = result.cheap
        lifestyle['dairyfree'] = result.dairy_free
        lifestyle['products'] = [x.id for x in result.products]
        lifestyle['recipes'] = [x.id for x in result.recipes]
        lifestyle['ingredients'] = [x.id for x in result.ingredients]
        lifestyles.append(lifestyle)
    return lifestyles

def orLifestyles(terms):
    ''' searches through lifestyles using or logic '''
    everything = {}
    for word in terms:
        lifestyles = []
        results = Lifestyle.query.filter(word.lower() in str(Lifestyle.name).lower())
        for result in results:
            lifestyle = {}
            lifestyle['id'] = result.id
            lifestyle['name'] = result.name
            lifestyle['img'] = result.img
            lifestyle['description'] = result.description
            lifestyle['weightmanage'] = result.weight_management
            lifestyle['glutenfree'] = result.gluten_free
            lifestyle['ketogenic'] = result.ketogenic
            lifestyle['vegetarian'] = result.vegetarian
            lifestyle['vegan'] = result.vegan
            lifestyle['cheap'] = result.cheap
            lifestyle['dairyfree'] = result.dairy_free
            lifestyle['products'] = [x.id for x in result.products]
            lifestyle['recipes'] = [x.id for x in result.recipes]
            lifestyle['ingredients'] = [x.id for x in result.ingredients]
            lifestyles.append(lifestyle)
        everything[word] = lifestyles
    return everything

def listRecipe(pagenum, size=10, col='name', order='desc'):
    ''' returns a page of recipes '''
    results = Recipe.query.order_by(col + ' ' + order).paginate(page=pagenum, per_page=size)
    page = {'recipes': [], 'pagenum': pagenum, 'size': size, 'total': len(Recipe.query.all())}
    for result in results.items:
        recipe = {}
        recipe['id'] = result.id
        recipe['name'] = result.name
        recipe['img'] = result.img
        recipe['time'] = result.time
        recipe['ingredients'] = [x.id for x in result.ingredientlists]
        recipe['lifestyles'] = [x.id for x in result.lifestyles]
        recipe['servings'] = result.servings
        recipe['instructions'] = result.instructions
        page['recipes'].append(recipe)
    return page

def listIngredient(pagenum, size=10, col='name', order='desc'):
    ''' returns a page of ingredients '''
    results = Ingredient.query.order_by(col + ' ' + order).paginate(page=pagenum, per_page=size)
    page = {'ingredients': [], 'pagenum': pagenum, 'size': size, 'total': len(Ingredient.query.all())}
    for result in results.items:
        ingredient = {}
        ingredient['id'] = result.id
        ingredient['name'] = result.name
        ingredient['img'] = result.img
        ingredient['calories'] = result.calories
        ingredient['protein'] = result.protein
        ingredient['fat'] = result.fat
        ingredient['carbs'] = result.carbs
        ingredient['recipes'] = [x.recipe_id for x in result.ingredientlists]
        ingredient['lifestyles'] = [x.id for x in result.lifestyles]
        page['ingredients'].append(ingredient)
    return page

def listProduct(pagenum, size=10, col='name', order='desc'):
    ''' returns a page of products '''
    results = Product.query.order_by(col + ' ' + order).paginate(page=pagenum, per_page=size)
    page = {'products': [], 'pagenum': pagenum, 'size': size, 'total': len(Product.query.all())}
    for result in results.items:
        product = {}
        product['id'] = result.id
        product['name'] = result.name
        product['img'] = result.img
        product['calories'] = result.calories
        product['protein'] = result.protein
        product['fat'] = result.fat
        product['satfat'] = result.satfat
        product['transfat'] = result.transfat
        product['carbs'] = result.carbs
        product['sugar'] = result.sugar
        product['lifestyles'] = [x.id for x in result.lifestyles]
        product['servingsize'] = result.servingsize
        page['products'].append(product)
    return page

def listLifestyle(pagenum, size=10, col='name', order='desc'):
    ''' returns a page of lifestyles '''
    results = Lifestyle.query.order_by(col + ' ' + order).paginate(page=pagenum, per_page=size)
    page = {'lifestyles': [], 'pagenum': pagenum, 'size': size, 'total': len(Lifestyle.query.all())}
    for result in results.items:
        lifestyle = {}
        lifestyle['id'] = result.id
        lifestyle['name'] = result.name
        lifestyle['img'] = result.img
        lifestyle['description'] = result.description
        lifestyle['weightmanage'] = result.weight_management
        lifestyle['glutenfree'] = result.gluten_free
        lifestyle['ketogenic'] = result.ketogenic
        lifestyle['vegetarian'] = result.vegetarian
        lifestyle['vegan'] = result.vegan
        lifestyle['cheap'] = result.cheap
        lifestyle['dairyfree'] = result.dairy_free
        lifestyle['products'] = [x.id for x in result.products]
        lifestyle['recipes'] = [x.id for x in result.recipes]
        lifestyle['ingredients'] = [x.id for x in result.ingredients]
        page['lifestyles'].append(lifestyle)
    return page

def specRecipe(ids):
    ''' returns recipes based off ids '''
    recipes = {'recipes': []}
    if not ids:
        return recipes
    ids = ids.split(',')
    for num in ids:
        result = Recipe.query.filter_by(id=num).first()
        if not result:
            continue
        recipe = {}
        recipe['id'] = result.id
        recipe['name'] = result.name
        recipe['img'] = result.img
        recipe['time'] = result.time
        recipe['ingredients'] = [x.id for x in result.ingredientlists]
        recipe['lifestyles'] = [x.id for x in result.lifestyles]
        recipe['servings'] = result.servings
        recipe['instructions'] = result.instructions
        recipes['recipes'].append(recipe)
    return recipes

def specIngredient(ids):
    ''' returns ingredients based off ids '''
    ingredients = {'ingredients': []}
    if(not ids):
        return ingredients
    ids = ids.split(',')
    for num in ids:
        result = Ingredient.query.filter_by(id=num).first()
        if not result:
            continue
        ingredient = {}
        ingredient['id'] = result.id
        ingredient['name'] = result.name
        ingredient['img'] = result.img
        ingredient['calories'] = result.calories
        ingredient['protein'] = result.protein
        ingredient['fat'] = result.fat
        ingredient['carbs'] = result.carbs
        ingredient['recipes'] = [x.recipe_id for x in result.ingredientlists]
        ingredient['lifestyles'] = [x.id for x in result.lifestyles]
        ingredients['ingredients'].append(ingredient)
    return ingredients

def specProduct(ids):
    ''' returns products based off ids '''
    products = {'products': []}
    if(not ids):
        return products
    ids = ids.split(',')
    for num in ids:
        result = Product.query.filter_by(id=num).first()
        if not result:
            continue
        product = {}
        product['id'] = result.id
        product['name'] = result.name
        product['img'] = result.img
        product['calories'] = result.calories
        product['protein'] = result.protein
        product['fat'] = result.fat
        product['satfat'] = result.satfat
        product['transfat'] = result.transfat
        product['carbs'] = result.carbs
        product['sugar'] = result.sugar
        product['lifestyles'] = [x.id for x in result.lifestyles]
        product['servingsize'] = result.servingsize
        products['products'].append(product)
    return products

def specLifestyle(ids):
    ''' returns lifestyles based off ids '''
    lifestyles = {'lifestyles': []}
    if(not ids):
        return lifestyles
    ids = ids.split(',')
    for num in ids:
        result = Lifestyle.query.filter_by(id=num).first()
        if not result:
            continue
        lifestyle = {}
        lifestyle['id'] = result.id
        lifestyle['name'] = result.name
        lifestyle['img'] = result.img
        lifestyle['description'] = result.description
        lifestyle['weightmanage'] = result.weight_management
        lifestyle['glutenfree'] = result.gluten_free
        lifestyle['ketogenic'] = result.ketogenic
        lifestyle['vegetarian'] = result.vegetarian
        lifestyle['vegan'] = result.vegan
        lifestyle['cheap'] = result.cheap
        lifestyle['dairyfree'] = result.dairy_free
        lifestyle['products'] = [x.id for x in result.products]
        lifestyle['recipes'] = [x.id for x in result.recipes]
        lifestyle['ingredients'] = [x.id for x in result.ingredients]
        lifestyles['lifestyles'].append(lifestyle)
    return lifestyles

def specInglist(ids):
    ''' returns ingredient lists based off ids '''
    inglists = {'inglists': []}
    if(not ids):
        return inglists
    ids = ids.split(',')
    for num in ids:
        result = Ingredientlist.query.filter_by(id=num).first()
        if not result:
            continue
        inglist = {}
        inglist['id'] = result.id
        inglist['ingid'] = result.ingredient_id
        inglist['recid'] = result.recipe_id
        inglist['amount'] = result.amount
        inglist['unit'] = result.unit
        inglists['inglists'].append(inglist)
    return inglists
