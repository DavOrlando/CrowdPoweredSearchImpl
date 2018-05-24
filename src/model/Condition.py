'''
Created on 24 mag 2018

@author: davideorlando
'''

class Condition(object):
    '''
    A condition for evaluate the set of item 
    '''


    def __init__(self, property,numberRequested):
        self._property = property
        self._numberRequested = numberRequested
        
    def verify(self,prop2NumValues):
        if(len(prop2NumValues) == 0):
            return False;
        try:
            return prop2NumValues[self._property] >=self._numberRequested
        except Exception:
            print("An error occurred during condition verify!")
            return False;