from functools import reduce
import pprint
toInt = lambda x: int(x.replace(",", ""))

def makeLists(fname, lists):
    f = open(fname)
    for line in f.readlines():
        record = line.split()
        for i in range(0, 4):
            lists[i].append(record[i + 1])

def makeDict(data, keyList, state, nameList, gender, numberList):
    for i in range(len(nameList)):
        valueList = [state, nameList[i], gender, numberList[i]]
        data.append(dict(zip(keyList, valueList)))

def buildData(data):
    camale = []
    cafemale = []
    camalenum = []
    cafemalenum = []
    flmale = []
    flfemale = []
    flmalenum = []
    flfemalenum = []
    makeLists("FinalExam/ca2021.txt", [camale, camalenum, cafemale, cafemalenum])
    makeLists("FinalExam/fl2021.txt", [flmale, flmalenum, flfemale, flfemalenum])

    dictKeys = ["state", "name", "gender", "number"]
    makeDict(dataList, dictKeys, "CA", camale, "male", camalenum)
    makeDict(dataList, dictKeys, "CA", cafemale, "female", cafemalenum)
    makeDict(dataList, dictKeys, "FL", flmale, "male", flmalenum)
    makeDict(dataList, dictKeys, "FL", flfemale, "female", flfemalenum)

def getTopRecords(data, criteria, num):
    records = list(filter(criteria, data))
    records = sorted(records, key=lambda x: toInt(x['number']), reverse=True)
    return records[:num]

def getAccNum(data):
    records = getTopRecords(
        data, lambda r: r['gender'] == 'female' and r['state'] == 'FL', 10)
    sumNum = lambda x, y: x + toInt(y['number'])
    return reduce(sumNum, records, 0)

dataList = []
buildData(dataList)

print("Top 10 names for California Male: ")
pprint.pprint(getTopRecords(dataList,lambda \
r:r['gender']=='male' and \
r['state']=='CA',10))

print("Top 10 names Florida Women that starts with 'E': ")
pprint.pprint(getTopRecords(dataList,lambda r:r['gender']=='female' \
                            and r['name'].startswith('E') \
                            and r['state']=='FL',10))

pprint.pprint("Top 10 names for Florida Women Total Number: {0}".format(
    getAccNum(dataList)))
