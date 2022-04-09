n=int(input("Number of Students: "))
m=int(input('Number of Scores: '))
names=input('Names of Students: ')
nameList=names.split(' ')
scoreList=[]
allScores=[]
for i in range (n):
  scores=input('Score: ')
  scoreList=scores.split(' ')
  for x in range (len(scoreList)):
      scoreList[x]=int(scoreList[x])
  allScores.append(scoreList)
print(allScores)