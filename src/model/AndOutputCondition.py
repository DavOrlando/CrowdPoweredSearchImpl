'''
Created on 24 mag 2018

@author: davideorlando
'''

class AndOutputCondition(object):
    '''
    Set of condition in and
    '''


    def __init__(self, conditions):
        '''
        Constructor
        '''
        self._conditions = conditions
        
    def verify(self,prop2NumValues):
        cond = True
        for condition in self._conditions:
            cond = condition.verify(prop2NumValues) and cond
            if (cond == False):
                return cond
        return cond