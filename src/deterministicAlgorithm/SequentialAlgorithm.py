'''
Created on 27 mag 2018

@author: davideorlando
'''
from model.CQBroker import CQBroker
from model.Human import Human

human = Human()


class SequentialAlgorithm(object):
    
    def __init__(self):
        '''
        '''

    def resolve(self, crowdfindInstance):
        items = crowdfindInstance._items
        fasi = 0
        costo = 0
        while crowdfindInstance.verify() == False:
            CQ = CQBroker.getInstance().getQuestions(items, 1)
            if (CQ[0]._isEvaluated == 0) :
                h = CQ[0]
            h._valutations["cat"] = human.answer(h, "cat")
            h._isEvaluated = 1
            fasi = fasi + 1
            costo = costo + 1
            crowdfindInstance._prop2NumValues["cat"] = crowdfindInstance._prop2NumValues["cat"] + h._valutations["cat"]
        
        print("Il numero di fasi è stato:" + str(fasi))
        print("Il costo è stato:" + str(costo))

    
