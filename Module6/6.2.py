def stripSpace (str):
  r=""
  for i in range (len(str)):
    c=str[i]
    if c>='A' and c<='Z':
      r=r+c
  return r
message=input('Input Message Here: ')
result=stripSpace (message)
print (result)