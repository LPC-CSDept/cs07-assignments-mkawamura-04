x=input('X coordinate:')
y=input('Y coordinate:')
X=int(x)
Y=int(y)
if (X>0 and Y>0): print('Your point is in quadrant 1')
elif (X<0 and Y>0): print('Your point is in quadrant 2')
elif (X>0 and Y<0): print('Your point is in quadrant 4')
elif (X<0 and Y<0): print('Your point is in quadrant 3')
else : print('Error')