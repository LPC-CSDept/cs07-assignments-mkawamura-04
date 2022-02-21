import random
stop=False
while stop==False:
  number = random.randint(0,100)
  if (number%2)==0:
    print('Even Number--Program Stopped')
    #print(number)for testing purposes
    print (number)
    stop=True
  else:print(number)


