'''Write a program to perform the following:-
1. Add an element to the set.
2. Remove an element to the set.
3. To perform the below for the given two set.
    a. Intersection
    b. Difference
    c. Symmetric difference
    d. Is a sub set of the another
    e. Given two set is a disjoint set'''
set = {1,2,3,4,5}
set.add(7)
print(set)

set = {1,2,3,4,5}
set.remove(3)
print(set)

set1 = {1,2,3,4,5}
set2 = {2,3,4,5,6}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.isdisjoint(set2))
