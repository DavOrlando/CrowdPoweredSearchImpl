'''
Created on 24 mag 2018

@author: davideorlando
'''

class CrowdfindInstance(object):
    '''
    A crowdfind instance of Crowdfind problem
    '''


    def __init__(self, items,outputCondition):
        '''
        Constructor
        '''
        self._items =items
        self._prop2NumValues ={}
        for prop in items._properties:
            self._prop2NumValues[prop] = 0
        self._outputCondition = outputCondition
        
        
    
    def verify(self):
        return self._outputCondition.verify();
            