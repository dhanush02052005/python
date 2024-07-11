#Write a program to create a dictionary where the values are squares of the keys
n=5
d=dict()
for i in range(1,n+1):
    d[i] = i**2
print(d)