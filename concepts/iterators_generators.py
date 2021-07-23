'GENERATORS'
# Generators are functions that return an iterable collection of items, one at a time, in a set manner.
# Generators, in general, are used to create iterators with a different approach.
# They employ the use of yield keyword rather than return to return a generator object.

## generate fibonacci numbers upto n ##
def fib(n):
    p, q = 0, 1
    while(p < n):
        yield p
        p, q = q, p + q

x = fib(10)    # create generator object --> which is iterable

print(x.__next__())
# print([i for i in x])


'ITERATORS'
# Iterators are objects with which we can iterate over iterable objects like lists, strings, etc.
# We will use the generator object above to use as an iterable

y = iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))