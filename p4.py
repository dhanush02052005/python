n=5
for i in range(n):
    for j in range(n):
        if(i==j or j==n-i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()