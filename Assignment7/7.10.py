import random
row=input('Row Number: ')
column=input('Column Number: ')
list2=[]
list5=[]
for j in range (int(row)):
  list1=[]  
  for i in range (int(column)):
    list1.append(random.randint(1,100))
  list2.append(list1)
print(list2)
list4=[]
for j in range (int(column)):
  column_sum=0
  for i in range (int(row)):
    column_sum=column_sum+list2[i][j]
  list4.append(column_sum)
print ('Sum of Columns: {0}'.format(list4))
for i in range (int(row)):
  row_sum=0
  for j in range (int(column)):
    row_sum=row_sum+list2[i][j]
  list5.append(row_sum)
print ('Sum of Rows: {0}'.format(list5))
index_c=list4.index(max(list4))
print ('Max Column: {0}'.format(index_c+1))
index_r=list5.index(max(list5))
print ('Max Row: {0}'.format(index_r+1))
#in the event of multiple max rows or columns, the program will only show the first one
  
    
  