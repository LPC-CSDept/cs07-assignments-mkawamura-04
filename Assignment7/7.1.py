user_input=input('Enter a Number: ')
User_input=int(user_input)
list=[]
while User_input>=0:
  list.append(User_input)
  user_input=input("Enter a Number: ")
  User_input=int(user_input)
list.remove(min(list))
list.remove(max(list))
Sum=sum(list)
Average=Sum/len(list)
print(Sum)
print(Average)