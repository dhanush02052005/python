num = [1,2,3,4,3,5,1]
ele = 3
p=[]
for i in range(len(num)):
    if num[i] == ele:
        continue
    else:
        p.append(num[i])
print(p)