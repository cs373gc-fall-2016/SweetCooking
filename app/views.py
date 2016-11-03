from app import app, helpers
from flask import jsonify, request, render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/foodproducts', defaults={'page_id': -1})
@app.route('/foodproducts/<int:page_id>')
def foodproducts(page_id):
    this_id = page_id
    if(this_id == -1):
        return render_template('foodproducts.html')
    else:
        return render_template('foodproduct.html', id=this_id)

@app.route('/ingredients', defaults={'page_id': -1})
@app.route('/ingredients/<int:page_id>')
def ingredients(page_id):
    this_id = page_id
    if(this_id == -1):
        return render_template('ingredients.html')
    else:
        return render_template('ingredient.html', id=this_id)

@app.route('/lifestyles', defaults={'page_id': -1})
@app.route('/lifestyles/<int:page_id>')
def lifestyles(page_id):
    this_id = page_id
    if(this_id == -1):
        return render_template('lifestyles.html')
    else:
        return render_template('lifestyle.html', id=this_id)

@app.route('/recipes', defaults={'page_id': -1})
@app.route('/recipes/<int:page_id>')
def recipes(page_id):
    this_id = page_id
    if(this_id == -1):
        return render_template('recipes.html')
    else:
        return render_template('recipe.html', id=this_id)

@app.route('/oreo_product')
def oreo_product():
    return render_template('oreo_product.html')

@app.route('/peanutbutter_product')
def peanutbutter_product():
    return render_template('peanutbutter_product.html')

@app.route('/pizza')
def pizza():
    return render_template('pizza.html')

@app.route('/salt_ingredient')
def salt_ingredient():
    return render_template('salt_ingredient.html')

@app.route('/spaghetti_meatballs')
def spaghetti_meatballs():
    return render_template('spaghetti_meatballs.html')

@app.route('/sugar_ingredient')
def sugar_ingredient():
    return render_template('sugar_ingredient.html')

@app.route('/tomato_ingredient')
def tomato_ingredient():
    return render_template('tomato_ingredient.html')

@app.route('/tostito_product')
def tostito_product():
    return render_template('tostito_product.html')

@app.route('/weightloss_lifestyle')
def weightloss_lifestyle():
    return render_template('weightloss_lifestyle.html')

@app.route('/fit_lifestyle')
def fitness():
    return render_template('fit_lifestyle.html')

@app.route('/vegan_lifestyle')
def vegan():
    return render_template('vegan_lifestyle.html')

@app.route('/tomato_sauce_product')
def tomato_sauce():
    return render_template('tomato_sauce_product.html')

@app.route('/bbq_sauce_product')
def bbq_sauce():
    return render_template('bbq_sauce_product.html')

@app.route('/cheese_ingredient')
def cheese_ingredient():
    return render_template('cheese_ingredient.html')

@app.route('/onion_ingredient')
def onion():
    return render_template('onion_ingredient.html')

@app.route('/water_ingredient')
def water():
    return render_template('water_ingredient.html')

@app.route('/pasta_product')
def pasta():
    return render_template('pasta_product.html')

@app.route('/ground_beef_ingredient')
def ground_beef():
    return render_template('ground_beef_ingredient.html')

@app.route('/parmesan_cheese_ingredient')
def parmesan_cheese():
    return render_template('parmesan_cheese_ingredient.html')
