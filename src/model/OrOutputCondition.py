'''
Created on 24 mag 2018

@author: davideorlando
'''

class OrOutputCondition(object):
    '''
    Set of condition in and
    '''


    def __init__(self, conditions):
        '''
        Constructor
        '''
        self._conditions = conditions
        
    def verify(self,items):
        cond = False
        for condition in self._conditions:
            cond = condition.verify(items) or cond
            if (cond == True):
                return cond
        return cond