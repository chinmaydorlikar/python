def low_dec(function):
    def wrapper():
        func = function()
        return func.lower()
    return wrapper

def split_dec(function):
    def wrapper():
        func = function()
        return func.split()
    return wrapper

def join_dec(function):
    def wrapper():
        func = function()
        return "_".join(func)
    return wrapper

@join_dec #-->Applied 3rd
@split_dec #-->Applied 2nd
@low_dec #-->Applied 1st
def hello():
    return "Hello World Python!"

print(hello())