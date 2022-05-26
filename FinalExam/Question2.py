import random

countDict = {}
for i in range(10):
    n = random.randrange(0,5)
    print(n,end=' ')

    if n not in countDict:
        countDict[n]=1
    else:
        countDict[n]=countDict[n]+1

print()
sortedCountDict=dict(sorted(countDict.items(),key=lambda item:item[1],reverse=True))
print(sortedCountDict)

k=next(iter(sortedCountDict))
print("Answer: {0}({1} time(s) occurred)".format(k, sortedCountDict[k]))
