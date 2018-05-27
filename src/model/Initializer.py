'''
Created on 25 mag 2018

@author: ciroliviero
'''

import csv
import miscellaneous.ItemsManager as manager
from model.CrowdfindInstance import CrowdfindInstance
from model.Condition import Condition
from deterministicAlgorithm.SequentialAlgorithm import SequentialAlgorithm
from deterministicAlgorithm.OptCostMaxParallelismAlgorithm import OptCostMaxParallelismAlgorithm
from deterministicAlgorithm.AlfaMultApproxAlgorithm import AlfaMultApproxAlgorithm
from deterministicAlgorithm.AlfaAddApproxAlgorithm import AlfaAddApproxAlgorithm

if __name__ == '__main__':
    m = manager.ItemsManager.getInstance()
    with open('../../resources/dataset.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            m.addItem(row['id'],row['properties'],row['valuations'])
    
    items = m.getItems()
    AlfaAddApproxAlgorithm().resolve(CrowdfindInstance(items, Condition("cat",10)),2)