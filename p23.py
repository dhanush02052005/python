#Remove an element from a tuple, without converting into any data structures. 
tup = (1,2,3,4,5)
rem_ele = 3
print(tuple(i for i in tup if i!=rem_ele))