""" Sweet Cooking Team Fall 2016 Test Harness """
#!/usr/bin/envalpython3

# -------
# imports
# -------
import pickle
import urllib.request
from io import StringIO
from unittest import main, TestCase


# ----------------
# TestSweetCooking
# ----------------
class TestSweetCooking(TestCase):
    """ test Sweet Cooking """

    # # -----
    # # Query
    # # -----
    def test_query_1(self):
        """ test query look up """
        # qeury pizza and make sure name has pizza in name
        # self.assertEqual(rmse(list1, list2), 1.00)
        
    def test_query_2(self):
        """ test query look up """
        # qeury taco and taco in name should pop up
        # self.assertEqual(rmse(list1, list2), 1.00)
        
    def test_query_3(self):
        """ test query look up """
        # qeury chips and chips in name should pop up
        # self.assertEqual(rmse(list1, list2), 1.00)
        
    # # ----
    # # Gram_to_cup
    # # ----
    def test_gram_to_cup_1(self):
        """ test gram to cup conversion """
        self.assertEqual(gram_to_cup(118.29), 0.5)
        
    def test_gram_to_cup_2(self):
        """ test gram to cup conversion """
        self.assertEqual(gram_to_cup(244), 1)
        
    def test_gram_to_cup_3(self):
        """ test gram to cup conversion """
        self.assertEqual(gram_to_cup(93.75), 0.75)
        
    # # ----
    # # Cup_to_gram
    # # ----
    def test_cup_to_gram_1(self):
        """ test gram to cup conversion """
        self.assertEqual(cup_to_gram(118.29), 0.5)
        
    def test_cup_to_gram_2(self):
        """ test gram to cup conversion """
        self.assertEqual(cup_to_gram(244), 1)
        
    def test_cup_to_gram_3(self):
        """ test gram to cup conversion """
        self.assertEqual(cup_to_gram(93.75), 0.75)
        
        
        


   


# ----
# main
# ----
if __name__ == "__main__":
    main()
