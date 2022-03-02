import random
sum=0
while sum<101:
  number = random.randint(0,100)
  sum=sum+number
  print(number)
print ('Sum: %d ' % sum)