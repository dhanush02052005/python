def fibonacci(n):
    if n<2:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n=5
for i in range(n+1):
    print(fibonacci(i))



