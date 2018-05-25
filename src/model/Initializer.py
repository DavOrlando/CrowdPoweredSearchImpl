'''
Created on 25 mag 2018

@author: ciroliviero
'''

import csv
import crowdPoweredSearchUtils.ItemsManager as manager

if __name__ == '__main__':
    m = manager.ItemsManager.getInstance()
    with open('../../resources/dataset.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            m.addItem(row['id'],row['properties'],row['valuations'])
    
    items = m.getItems()
    for i in items:
        print(str(i))
    
    '''Esempio'''  
    print("item 5:" + m.getItemRealProperty(5,"cat"))