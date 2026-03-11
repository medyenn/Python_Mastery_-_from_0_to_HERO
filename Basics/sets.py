#!/usr/bin/env python3

set1 = {12, 3243,  34432, 1}
print(set1)  # We notice that sets don't preserve the order

# sets elements are not in order because when the cpu allocates memory for
# set's elements it dosen't take a contiguous block of memory and put them
# instead it uses some hash functions that generate a hash value
# acording to it each element gets stored somewhere
# random in the memory so it loses control on the order
# but it still very usefull because using these hash functions the access
# to the elements becomes so fast by the position number (hash value)

set1 = {13, 7, 27, 7}
print(set1)  # We notice that sets don't allow duplicates repition of items
# even if you try to insert a value multiple times it will be stored only once

# we cannot access set's elements with inddices : set1[1] doesn't exist

set1.remove(7)
print(set1)  # we notice that it's mutable as we can add or remove items

# SPECIAL METHODS

# add method
# we can't use append because it relies on index
a = {-62, 827, -329, 86, 110, -13, 167}
a.add(81)
print(a)

# update method
a.update((-1278, 218))  # we can give it any iteratable data
# structure
# update will add all the values of the iteratable at once to the set
# for remove we can use it only if we know the exact values in the set
a.remove(-329)
# We can use some shortcuts instead of the name of some methods :
a |= {218, 1267}  # SHORTCUT for UPDATE METHOD
print(a)

# DISCARD METHOD : acts like remove method but if we give a wrong value
# that doesn't exist in the set nothing happens:
a.discard(827)
a.discard(-5)
print(a)

# MATHEMATICAL METHODS IN SETS:
b = {86, 110, -13, 167, -27621, 184729, -37486, 19740}

print("\n === Maths on sets === \n")
print(a.union(b))  # here we are not changing the original sets
print(a | b)  # SHORTCUT FOR UNION

print()
# Intersection:
print(a.intersection(b))
print(a & b)  # SHORTCUT INTERSECTION

print()
# Differences
print(a.difference(b))
print(b.difference(a))

print()

print(a - b)  # Shortcut for difference
print(b - a)

print()
# the contrary of intersection:
print(a.symmetric_difference(b))
print(a ^ b)  # Shortcut for the unique elements

print()

a = {1, 3, 5, 7, 9}
b = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(a.issubset(b))  # It tells if the first set is fully exist in the second
print(b.issuperset(a))  # It tells if the first conatins full the second
print(a.isdisjoint(b))  # It tells if there is no common values
