user_input=input('User Input: ')
s=user_input.split (' ')
length=int(s[0])
list1=[]
for i in range (length):
  User_input=int(s[i+1])
  list1.append(User_input)
print (list1)
list2=[]
for i in range (int(s[length+1])):
  Userinput=int(s[length+i+2])
  list2.append(Userinput)
print (list2)
for i in range (len(list2)):
  try:
    index2=list1.index(list2[0])
  except ValueError:
    print ('False')
    break
  m=index2+i
  if m>=len(list1):
    print ('False')
    break
  if list1[m]!=list2[i]:
    print ('False')
    break
else: print ('True')


    
    