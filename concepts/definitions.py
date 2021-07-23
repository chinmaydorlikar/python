"**********"
# In Python, arguments are passed by reference, i.e., reference to the actual object is passed.
"**********"

MODULES
# Modules, in general, are simply Python files with a .py extension
# They can have a set of functions, classes or variables defined and implemented.
# They can be imported and initialized once using the import statement.
# If partial functionality is needed, import the requisite classes or functions using
# from foo import bar.

PACKAGES
# Packages allow for hierarchial structuring of the module namespace using dot notation.
# As, modules help avoid clashes between global variable names, packages help avoid clashes between
# module names.

GLOBAL
# Global variables are public variables that are defined in the global scope.

PROTECTED
# Protected attributes are attributes defined with a underscore prefixed to their identifier eg. _sara.
# They can still be accessed and modified from outside the class they are defined in but
# a responsible developer should refrain from doing so.

PRIVATE
# Private attributes are attributes with double underscore prefixed to their identifier eg. __ansh.
# They cannot be accessed or modified from the outside directly and will result in an AttributeError
# if such an attempt is made.

SELF
# Self is a keyword in Python used to define an instance or an object of a class.


__init__
# __init__ is a contructor method in Python and is automatically called to allocate memory
# when a new object/instance is created.
class Student:
    def __init__(self, fname, lname, age, section):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.section = section

# creating a new object
stu1 = Student("Sara", "Ansh", 22, "A2")