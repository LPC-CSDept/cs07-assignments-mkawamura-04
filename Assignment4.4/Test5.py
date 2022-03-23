import random
numbers= []
for x in range (10):
  numbers.append (random.randint(0,100))
print (numbers)
minVal=min(numbers)
minValIndex=numbers.index(minVal)
print (minValIndex)
print (numbers[5])
numbers[minValIndex]=numbers[0]
numbers[0]=minVal
print (numbers)