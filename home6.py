a = [
    [11,12,13],
    [21,22,23],
    [31,32,33,]
]
b = [
    [14,24,34]
]
c = 0
for i in a:
    for x in b:
        i.append(x[c])
        c += 1
        print(i) 
