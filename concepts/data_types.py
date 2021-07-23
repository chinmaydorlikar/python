# int	: Stores integer literals including hex, octal and binary numbers as integers
x=3
print(type(x))

# float	: Stores literals containing decimal values and/or exponent sign as floating-point numbers
x=3.1
print(type(x))

# complex	: Stores complex number in the form (A + Bj) and has attributes: real and imag
x=3+4j
print(type(x), x.real, x.imag, x.conjugate())

# bool : Stores boolean value (True or False)
x=True
print(type(x))

#================================================================================#

# list :	Mutable sequence used to store collection of items.
x = [1, 2, 3, "string"]
print(type(x))

# tuple	: Immutable sequence used to store collection of items.
x = (1, 2, 3, "string")
print(type(x))

# range	: Represents an immutable sequence of numbers generated during execution.
print(type(range(5)))

# str	: Immutable sequence of Unicode code points to store textual data.
x="Hello World"
print(type(x))

#================================================================================#

# dict : Stores comma-separated list of key: value pairs
x = {'a':2, 'b':3}
print(type(x))

# set	Mutable unordered collection of distinct hashable objects
x = {2, 11, 8, 5,6}
print(type(x))

# frozenset	Immutable collection of distinct hashable objects
x = frozenset(x)
print(type(x), x)