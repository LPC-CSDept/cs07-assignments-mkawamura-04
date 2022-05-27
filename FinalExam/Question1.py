from functools import reduce

toInt=lambda x:int(x.replace(",",""))

def makeLists(fname,lists):
    f=open(fname)
    for line in f.readlines():
        record=line.split()
        for i in range(0,4):
            lists[i].append(record[i+1])
          
def makeDict(data,keyList,state,nameList,gender,numberList):
    for i in range(len(nameList)):
        valueList=[state,nameList[i],gender,numberList[i]]
        data.append(dict(zip(keyList,valueList)))

def buildData(data):
    camale=[]
    cafemale=[]
    camalenum=[]
    cafemalenum=[]
    flmale=[]
    flfemale=[]
    flmalenum=[]
    flfemalenum=[]
    makeLists("ca2021.txt",[camale,camalenum,cafemale,cafemalenum])
    makeLists("fl2021.txt",[flmale,flmalenum,flfemale,flfemalenum])
