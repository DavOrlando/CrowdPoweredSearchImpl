'''
Created on 24 mag 2018

@author: davideorlando
'''
import unittest
from model.Item import Item
from model.Condition import Condition
from model.OrOutputCondition import OrOutputCondition
from model.AndOutputCondition import AndOutputCondition

simpleCondition = Condition("gatto", 0)
fConGattoZero = {"gatto":0}

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def testVerifySimpleCondition_True(self):
        self.assertTrue(simpleCondition.verify(fConGattoZero))
        
         
    def testVerifySimpleCondition_False(self):
        self.assertFalse(simpleCondition.verify({}))
     
    def testVerifyAndOutputCondition_True(self):
        outputCond = AndOutputCondition({simpleCondition, simpleCondition})
        self.assertTrue(outputCond.verify(fConGattoZero))
  
    def testVerifyAndOutputCondition_False(self):
        outputCond = AndOutputCondition({simpleCondition, Condition("gatto", 5)})
        self.assertFalse(outputCond.verify(fConGattoZero))
     
    def testVerifyOrOutputCondition_True(self):
        outputCond = OrOutputCondition({simpleCondition, Condition("gatto", 5)})
        self.assertTrue(outputCond.verify(fConGattoZero))
      
    def testVerifyOrOutputCondition_False(self):
        outputCond = OrOutputCondition({})
        self.assertFalse(outputCond.verify({}))    

           
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
