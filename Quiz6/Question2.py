isEvens=lambda n: True if n%2==0 else False
def getMerged (list1,list2):
  list3=[]
  list4=[]
  for i in range (len(list1)):
    n=list1[i]
    if not isEvens (n):
      list3.append(n)
  for i in range(len(list2)):
    n=list2[i]
    if not isEvens (n):
      list4.append(n)
  yield (list3+list4)
result=getMerged([1,2,3,4],[5,6,7,8])
print (next(result))
