'''
Created on 24 mag 2018

@author: davideorlando
'''
import unittest
from model.Item import Item
from model.Condition import Condition
from model.OrOutputCondition import OrOutputCondition
from model.AndOutputCondition import AndOutputCondition

propGatto = "propGatto"
itemOne = "1"
properties = {propGatto};
item1 = Item(itemOne, properties)
simpleCondition = Condition(propGatto, 0)
setWithOneItem = {item1}


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def testVerifySimpleCondition_True(self):
        self.assertTrue(simpleCondition.verify(setWithOneItem))
        
    def testVerifySimpleCondition_False(self):
        self.assertFalse(simpleCondition.verify({}))
    
    def testVerifyAndOutputCondition_True(self):
        outputCond = AndOutputCondition({simpleCondition})
        self.assertTrue(outputCond.verify(setWithOneItem))

    def testVerifyAndOutputCondition_False(self):
        outputCond = AndOutputCondition({simpleCondition, Condition(propGatto, 5)})
        self.assertFalse(outputCond.verify(setWithOneItem))
    
    def testVerifyOrOutputCondition_True(self):
        outputCond = OrOutputCondition({simpleCondition, Condition(propGatto, 5)})
        self.assertTrue(outputCond.verify(setWithOneItem))
     
    def testVerifyOrOutputCondition_False(self):
        outputCond = OrOutputCondition({})
        self.assertFalse(outputCond.verify(setWithOneItem))    

           
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
