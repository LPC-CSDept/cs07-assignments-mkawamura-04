getEvens = lambda l: filter(lambda n: n%2 == 0, l)
def getMerged(list1, list2):
    e1 = getEvens(list1)
    e2 = getEvens(list2)

    for i in e1:
        yield i
    for i in e2:
        yield i

list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1)
print(list2)

for i in getMerged(list1, list2):
    print(i, end=' ')
