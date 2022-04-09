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
for i in range (n):
  row_sum=0
  for j in range (m):
    row_sum=row_sum+allScores[i][j]
  average=row_sum/m
  print ('Name:{0}, Sum:{1}, Average:   {2}'.format(nameList[i],row_sum,average))
for j in range (m):
  column_sum=0
  for i in range (n):
    column_sum=column_sum+allScores[i][j]
  average=column_sum/n
  print ('Subject Number:{0}, Subject Sum: {1}, Subject Average:{2}'.format(j+1,column_sum,average))