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
tuple2=tuple(list2)
if tuple2 in list1:
  print ('True')