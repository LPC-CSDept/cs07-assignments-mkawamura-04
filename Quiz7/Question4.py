import xlrd
from functools import reduce
import pprint

workbook = xlrd.open_workbook('student.xls')
sheetNames = workbook.sheet_names()
sheetByIndex = workbook.sheet_by_index(0)

header = sheetByIndex.row_values(0)
header = list(filter(lambda cell: cell != '', header))

id = sheetByIndex.col_values(0, start_rowx=1)

name = sheetByIndex.col_values(1, start_rowx=1)

num_scores = sheetByIndex.nrows - 1
scores = []
for i in range(num_scores):
  score = sheetByIndex.row_values(i+1, start_colx=2)
  scores.append(score)

dictList = []
for pid in range(len(name)):
  record = []
  record.append(id[pid])
  record.append(name[pid])
  record.append(scores[pid])
  d = dict(zip(header, record))
  dictList.append(d)
pprint.pprint(dictList)

for d in dictList:
  print("{0: 0.0f} {1: <10} {2}".format(d['ID'], d['Name'], reduce(lambda x,y: x+y, d['Scores'])))