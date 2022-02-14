import random
number1 = random.randint(0,100)
print(number1)
import random
number2 = random.randint(0,100)
print(number2)
import random
number3 = random.randint(0,100)
print(number3)
if(number1==number2 and number2==number3) : print('All Numbers Are the Same')
elif(number1==number2): print('Numbers 1 and 2 are the same')
elif(number2==number3): print('Numbers 2 and 3 are the same')
elif(number3==number1): print('Numbers 1 and 3 are the same')
else: print('None are the same')