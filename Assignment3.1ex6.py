import random
number1 = random.randint(0,100)
print(number1)
import random
number2 = random.randint(0,100)
print(number2)
import random
number3 = random.randint(0,100)
print(number3)
if(number1<number2 and number1<number3): print('Number 1 is the smallest')
elif(number2<number1 and number2<number3): print ('Number 2 is the smallest')
else: print('Number 3 is the smallest')