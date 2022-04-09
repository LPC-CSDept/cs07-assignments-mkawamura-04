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
for i in range (n):
  row_sum=0
  for j in range (m):
    row_sum=row_sum+allScores[i][j]
  average=row_sum/m
  print ('Name: {0} Sum: {1} Average:     {2}'.format(nameList[i],row_sum,average))