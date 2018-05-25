'''
Created on 25 mag 2018

@author: ciroliviero
'''

'''
This module creates in resources folder a CSV dataset named dataset.csv and structured as follows:
each row in CSV dataset contains id,properties,valuations.
- id is the item's id (it's equal to row number)
- properties is a list of couples <propertyName,propertyValue> containing the real values of the item
(for example cat:1&color:2)
- valuations is a list of couples <humanId,listOfProperties> containing examples of humans' answers
in the case of uncertain setting (for example 001-cat:0&color:2+002-cat:1&color:2+...)
'''

import os

HEADER = "id,properties,valuations"
OUTPUT_FILE = "../../resources/dataset.csv"
TRUE_CATS_IMAGES= [0,5,10,11,12,13,20,22,24,49]

def alwaysRightHumanBehaviour(listOfProperties):
    valuations = ""
    for x in listOfProperties:
        valuations = valuations + x + "&"
    return valuations[:-1]

def alwaysWrongHumanBehaviour(listOfProperties):
    valuations = ""
    for x in listOfProperties:
        name = x.split(":")[0]
        value = x.split(":")[1]
        valuations = valuations + name + ":" + str(1-int(value)) + "&"
    return valuations[:-1]

def spammerBehaviour(listOfProperties):
    valuations = ""
    for x in listOfProperties:
        name = x.split(":")[0]
        valuations = valuations + name + ":1" + "&"
    return valuations[:-1]

def goodHumanBehaviour(itemId,listOfProperties):
    valuations = ""
    for x in listOfProperties:
        name = x.split(":")[0]
        value = x.split(":")[1]
        if(itemId%5>3):
            value = str(1-int(value))
        valuations = valuations + name + ":" + value + "&"
    return valuations[:-1]
    

def quiteGoodHumanBehaviour(itemId,listOfProperties):
    valuations = ""
    for x in listOfProperties:
        name = x.split(":")[0]
        value = x.split(":")[1]
        if(itemId%5>2):
            value = str(1-int(value))
        valuations = valuations + name + ":" + value + "&"
    return valuations[:-1]


'''
By design:
- humans 0,5,10... always answer in the correct way according to the value assigned to properties
- humans 1,6,11... always answer in the wrong way according to the value assigned to properties
- humans 2,7,12... are spammer and they always answer 1
- humans 3,8,13... answer in the right way 4 times out of 5
- humans 4,9,14... answer in the right way 3 times out of 5
'''
def getValuationsForProperties(itemId,properties):
    row = ""
    for y in range(0,15):
        if(y%5==0):
            valuations = alwaysRightHumanBehaviour(properties)
        elif(y%5==1):
            valuations = alwaysWrongHumanBehaviour(properties)
        elif(y%5==2):
            valuations = spammerBehaviour(properties)
        elif(y%5==3):
            valuations = goodHumanBehaviour(itemId,properties)
        else:
            valuations = quiteGoodHumanBehaviour(itemId,properties)
        row = row + str(y) + "-" + valuations + "+"
    print("Valuation for item: " + str(itemId) + " with properties " + str(properties) + " are "+ row[:-1])
    return row[:-1]

if __name__ == '__main__':
    if(os.path.exists(OUTPUT_FILE)):
        os.remove(OUTPUT_FILE)
        print("Removed: "+OUTPUT_FILE)
    dataset = open(OUTPUT_FILE,"w")
    print("Created empty file: "+OUTPUT_FILE)
    dataset.write(HEADER+"\n")
    for x in range(0, 50):
        if(x in TRUE_CATS_IMAGES):
            row = str(x)+",cat:1,"+getValuationsForProperties(x,["cat:1"])
        else:
            row = str(x)+",cat:0,"+getValuationsForProperties(x,["cat:0"])
        dataset.write(row+"\n")
    dataset.close()
    print("File closed: "+OUTPUT_FILE)
    
