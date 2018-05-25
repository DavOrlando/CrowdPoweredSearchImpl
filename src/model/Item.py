'''
Created on 24 mag 2018

@author: davideorlando
'''

class Item(object):
    '''
    Item with properties that will be valuated by humans
    in a crowdsourcing context.
    '''


    def __init__(self, id,properties):
        '''
        Initialize a new Item with an id, a set of properties 
        and valutations for his properties
        '''
        self._id = id
        self._properties = properties
        self._valutations = {}
        for prop in self._properties:
            self._valutations[prop] = -1;
     
    
    def evaluated(self,property):
        return self._valutations[property]!=-1;   
    
    def setValueProp(self,property,value):
        self._valutations[property] = value; 
        
    def __str__(self, *args, **kwargs):
        return str("[id: "+self._id+", properties: "+str(self._properties)+"]");