stop=False
user_input=input('Input Numbers: ')
s=user_input.split(' ')
numbers=[]
for i in range (len(s)):
  numbers.append(int(s[i]))
i=0
m=False
while True:
  if i+1>= len(numbers):
    break
  if numbers[i] % 2==0 and numbers[i+1] % 2==0:
    print(numbers[i])
    print(numbers[i+1])
    m=True
    break
  i=i+1
if m==False:
  print('No Consecutive Even Numbers')
    
