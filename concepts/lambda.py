'LAMBDA'
#A function with a single expression. Used for a quick use

# Assigning lambda functions to a variable
mul = lambda a, b : a * b
print(mul(2, 5))    # output => 10

# Wrapping lambda functions inside another function
def myWrapper(n):
  return lambda a : a * n

mulFive = myWrapper(5)
print(mulFive(2))    # output => 10


'SLICING'
# Syntax for slicing is [start : stop : step]
# Default value for start is 0, stop is number of items, step is 1.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1 : : 2])  #output : [2, 4, 6, 8, 10]