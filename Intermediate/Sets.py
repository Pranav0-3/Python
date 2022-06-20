# Sets
#**************************************************************************************************************************



#*******************************************________SETS________*****************************************************



# Sets
# A Set is an unordered collection data type that is unindexed, mutable, and has no duplicate elements. 
# Sets are created with braces.

# my_set = {"apple", "banana", "cherry"}





# Create a set
# Use curly braces or the built-in set function.

my_set = {"apple", "banana", "cherry"}
print(my_set)

# or use the set function and create from an iterable, e.g. list, tuple, string
my_set_2 = set(["one", "two", "three"])
my_set_2 = set(("one", "two", "three"))
print(my_set_2)

my_set_3 = set("aaabbbcccdddeeeeeffff")
print(my_set_3)

# careful: an empty set cannot be created with {}, as this is interpreted as dict
# use set() instead
a = {}
print(type(a))
a = set()
print(type(a))

# {'banana', 'apple', 'cherry'}
# {'three', 'one', 'two'}
# {'b', 'c', 'd', 'e', 'f', 'a'}
# <class 'dict'>
# <class 'set'>














# Add elements
my_set = set()

# use the add() method to add elements
my_set.add(42)
my_set.add(True)
my_set.add("Hello")

# note: the order does not matter, and might differ when printed
print(my_set)

# nothing happens when the element is already present:
my_set.add(42)
print(my_set)


# {True, 42, 'Hello'}
# {True, 42, 'Hello'}












# Remove elements
# remove(x): removes x, raises a KeyError if element is not present

my_set = {"apple", "banana", "cherry"}
my_set.remove("apple")
print(my_set)

# KeyError:
# my_set.remove("orange")

# discard(x): removes x, does nothing if element is not present
my_set.discard("cherry")
my_set.discard("blueberry")
print(my_set)

# clear() : remove all elements
my_set.clear()
print(my_set)

# pop() : return and remove a random element
a = {True, 2, False, "hi", "hello"}
print(a.pop())
print(a)


# {'banana', 'cherry'}
# {'banana'}
# set()
# False
# {True, 2, 'hi', 'hello'}










# Check if element is in Set
my_set = {"apple", "banana", "cherry"}
if "apple" in my_set:
    print("yes")

# yes














# Iterating
# Iterating over a set by using a for in loop
# Note: order is not important
my_set = {"apple", "banana", "cherry"}
for i in my_set:
    print(i)


# banana
# apple
# cherry














# Union and Intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union() : combine elements from both sets, no duplication
# note that this does not change the two sets
u = odds.union(evens)
print(u)

# intersection(): take elements that are in both sets
i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# set()
# {3, 5, 7}
# {2}
















# Difference of sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# difference() : returns a set with all the elements from the setA that are not in setB.
diff_set = setA.difference(setB)
print(diff_set)

# A.difference(B) is not the same as B.difference(A)
diff_set = setB.difference(setA)
print(diff_set)

# symmetric_difference() : returns a set with all the elements that are in setA and setB but not in both
diff_set = setA.symmetric_difference(setB)
print(diff_set)

# A.symmetric_difference(B) = B.symmetric_difference(A)
diff_set = setB.symmetric_difference(setA)
print(diff_set)


# {4, 5, 6, 7, 8, 9}
# {10, 11, 12}
# {4, 5, 6, 7, 8, 9, 10, 11, 12}
# {4, 5, 6, 7, 8, 9, 10, 11, 12}















# Copying
set_org = {1, 2, 3, 4, 5}

# this just copies the reference to the set, so be careful
set_copy = set_org

# now modifying the copy also affects the original
set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)

# use copy() to actually copy the set
set_org = {1, 2, 3, 4, 5}
set_copy = set_org.copy()

# now modifying the copy does not affect the original
set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)


# {1, 2, 3, 4, 5, 6, 7}
# {1, 2, 3, 4, 5, 6, 7}

# {1, 2, 3, 4, 5, 6, 7}
# {1, 2, 3, 4, 5}














# Subset, Superset, and Disjoint
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
# issubset(setX): Returns True if setX contains the set
print(setA.issubset(setB))
print(setB.issubset(setA)) # True

# issuperset(setX): Returns True if the set contains setX
print(setA.issuperset(setB)) # True
print(setB.issuperset(setA))

# isdisjoint(setX) : Return True if both sets have a null intersection, i.e. no same elements
setC = {7, 8, 9}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))


# False
# True
# True
# False
# False
# True