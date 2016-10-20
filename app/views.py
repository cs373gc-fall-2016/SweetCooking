from app import app

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/foodproducts')
def foodproducts():
    return render_template('foodproducts.html')

@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')

@app.route('/lifestyles')
def lifestyles():
    return render_template('lifestyles.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

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
