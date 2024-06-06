num = [1,2,4,5,3,4,5,4,6]  #remove repeating elements
p=[]
for i in range(len(num)):
    flag=0
    for j in range(len(num)):
        if i==j:
            continue
        else:
            if(num[i]==num[j]):
                flag = flag+1
    if(flag==0):
        p.append(num[i])
print(p)