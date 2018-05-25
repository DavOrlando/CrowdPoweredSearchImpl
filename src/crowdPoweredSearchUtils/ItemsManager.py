'''
Created on 25 mag 2018

@author: ciroliviero
'''

import model.Item as i

class ItemsManager(object):
    '''
    classdocs
    '''
    
    # Here will be the instance stored.
    _instance = None
    _items = []
    _itemId2realProperties = {}
    _itemId2valuations = {}
    
    
    def addItem(self,itemId,itemProperties,valuations):
        propertyName2value = {}
        for keyAndValue in itemProperties.split("&"):
            propertyName2value[keyAndValue.split(":")[0]] = keyAndValue.split(":")[1]
        newItem = i.Item(itemId,propertyName2value.keys())
        ItemsManager._items.append(newItem)
        ItemsManager._itemId2realProperties[itemId] = propertyName2value
    
    def getItems(self):
        return ItemsManager._items


    def getItemRealProperty(self,itemId,propertyName):
        return ItemsManager._itemId2realProperties[str(itemId)][propertyName]
    
    @staticmethod
    def getInstance():
        """ Static access method. """
        if ItemsManager._instance == None:
            ItemsManager()
        return ItemsManager._instance 



    def __init__(self):
        '''
        Constructor
        '''
        if ItemsManager._instance != None:
            raise Exception("This class is a singleton!")
        else:
            ItemsManager._instance = self
        