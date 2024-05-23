n=5
count=0
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(65+count),end="")
        count+=1
    print()