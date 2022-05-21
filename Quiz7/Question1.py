import xlrd
workbook = xlrd.open_workbook('student.xls')
sheetNames = workbook.sheet_names()
sheetByIndex = workbook.sheet_by_index(0)
header = sheetByIndex.row_values(0)
header = list(filter(lambda cell: cell != '', header))
print(header)
id = sheetByIndex.col_values(0, start_rowx=1)
print(id)
name = sheetByIndex.col_values(1, start_rowx=1)
print(name)
num_scores = sheetByIndex.ncols - 2
scores = []
for i in range(num_scores):
    score = sheetByIndex.row_values(i+2, start_colx=2)
    scores.append(score)
print(scores)


dictionary=dict(zip(header,record))
for zipval dictionary 
print (dictionary)
"""highScore = lambda l: filter(lambda n: n>280, l)
result=highScore(totalscore)
print (total score data)
from functool import reduce
functools.reduce(lambda sheetByIndex: id,name,total score,)"""
