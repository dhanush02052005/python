num = [[1,2,3,4,5],[1,2,3,4],[1,2]]  
l = num[0]
for i in range(len(num)):
    if(len(num[i]) > len(l)):
        l=num[i]
print(l)