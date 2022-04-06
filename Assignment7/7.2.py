User_input=input('User Input: ')
s=User_input.split(' ')
list=[]
for i in range(int(s[0])):
  user_input=int(s[i+1])
  list.append(user_input)
Average=sum(list)/len(list)
for i in range(len(list)):
  Difference=abs(Average-list[i])
  print (Difference, end = ' ')
  
  