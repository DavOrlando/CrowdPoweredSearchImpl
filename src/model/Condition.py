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
        
    def verify(self,items):
        cont = 0
        for item in items:
            if(item._valutations[self._property] ==1):
                cont+=1
            if(cont>=self._numberRequested):
                return True
        return False 
        