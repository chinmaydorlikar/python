# Shallow Copy is a bit-wise copy of an object.
from copy import copy, deepcopy

list_1 = [1, 2, [3, 5], 4]

## shallow copy

list_2 = copy(list_1)
list_2[3] = 7
list_2[2].append(6)

print("copy    : ",list_2)    # output => [1, 2, [3, 5, 6], 7]
print("original: ",list_1)    # output => [1, 2, [3, 5, 6], 4]

# Deep Copy copies all values recursively from source to target object
# It even duplicates the objects referenced by the source object.

list_3 = deepcopy(list_1)
list_3[3] = 8
list_3[2].append(7)

print("deepcopy: ",list_3)    # output => [1, 2, [3, 5, 6, 7], 8]
print("original: ",list_1)    # output => [1, 2, [3, 5, 6], 4]