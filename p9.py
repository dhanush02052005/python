n=3
for i in range(n):
    for j in range(n-i):
        if(i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i):
        if(i==j-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()