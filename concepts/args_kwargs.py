'*args'

# *args is a special syntax used in function definition to pass variable-length argument.
# “*” means variable length and “args” is the name used by convention. You can use any other.

def multiply(a, b, *argv):
    mul = a * b

    for num in argv:
        mul *= num

    return mul

print(multiply(1, 2, 3, 4, 5)) #output: 120

#================================================================================================#

'**kwargs'

# **kwargs is a special syntax used in function definition to pass variable-length keyworded argument.
# Keyworded argument means a variable which has a name when passed to a function.
# It is actually a dictionary of variable name and its value.
def tellArguments(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)
tellArguments(arg1 = "1", arg2 = "2", arg3 = "3")