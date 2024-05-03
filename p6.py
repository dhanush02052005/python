n=5
for i in range(n):
    for j in range(n):
        if(j==n-i-1):
            print("*",end=" ")
        elif(i==j and (i<n/2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()