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
if (len(list1) < len(list2)):
  list3=list1+list2
else:
  list3=list2+list1
print (list3)