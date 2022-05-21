import xlrd
workbook = xlrd.open_workbook('student.xls')
sheetNames = workbook.sheet_names()
sheetByIndex = workbook.sheet_by_index(0)
firstColumn = sheetByIndex.col_values(0)
print(firstColumn)
secondColumn = sheetByIndex.col_values(1)
print(secondColumn)
print(sheetByIndex.col_values(2))

