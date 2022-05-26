def makeLists(fname,lists):
    f=open(fname)
    for line in f.readlines():
        record=line.split()
        for i in range(0,4):
            lists[i].append(record[i+1])