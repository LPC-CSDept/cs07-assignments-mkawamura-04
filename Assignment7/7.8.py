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
list3=[]
if len(list1)>len(list2):
  minlength=len(list2)
  remaining=list1
else:
  minlength=len(list1)
  remaining=list2
for i in range (minlength):
    list3.append(list1[i])
    list3.append(list2[i])
list3.extend(remaining [minlength:])
print (list3)
