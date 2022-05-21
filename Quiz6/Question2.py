getEvens=lambda n: True if n%2==0 else False
def getMerged (list1,list2):
  list3=[]
  list4=[]
  for i in range (len(list1)):
    n=list1[i]
    if not getEvens (n):
      list3.append(n)
  for i in range(len(list2)):
    n=list2[i]
    if not getEvens (n):
      list4.append(n)
  finalList=list3+list4
  return (finalList)
list1=[1,2,3,4]
list2=[5,6,7,8]
result=getMerged (list1,list2)
print(result)
