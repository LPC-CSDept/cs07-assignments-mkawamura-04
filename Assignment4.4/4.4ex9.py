import random
number = random.randint(0,99)
while True:
  prevnumber=number
  number = random.randint(0,99)
  print ("Previous Number: %d" % prevnumber)
  print ("Random Generated: %d" % number)
  if number>prevnumber:
    break  