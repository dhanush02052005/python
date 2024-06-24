# Find the frequency of each element in a tuple, using dictionary.
tup = (1,2,3,4,5,1,2,3)
d= dict()
for i in tup:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
print(d)