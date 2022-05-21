isspace=lambda c: True if c==' ' else False 
def mystrip(str):
  r=""
  for i in range (len(str)):
    c=str[i]
    if not isspace (c):
      r=r+c
  return r
message=input('Input Message Here: ')
result=mystrip(message)
print(result)
