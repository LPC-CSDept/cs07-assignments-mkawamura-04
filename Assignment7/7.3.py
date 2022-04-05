user_input=input('User Input: ')
s=user_input.split (' ')
length=int(s[0])
list1=[]
for i in range (length):
  User_input=int(s[i+1])
  list1.append(User_input)
for i in range (int(s[length+1])):
  Userinput=int(s[length+i+2])
  if not Userinput in list1:
    print ('False')
    break
else: 
  print ('True')   
    
