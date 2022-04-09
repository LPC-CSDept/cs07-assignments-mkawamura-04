n=int(input("Number of Students: "))
m=int(input('Number of Scores: '))
names=input('Names of Students: ')
nameList=names.split(' ')
scoreList=[]
allScores=[]

print (nameList)
for i in range (n):
  for j in range (m):
    scores=input('Score')
    scoreList=scores.split(' ')
    for x in range (len(scoreList)):
      scoreList[x]=int(scoreList[x])
    allScores.append(scoreList)