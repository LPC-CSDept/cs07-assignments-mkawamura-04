stop=False
user_input=input('Input Numbers: ')
s=user_input.split(' ')
for i in range (len(s)):
  numbers[i]=int(s[i])
while stop==False:
  for i in range(len(numbers)):
    if numbers[i] % 2=0 and numbers[i+1] % 2=0:
      print(numbers[i])
      print(numbers[i+1])
      break
else:
  print('No Consectutive Even Numbers')
    
