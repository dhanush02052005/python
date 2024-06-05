num = [1,2,3,4,5,3,4,6]           #Remove Duplicates
p=[]
for i in range(len(num)):
    if (num[i] not in p):
        p.append(num[i])
print(p)