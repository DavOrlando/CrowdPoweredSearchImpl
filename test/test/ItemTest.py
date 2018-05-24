'''
Created on 24 mag 2018

@author: davideorlando
'''
import unittest
from model.Item import Item
from unittest.test.test_assertions import Test_Assertions

propGatto = "propGatto"
itemOne = "1"
properties = {propGatto};
item1=Item(itemOne, properties)


def resetProp(itemOne):
    for prop in itemOne._properties:
        itemOne._valutations[prop] = -1


class Test(unittest.TestCase):
    

    def setUp(self):
        pass

    def tearDown(self):
        resetProp(item1)


    def testItemCreation(self):
        self.assertEqual(itemOne, str(item1))
    
    def testItemCreation_evaluatedFalse(self):
        self.assertFalse(item1.evaluated(propGatto))
    
    def testItemCreation_evaluatedTrueWithValueOne(self):
        item1.setValueProp(propGatto, 1);
        self.assertTrue(item1.evaluated(propGatto))
    
    def testItemCreation_evaluatedTrueWithValueZero(self):
        item1.setValueProp(propGatto, 0);
        self.assertTrue(item1.evaluated(propGatto))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()