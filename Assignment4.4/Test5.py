import random
numbers= []
for x in range (10):
  numbers.append (random.randint(0,100))
print (numbers)
minVal=min(numbers)
minValIndex=numbers.index(minVal)
numbers[minValIndex]=numbers[0]
numbers[0]=minVal
print (numbers)
minVal2=min(numbers[1:])
minVal2Index=numbers[1:].index(minVal2)+1
numbers[minVal2Index]=numbers[1]
numbers[1]=minVal2
print(numbers)

