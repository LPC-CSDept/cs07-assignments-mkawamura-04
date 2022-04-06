User_input=input('User Input: ')
s=User_input.split(' ')
list1=[]
for i in range(int(s[0])):
  user_input=int(s[i+1])
  list1.append(user_input)
Average=sum(list1)/len(list1)
for i in range(len(list1)):
  Difference=abs(Average-list1[i])
  print (Difference, end = ' ')
  
  