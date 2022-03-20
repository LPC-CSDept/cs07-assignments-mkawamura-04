import random
i=0
sum=0
s="Numbers: "
while i<10:
  number = random.randint(0,100)
  sum=sum+number
  s=s+str(number)+", "  
  i=i+1
  if sum>100:
    break
if sum>100:
  print (s, end='')
  print ("Sum: %d" % sum)
else:
  print ("The total is <=100" )
    