from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/foodproducts')
@app.route('/foodproducts.html')
def foodproducts():
    return render_template('foodproducts.html')

@app.route('/ingredients')
@app.route('/ingredients.html')
def ingredients():
    return render_template('ingredients.html')

@app.route('/lifestyles')
@app.route('/lifestyles.html')
def lifestyles():
    return render_template('lifestyles.html')

@app.route('/recipes')
@app.route('/recipes.html')
def recipes():
    return render_template('recipes.html')

@app.route('/oreo_product')
@app.route('/oreo_product.html')
def oreo_product():
    return render_template('oreo_product.html')

@app.route('/peanutbutter_product')
@app.route('/peanutbutter_product.html')
def peanutbutter_product():
    return render_template('peanutbutter_product.html')

@app.route('/pizza')
@app.route('/pizza.html')
def pizza():
    return render_template('pizza.html')

@app.route('/salt_ingredient')
@app.route('/salt_ingredient.html')
def salt_ingredient():
    return render_template('salt_ingredient.html')

@app.route('/spaghetti_meatballs')
@app.route('/spaghetti_meatballs.html')
def spaghetti_meatballs():
    return render_template('spaghetti_meatballs.html')

@app.route('/sugar_ingredient')
@app.route('/sugar_ingredient.html')
def sugar_ingredient():
    return render_template('sugar_ingredient.html')

@app.route('/tomato_ingredient')
@app.route('/tomato_ingredient.html')
def tomato_ingredient():
    return render_template('tomato_ingredient.html')

@app.route('/tostito_product')
@app.route('/tostito_product.html')
def tostito_product():
    return render_template('tostito_product.html')

@app.route('/weightloss_lifestyle')
@app.route('/weightloss_lifestyle.html')
def weightloss_lifestyle():
    return render_template('weightloss_lifestyle.html')

@app.route('/sushi')
@app.route('/sushi.html')
def sushi():
    return render_template('sushi.html')

@app.route('/fit_lifestyle')
@app.route('/fit_lifestyle.html')
def fitness():
    return render_template('fit_lifestyle.html')

@app.route('/vegan_lifestyle')
@app.route('/vegan_lifestyle.html')
def vegan():
    return render_template('vegan_lifestyle.html')

@app.route('/tomato_sauce_product')
@app.route('/tomato_sauce_product.html')
def tomato_sauce():
    return render_template('tomato_sauce_product.html')

@app.route('/bbq_sauce_product')
@app.route('/bbq_sauce_product.html')
def bbq_sauce():
    return render_template('bbq_sauce_product.html')

@app.route('/cheese_ingredient')
@app.route('/cheese_ingredient.html')
def cheese_ingredient():
    return render_template('cheese_ingredient.html')

@app.route('/onion_ingredient')
@app.route('/onion_ingredient.html')
def onion():
    return render_template('onion_ingredient.html')

@app.route('/water_ingredient')
@app.route('/water_ingredient.html')
def water():
    return render_template('water_ingredient.html')

@app.route('/pasta_product')
@app.route('/pasta_product.html')
def pasta():
    return render_template('pasta_product.html')

@app.route('/ground_beef_ingredient')
@app.route('/ground_beef_ingredient.html')
def ground_beef():
    return render_template('ground_beef_ingredient.html')

@app.route('/parmesan_cheese_ingredient')
@app.route('/parmesan_cheese_ingredient.html')
def parmesan_cheese():
    return render_template('parmesan_cheese_ingredient.html')
