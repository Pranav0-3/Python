#  Tuples
#***********************************************************************************************************************

# ***********************************___________TUPLES____________*******************************************************

# Tuple
# A tuple is a collection of objects which is ordered and immutable. 
# Tuples are similar to lists, the main difference ist the immutability. 
# In Python tuples are written with round brackets and comma separated value
# my_tuple = ("Max", 28, "New York")

# Reasons to use a tuple over a list
# Generally used for objects that belong together.
# Use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
# Since tuple are immutable, iterating through tuple is slightly faster than with list.
# Tuples with their immutable elements can be used as key for a dictionary. This is not possible with lists.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.


# Create a tuple
# Tuples are created with round brackets and comma separated values. Or use the built-in tuple function.



tuple_1 = ("Max", 28, "New York")
tuple_2 = "Linda", 25, "Miami" # Parentheses are optional

# Special case: a tuple with only one element needs to have a comma at the end, 
# otherwise it is not recognized as tuple
tuple_3 = (25,)
print(tuple_1)
print(tuple_2)
print(tuple_3)

# Or convert an iterable (list, dict, string) with the built-in tuple function
tuple_4 = tuple([1,2,3])
print(tuple_4)


# OUTPUT:
# ('Max',28,'New York')
# ('Linda', 25, 'Miami')
# (25,) 
# (1,2,3)










# Access elements
# You access the tuple items by referring to the index number. Note that the indices start at 0.



item = tuple_1[0]
print(item)
# You can also use negative indexing, e.g -1 refers to the last item,
# -2 to the second last item, and so on
item = tuple_1[-1]
print(item)


# OUTPUT:
# Max
# New York









# Add or change items
# Not possible and will raise a TypeError.

#tuple_1[2] = "Boston"

# OUTPUT:
# TypeError           Traceback (most recent call last)
# <ipython-input-5-c391d8981369> in <module>
# ----> 1 tuple_1[2] = "Boston"

# TypeError: 'tuple' object does not support item assignment




# Delete a tuple
del tuple_2



# Iterating
# Iterating over a tuple by using a for in loop
for i in tuple_1:
    print(i)



# OUTPUT:
# Max
# 28
# New York









# Check if an item exists
if "New York" in tuple_1:
    print("yes")
else:
    print("no")

    # OUTPUT:
    # yes












# Usefule methods
my_tuple = ('a','p','p','l','e',)

            # len() : get the number of elements in a tuple
print(len(my_tuple))                                        #5



            # count(x) : Return the number of items that is equal to x
print(my_tuple.count('p'))                                   #2




            # index(x) : Return index of first item that is equal to x
print(my_tuple.index('l'))                                    #3




            # repetition
my_tuple = ('a', 'b') * 5       
print(my_tuple)                                                 #('a','b','a','b','a','b','a','b','a','b')




            # concatenation
my_tuple = (1,2,3) + (4,5,6)
print(my_tuple)                                                 #(1,2,3,4,5,6)




            # convert list to a tuple and vice versa
my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print(list_to_tuple)                                            #('a','b','c','d')

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)                                            #['a','b','c','d']

            
            
            
            # convert string to tuple
string_to_tuple = tuple('Hello')
print(string_to_tuple)                                          #("H",'e','l','l','0')












# Slicing
# Access sub parts of the tuple wih the use of colon (:), just as with strings.

# a[start:stop:step], default step is 1
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
b = a[::2] # start to end with every second item
print(b)
b = a[::-1] # reverse tuple
print(b)

# OUTPUT:
# (2, 3)
# (3, 4, 5, 6, 7, 8, 9, 10)
# (1, 2, 3)
# (1, 3, 5, 7, 9)
# (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)













# Unpack tuple
# number of variables have to match number of tuple elements
tuple_1 = ("Max", 28, "New York")
name, age, city = tuple_1
print(name)
print(age)
print(city)

# tip: unpack multiple elements to a list with *
my_tuple = (0, 1, 2, 3, 4, 5)
item_first, *items_between, item_last = my_tuple
print(item_first)
print(items_between)
print(item_last)











# Nested tuples
# Tuples can contain other tuples (or other container types).

a = ((0, 1), ('age', 'height'))
print(a)
print(a[0])


# OUTPUT:
# ((0, 1), ('age', 'height'))
# (0, 1)









# Compare tuple and list
# The immutability of tuples enables Python to make internal optimizations. 
# Thus, tuples can be more efficient when working with large data.


# compare the size
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# compare the execution time of a list vs. tuple creation statement
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))