list1=[5, 20, 30, 35, 50]
v=25
for i in range (3):
  if v>list1[i] and v<list1[i+1]:
    list1.insert (i+1, v)
if v>list1[4]:
  list1.append (v)
if v<list1[0]:
  list1.insert (0, v)
print (list1)