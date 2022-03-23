n=input("Number of Students: ")
m=input('Number of Scores: ')
scoreList=[]
allScore=[]
names=input('Names of Students: ')
nameList=names.split(' ')
print (nameList)
for i in range (int(n)):
  for x in range (int(m)):
    scores=input('Score')
    scoreList=scores.split(' ')
    for x in range (len(scoreList)):
      scoreList[m]=int(scoreList[m])
    allScore.append(scoreList)

