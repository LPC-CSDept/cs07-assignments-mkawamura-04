import random
N=20
list1=[]
for i in range (N):
  list1.insert (i, random.randint(1,10))
print (list1)
target=input('Value To Be Deleted: ')
Target=int(target)
while Target in list1:
  list1.remove(Target)
print (list1)