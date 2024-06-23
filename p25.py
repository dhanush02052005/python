# Merge the given two tuples without duplicates.
tup1 = (1,2,3,4,3)
tup2 = (4,5,6,4,5)
convert = set(tup1).union(set(tup2))
print(tuple(convert))