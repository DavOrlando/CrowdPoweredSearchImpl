'''
Created on 25 mag 2018

@author: ciroliviero
'''


class CQBroker(object):
    '''
    classdocs
    '''
    
    # Here will be the instance stored.
    _instance = None
    _lastItemForQuestion=0
    
    def getQuestions(self, items, numberOfQuestion):
        try:
            listItems = items[CQBroker._lastItemForQuestion:CQBroker._lastItemForQuestion+numberOfQuestion]
            CQBroker._lastItemForQuestion=CQBroker._lastItemForQuestion+numberOfQuestion
            return listItems
        except:
            return items[CQBroker._lastItemForQuestion:]
    
    
    @staticmethod
    def getInstance():
        """ Static access method. """
        if CQBroker._instance == None:
            CQBroker()
        return CQBroker._instance 



    def __init__(self):
        '''
        Constructor
        '''
        if CQBroker._instance != None:
            raise Exception("This class is a singleton!")
        else:
            CQBroker._instance = self
        