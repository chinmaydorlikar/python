# Performing mathematical operations on the entire list
my_list = [2, 3, 5, 7, 11]

squared_list = [x**2 for x in my_list]    # ---->list comprehension
# output => [4 , 9 , 25 , 49 , 121]

squared_dict = {x:x**2 for x in my_list}    # ---->dict comprehension
# output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}

# Performing conditional filtering operations on the entire list
my_list = [2, 3, 5, 7, 11]

squared_list = [x**2 for x in my_list if x%2 != 0]
# output => [9 , 25 , 49 , 121]

squared_dict = {x:x**2 for x in my_list if x%2 != 0}
# output => {11: 121, 3: 9 , 5: 25 , 7: 49}

# Combining multiple lists into one
# Comprehensions allow for multiple iterators and hence, can be used to combine multiple lists into one.
a = [1, 2, 3]
b = [7, 8, 9]

[(x + y) for (x,y) in zip(a,b)]  # parallel iterators
# output => [8, 10, 12]

[(x,y) for x in a for y in b]    # nested iterators
# output => [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)]