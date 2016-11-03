#!/usr/bin/envalpython3

# -------
# imports
# -------
import unittest
from app.helpers import *
from app.models import *
from unittest import main, TestCase

# ----------------
# TestIngredient
# ----------------
class TestIngredient(TestCase):

    def test_searchall_and(self):
        ''' testing for and '''
        result = searchAll('a e i o u')
        self.assertTrue('and' in result)
        
    def test_searchall_or(self):
        ''' testing for or '''
        result = searchAll('a e i o u')
        self.assertTrue('or' in result)
        
    def test_searchall_empty(self):
        ''' testing for empty string '''
        result = searchAll('a e i o u')
        assert('and' in result and 'or' in result)
        for pillar in result['and']:
            self.assertTrue(len(pillar) > 0)
        for pillar in result['or']:
            self.assertTrue(len(pillar) > 0)
        
    def test_searchrecipes_and(self):
        ''' testing for and '''
        result = searchRecipes('a e i o u')
        self.assertTrue('and' in result)
        
    def test_searchrecipes_or(self):
        ''' testing for or '''
        result = searchRecipes('a e i o u')
        self.assertTrue('or' in result)
        
    def test_searchrecipes_empty(self):
        ''' testing for empty string '''
        result = searchRecipes('a e i o u')
        assert('and' in result and 'or' in result)
        for pillar in result['and']:
            self.assertTrue(len(pillar) > 0)
        for pillar in result['or']:
            self.assertTrue(len(pillar) > 0)
        
    def test_searchingredients_and(self):
        ''' testing for and '''
        result = searchIngredients('a e i o u')
        self.assertTrue('and' in result)

    def test_searchingredients_or(self):
        ''' testing for or '''
        result = searchIngredients('a e i o u')
        self.assertTrue('or' in result)

    def test_searchingredients_empty(self):
        ''' testing for empty string '''
        result = searchIngredients('a e i o u')
        assert('and' in result and 'or' in result)
        for pillar in result['and']:
            self.assertTrue(len(pillar) > 0)
        for pillar in result['or']:
            self.assertTrue(len(pillar) > 0)

    def test_searchproducts_and(self):
        ''' testing for and '''
        result = searchProducts('a e i o u')
        self.assertTrue('and' in result)

    def test_searchproducts_or(self):
        ''' testing for or '''
        result = searchProducts('a e i o u')
        self.assertTrue('or' in result)

    def test_searchproducts_empty(self):
        ''' testing for empty string '''
        result = searchProducts('a e i o u')
        assert('and' in result and 'or' in result)
        for pillar in result['and']:
            self.assertTrue(len(pillar) > 0)
        for pillar in result['or']:
            self.assertTrue(len(pillar) > 0)

    def test_searchlifestyles_and(self):
        ''' testing for and '''
        result = searchLifestyles('a e i o u')
        self.assertTrue('and' in result)

    def test_searchlifestyles_or(self):
        ''' testing for or '''
        result = searchLifestyles('a e i o u')
        self.assertTrue('or' in result)

    def test_searchlifestyles_empty(self):
        ''' testing for empty string '''
        result = searchLifestyles('a e i o u')
        assert('and' in result and 'or' in result)
        for pillar in result['and']:
            self.assertTrue(len(pillar) > 0)
        for pillar in result['or']:
            self.assertTrue(len(pillar) > 0)

    def test_andrecipes_empty(self):
        ''' testing for empty string '''
        result = andRecipes('')
        self.assertTrue(len(result) > 0)

    def test_andrecipes_none(self):
        ''' testing for no results '''
        result = andRecipes('thisshoulddefinitelynotreturnanything')
        self.assertEqual(len(result), 0)

    def test_andrecipes_result(self):
        ''' testing for regular results '''
        result = andRecipes('a')
        self.assertTrue(len(result) > 0)

    def test_orrecipes_empty(self):
        ''' testing for empty string '''
        result = orRecipes([''])
        self.assertTrue(len(result) > 0)

    def test_orrecipes_none(self):
        ''' testing for no results '''
        termstring = 'thisshoulddefinitelynotreturnanything'
        result = orRecipes([termstring])
        result = result[termstring]
        self.assertEqual(len(result), 0)

    def test_orrecipes_result(self):
        ''' testing for regular results '''
        result = orRecipes(['a'])
        self.assertTrue(len(result) > 0)

    def test_andingredients_empty(self):
        ''' testing for empty string '''
        result = andIngredients('')
        self.assertTrue(len(result) > 0)

    def test_andingredients_none(self):
        ''' testing for no results '''
        result = andIngredients('thisshoulddefinitelynotreturnanything')
        self.assertEqual(len(result), 0)

    def test_andingredients_result(self):
        ''' testing for regular results '''
        result = andIngredients('a')
        self.assertTrue(len(result) > 0)

    def test_oringredients_empty(self):
        ''' testing for empty string '''
        result = orIngredients([''])
        self.assertTrue(len(result) > 0)

    def test_oringredients_none(self):
        ''' testing for no results '''
        termstring = 'thisshoulddefinitelynotreturnanything'
        result = orIngredients([termstring])
        result = result[termstring]
        self.assertEqual(len(result), 0)

    def test_oringredients_result(self):
        ''' testing for regular results '''
        result = orIngredients(['a'])
        self.assertTrue(len(result) > 0)

    def test_andproducts_empty(self):
        ''' testing for empty string '''
        result = andProducts('')
        self.assertTrue(len(result) > 0)

    def test_andproducts_none(self):
        ''' testing for no results '''
        result = andProducts('thisshoulddefinitelynotreturnanything')
        self.assertEqual(len(result), 0)

    def test_andproducts_result(self):
        ''' testing for regular results '''
        result = andProducts('a')
        self.assertTrue(len(result) > 0)

    def test_orproducts_empty(self):
        ''' testing for empty string '''
        result = orProducts([''])
        self.assertTrue(len(result) > 0)

    def test_orproducts_none(self):
        ''' testing for no results '''
        termstring = 'thisshoulddefinitelynotreturnanything'
        result = orProducts([termstring])
        result = result[termstring]
        self.assertEqual(len(result), 0)

    def test_orproducts_result(self):
        ''' testing for regular results '''
        result = orProducts(['a'])
        self.assertTrue(len(result) > 0)

    def test_andlifestyles_empty(self):
        ''' testing for empty string '''
        result = andLifestyles('')
        self.assertTrue(len(result) > 0)

    def test_andlifestyles_none(self):
        ''' testing for no results '''
        result = andLifestyles('thisshoulddefinitelynotreturnanything')
        self.assertEqual(len(result), 0)

    def test_andlifestyles_result(self):
        ''' testing for regular results '''
        result = andLifestyles('a')
        self.assertTrue(len(result) > 0)

    def test_orlifestyles_empty(self):
        ''' testing for empty string '''
        result = orLifestyles([''])
        self.assertTrue(len(result) > 0)

    def test_orlifestyles_none(self):
        ''' testing for no results '''
        termstring = 'thisshoulddefinitelynotreturnanything'
        result = orLifestyles([termstring])
        result = result[termstring]
        self.assertEqual(len(result), 0)

    def test_orlifestyles_result(self):
        ''' testing for regular results '''
        result = orLifestyles(['a'])
        self.assertTrue(len(result) > 0)

    def test_listRecipe_pagesize(self):
        ''' testing size of pages returned '''
        result = listRecipe(1, size=20)
        self.assertEqual(len(result['recipes']), 20)
        self.assertEqual(result['size'], 20)

    def test_listRecipe_ascending(self):
        ''' testing ascending sort '''
        result1 = listRecipe(1, size=1, order='asc')
        result1 = result1['recipes'][0]['name']
        result2 = listRecipe(2, size=1, order='asc')
        result2 = result2['recipes'][0]['name']
        self.assertTrue(result1 < result2)

    def test_listRecipe_descending(self):
        ''' testing ascending sort '''
        result1 = listRecipe(1, size=1, order='desc')
        result1 = result1['recipes'][0]['name']
        result2 = listRecipe(2, size=1, order='desc')
        result2 = result2['recipes'][0]['name']
        self.assertTrue(result1 > result2)

    def test_listIngredient_pagesize(self):
        ''' testing size of pages returned '''
        result = listIngredient(1, size=20)
        self.assertEqual(len(result['ingredients']), 20)
        self.assertEqual(result['size'], 20)

    def test_listIngredient_ascending(self):
        ''' testing ascending sort '''
        result1 = listIngredient(1, size=1, order='asc')
        result1 = result1['ingredients'][0]['name']
        result2 = listIngredient(2, size=1, order='asc')
        result2 = result2['ingredients'][0]['name']
        self.assertTrue(result1 < result2)

    def test_listIngredient_descending(self):
        ''' testing ascending sort '''
        result1 = listIngredient(1, size=1, order='desc')
        result1 = result1['ingredients'][0]['name']
        result2 = listIngredient(2, size=1, order='desc')
        result2 = result2['ingredients'][0]['name']
        self.assertTrue(result1 > result2)

    def test_listProduct_pagesize(self):
        ''' testing size of pages returned '''
        result = listProduct(1, size=20)
        self.assertEqual(len(result['products']), 20)
        self.assertEqual(result['size'], 20)

    def test_listProduct_ascending(self):
        ''' testing ascending sort '''
        result1 = listProduct(1, size=1, order='asc')
        result1 = result1['products'][0]['name']
        result2 = listProduct(50, size=1, order='asc')
        result2 = result2['products'][0]['name']
        self.assertTrue(result1 < result2)

    def test_listProduct_descending(self):
        ''' testing ascending sort '''
        result1 = listProduct(1, size=1, order='desc')
        result1 = result1['products'][0]['name']
        result2 = listProduct(50, size=1, order='desc')
        result2 = result2['products'][0]['name']
        self.assertTrue(result1 > result2)

    def test_listLifestyle_pagesize(self):
        ''' testing size of pages returned '''
        result = listLifestyle(1, size=5)
        self.assertEqual(len(result['lifestyles']), 5)
        self.assertEqual(result['size'], 5)

    def test_listLifestyle_ascending(self):
        ''' testing ascending sort '''
        result1 = listLifestyle(1, size=1, order='asc')
        result1 = result1['lifestyles'][0]['name']
        result2 = listLifestyle(2, size=1, order='asc')
        result2 = result2['lifestyles'][0]['name']
        self.assertTrue(result1 < result2)

    def test_listLifestyle_descending(self):
        ''' testing ascending sort '''
        result1 = listLifestyle(1, size=1, order='desc')
        result1 = result1['lifestyles'][0]['name']
        result2 = listLifestyle(2, size=1, order='desc')
        result2 = result2['lifestyles'][0]['name']
        self.assertTrue(result1 > result2)

    def test_specrecipe_noid(self):
        ''' testing no ids passed in '''
        result = specRecipe('')
        self.assertFalse(result['recipes'])

    def test_specrecipe_1id(self):
        ''' testing one id '''
        expected = Recipe.query.limit(2).first()
        actual = specRecipe(str(expected.id))
        self.assertEqual(len(actual['recipes']), 1)
        actual = actual['recipes'][0]
        self.assertEqual(expected.id, actual['id'])
        self.assertEqual(expected.name, actual['name'])

    def test_specrecipe_2ids(self):
        ''' testing two ids '''
        expected = [x for x in Recipe.query.limit(2).all()]
        actual = specRecipe(str(expected[0].id) + ',' + str(expected[1].id))
        self.assertEqual(len(actual['recipes']), 2)
        for x in range(2):
            self.assertEqual(expected[x].id,  actual['recipes'][x]['id'])
            self.assertEqual(expected[x].name,  actual['recipes'][x]['name'])

    def test_specproduct_noid(self):
        ''' testing no ids passed in '''
        result = specProduct('')
        self.assertFalse(result['products'])

    def test_specproduct_1id(self):
        ''' testing one id '''
        expected = Product.query.limit(2).first()
        actual = specProduct(str(expected.id))
        self.assertEqual(len(actual['products']), 1)
        actual = actual['products'][0]
        self.assertEqual(expected.id, actual['id'])
        self.assertEqual(expected.name, actual['name'])

    def test_specproduct_2ids(self):
        ''' testing two ids '''
        expected = [x for x in Product.query.limit(2).all()]
        actual = specProduct(str(expected[0].id) + ',' + str(expected[1].id))
        self.assertEqual(len(actual['products']), 2)
        for x in range(2):
            self.assertEqual(expected[x].id,  actual['products'][x]['id'])
            self.assertEqual(expected[x].name,  actual['products'][x]['name'])

    def test_specingredient_noid(self):
        ''' testing no ids passed in '''
        result = specIngredient('')
        self.assertFalse(result['ingredients'])

    def test_specingredient_1id(self):
        ''' testing one id '''
        expected = Ingredient.query.limit(2).first()
        actual = specIngredient(str(expected.id))
        self.assertEqual(len(actual['ingredients']), 1)
        actual = actual['ingredients'][0]
        self.assertEqual(expected.id, actual['id'])
        self.assertEqual(expected.name, actual['name'])

    def test_specingredient_2ids(self):
        ''' testing two ids '''
        expected = [x for x in Ingredient.query.limit(2).all()]
        actual = specIngredient(str(expected[0].id) + ',' + str(expected[1].id))
        self.assertEqual(len(actual['ingredients']), 2)
        for x in range(2):
            self.assertEqual(expected[x].id,  actual['ingredients'][x]['id'])
            self.assertEqual(expected[x].name,  actual['ingredients'][x]['name'])

    def test_speclifestyle_noid(self):
        ''' testing no ids passed in '''
        result = specLifestyle('')
        self.assertFalse(result['lifestyles'])

    def test_speclifestyle_1id(self):
        ''' testing one id '''
        expected = Lifestyle.query.limit(2).first()
        actual = specLifestyle(str(expected.id))
        self.assertEqual(len(actual['lifestyles']), 1)
        actual = actual['lifestyles'][0]
        self.assertEqual(expected.id, actual['id'])
        self.assertEqual(expected.name, actual['name'])

    def test_speclifestyle_2ids(self):
        ''' testing two ids '''
        expected = [x for x in Lifestyle.query.limit(2).all()]
        actual = specLifestyle(str(expected[0].id) + ',' + str(expected[1].id))
        self.assertEqual(len(actual['lifestyles']), 2)
        for x in range(2):
            self.assertEqual(expected[x].id,  actual['lifestyles'][x]['id'])
            self.assertEqual(expected[x].name,  actual['lifestyles'][x]['name'])

    def test_specinglist_noid(self):
        ''' testing no ids passed in '''
        result = specInglist('')
        self.assertFalse(result['inglists'])

    def test_specinglist_1id(self):
        ''' testing one id '''
        expected = Ingredientlist.query.limit(2).first()
        actual = specInglist(str(expected.id))
        self.assertEqual(len(actual['inglists']), 1)
        actual = actual['inglists'][0]
        self.assertEqual(expected.id, actual['id'])

    def test_specinglist_2ids(self):
        ''' testing two ids '''
        expected = [x for x in Ingredientlist.query.limit(2).all()]
        #expected = [expected[0], expected[1]]
        actual = specInglist(str(expected[0].id) + ',' + str(expected[1].id))
        self.assertEqual(len(actual['inglists']), 2)
        for x in range(2):
            self.assertEqual(expected[x].id,  actual['inglists'][x]['id'])

# ----
# main
# ----
if __name__ == "__main__":
    main()
