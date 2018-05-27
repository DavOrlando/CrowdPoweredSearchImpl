'''
Created on 27 mag 2018

@author: davideorlando
'''
from model.CQBroker import CQBroker
from model.Human import Human

human = Human()


class AlfaAddApproxAlgorithm(object):
    
    def __init__(self):
        '''
        '''

    def resolve(self, crowdfindInstance,alfa):
        items = crowdfindInstance._items
        fasi = 0
        costo = 0
        valoriTrovati = 0;
        while crowdfindInstance.verify() == False:
            numOfQuestions = crowdfindInstance._outputCondition._numberRequested - valoriTrovati + alfa
            CQ = CQBroker.getInstance().getQuestions(items, numOfQuestions)
            for question in CQ:
                question._valutations["cat"] = human.answer(question, "cat")
                question._isEvaluated = 1
                costo = costo + 1
                crowdfindInstance._prop2NumValues["cat"] = crowdfindInstance._prop2NumValues["cat"] + question._valutations["cat"]
                valoriTrovati = valoriTrovati + question._valutations["cat"]
            fasi = fasi + 1
        print("Il numero di fasi è stato:" + str(fasi))
        print("Il costo è stato:" + str(costo))
    
