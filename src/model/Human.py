'''
Created on 27 mag 2018

@author: davideorlando
'''
from miscellaneous.ItemsManager import ItemsManager

class Human(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def answer(self, item,propertyName):
        return ItemsManager.getInstance().getItemRealProperty(item._id, propertyName)