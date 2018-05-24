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
        if len(items) != 0:
            for prop in list(items)[0]._properties:
                self._prop2NumValues[prop] = 0
        self._outputCondition = outputCondition
        
        
    
    def verify(self):
        return self._outputCondition.verify(self._prop2NumValues);
            
