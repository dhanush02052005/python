def fact(n):      #recursion
    if(n==1):
        return n
    else:
        return n*fact(n-1)
n=5
print(fact(n))


from functools import reduce #reduce function

n=5
word = reduce(lambda x,y : x*y ,range(1,n+1))
print(word)