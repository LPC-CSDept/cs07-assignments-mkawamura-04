import random
number=5
def makeList (n):
  l=[]
  for i in range (number):
    l.append(random.randrange(1,10))
  return l
list1=makeList (number)
print (list1)
list2=makeList (number)
print (list2)
list3=[]
def sumFunction (list1,list2):
  sum=0
  for i in range (len(list1)):
    sum=sum+list1[i]*list2[i]
    i=i+1
  return (sum)
result=sumFunction (list1,list2)
print(result)
  
  
