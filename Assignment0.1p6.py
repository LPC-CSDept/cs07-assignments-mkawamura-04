import xlrd

wb = xlrd.open_workbook('SampleSuperStore.xls')
ws = wb.sheet_by_index(0)

listrows = []
for row in range(5):
  listrows.append(ws.row_values(row))
print(listrows)

import pandas as pd
df = pd.read_excel('SampleSuperStore.xls')
print(df[:3])