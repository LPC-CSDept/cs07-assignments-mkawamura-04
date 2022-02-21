import random
sum=0
while sum<101:
  number = random.randint(0,100)
  print(number)
  sum=sum+number
print ('Sum: %d ' % sum)