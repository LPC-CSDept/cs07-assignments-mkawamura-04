User_input=input('User Input: ')
s=User_input.split(' ')
print(s)
list=[]
for i in range(int(s[0])):
  user_input=int(s[i+1])
  list.append(user_input)
print (list)
Average=sum(list)/len(list)
print (Average)
Sum=0
for i in range(len(list)):
  Difference=abs(Average-list[i])
  print (Difference, end = ' ')
  
  