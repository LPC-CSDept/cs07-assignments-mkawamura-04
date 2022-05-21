isspace = lambda c : True if c == ' ' else False
def getalnum(str):
    for i in range(len(str)):
        c = str[i]
        if isspace(c):
            continue
        yield str[i]
msg = input('Input Message Here: ')
res = getalnum(msg)
for v in res:
    print(v, end='')