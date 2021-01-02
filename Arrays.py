# Basic Operations
# Following are the basic operations supported by an array.
#   Traverse − print all the array elements one by one.
#   Insertion − Adds an element at the given index.
#   Deletion − Deletes an element at the given index.
#   Search − Searches an element using the given index or by the value.
#   Update − Updates an element at the given index.

from array import *

# arrayName = array(typecode, [Initializers])
#
# Typecodes:
# b	    Represents signed integer of size 1 byte/td>
# B	    Represents unsigned integer of size 1 byte
# c	    Represents character of size 1 byte
# i	    Represents signed integer of size 2 bytes
# I	    Represents unsigned integer of size 2 bytes
# f	    Represents floating point of size 4 bytes
# d	    Represents floating point of size 8 bytes

# Creating an array and printing all elements
print('Print new array')
array1 = array('i', [10,20,30,40,50])
for x in array1:
    print(x)

# Accessing specific elements using print
print('\nPrint index 0 and 2')
print(array1[0])
print(array1[2])

# Inserting an element at index 1
print('\nInsert 60 at index 1')
array1.insert(1,60)
for x in array1:
    print(x)

# Removing an element
print('\nRemove element 40')
array1.remove(40)
for x in array1:
    print(x)

# Search for elemnt 50 and print index
print('\nFind index of element 50')
print(array1.index(50))

# Update index 2
print('\nUpdate index 2 to equal 80')
array1[2] = 80
for x in array1:
    print(x)