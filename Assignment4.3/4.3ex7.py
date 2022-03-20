import random
stop=False
number = random.randint(0,99)
while stop==False:
  prevnumber=number
  number = random.randint(0,99)
  print ("Previous Number: %d" % prevnumber)
  print ("Random Generated: %d" % number)
  if number>prevnumber:
    stop=True
  

  