a="abcdef"
b="abcdhf"
c=0
for i in range(len(a)):
    if a[i] in b:
        c+=1
print(c)