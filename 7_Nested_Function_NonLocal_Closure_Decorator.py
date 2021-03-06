# Nested Function

# global scope
num = 100


def outer():
    num = 200
    print(f"num: {num}")

    def inner():
        global num
        print("Inside Inner")
        print(f"num: {num}")  # Output: 200

    inner()


# outer()


def outer():
    print("Inside Outer")
    num = 200
    print(f"num: {num}")

    def inner():
        print("Inside Inner")
        num = 300
        num2 = 500
        print(f"num: {num}")
        print(f"num2: {num2}")

    inner()
    print(f"num: {num}")
    # print(f"num2: {num2}") # Outer() cannot access inner() variables/properties.


# outer()

# Non Local Keyword: used to modify the state of Outer function properties
# ---------------------------------------------------------------------------
# global
# num = 100
# print(f"global num: {num}")
# print('--' * 30)


def outer():
    print("Inside Outer()")
    # local
    num = 200
    print(f"local num: {num}")
    print('--' * 30)

    def inner1():
        print("Inside INNER1")
        num = 300
        print(f"local num: {num}")
        print('--' * 30)

    def inner2():
        print("Inside INNER2")
        global num
        num = 400
        print(f"global num: {num}")
        print('--' * 30)

    def inner3():
        print("Inside INNER3")
        nonlocal num
        num = 500
        print(f"nonlocal num: {num}")
        print('--' * 30)

    inner1()
    inner2()
    inner3()

    print(f"local num: {num}")


# outer()
# print(f"global num: {num}")
# print('--' * 30)


# -----------------------------------------------------------------------
"""
CLOSURE: Closure is a phenomenon of nested functions, when an outer function returns inner function reference.

The criteria that must be met to create closure in Python are summarized in the following points:
    1. We must have a nested function (function inside a function).
    2. The nested function must refer to a value defined in the enclosing function.
    3. The enclosing function must return(by reference) the nested function.

Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.
When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solution. 
But when the number of attributes and methods get larger, it's better to implement a class.

Fixed parameters are passed to outer functions, and the variable parameters are passed to the inner function.
"""


# -----------------------------------------------------------------------

# This is an example of closure, as outer() returns inner function.
def outer():
    num = 100
    print(f"Inside Outer")

    def inner():
        print("Inside Inner")
        print(f"num: {num}")

    # return by value
    # return num

    # return by reference
    return inner


# a = outer()
# print(f"a: {a}, type of a: {type(a)}")
# a()


# examples:
# 1. Print a table of a number

def table(num):
    def inner():
        print([num * i for i in range(1, 11)])

    return inner


def run():
    table_4 = table(4)
    print(f"table_4: {table_4}, type of table_4: {type(table_4)}")
    table_4()

    print('--' * 40)

    table_5 = table(5)
    print(f"table_5: {table_5}, type of table_5: {type(table_5)}")
    table_5()


# run()


# -----------------------------------------------------------------------
"""
DECORATOR: used to perform a common set of pre and post operations, before/after a function call. Achieved via Closure. 
        Used for Logging, Auditing etc.
        A decorator takes in a function, adds some functionality and returns it.
        When we want to embed some extra functionality to a common function, then we can use a decorator. 
"""


# -----------------------------------------------------------------------

# def decorate_result1(func):
#     print("Inside Decorator")
#
#     def inner(p1, p2):
#         print("Inside Inner - Function called")
#         func(p1, p2)
#         print("--" * 30)
#
#     return inner


def decorate_result(func):
    print("Inside Decorator")

    def inner(*args):
        print("Inside Inner - Function called")
        func(*args)
        print("--" * 30)

    return inner


# @decorate_result
def add(a, b):
    print(f"a+b: {a + b}")


# @decorate_result
def subtract(a, b):
    print(f"a-b: {a - b}")


# @decorate_result
def multiply(a, b):
    print(f"a*b: {a * b}")


# @decorate_result
def divide(a, b):
    print(f"a/b: {a / b}")


def run1():
    add(10, 20)
    subtract(10, 20)
    multiply(10, 20)
    divide(10, 20)


# run()
# --------------------------------------

def dec_results(func):
    print(f"Inside Decorator")

    def inner():
        print("**" * 40)
        func()
        print("**" * 40)

    return inner


friends = {
    'Manoj': {'Age': 29, 'City': 'Pune'},
    'Saurav': {'Age': 28, 'City': 'Aligarh'},
    'Kanchan': {'Age': 25, 'City': 'Pune'},
    'Sam': {'Age': 24, 'City': 'Mumbai'},
    'Payal': {'Age': 22, 'City': 'Raipur'}
}


# @dec_results
# @decorate_result
def list_friends():
    for key, value in friends.items():
        print(f"Friend name is {key}, Age is {value['Age']} and lives in {value['City']}")


# list_friends()
# ------------------------------------

def logger(func):
    def inner(*args, **kwargs):
        print("In Logger ---- Function Call")
        print(f"Function {func} is called.")
        print(f" Parameters: args =>{args}, kwargs=> {kwargs}")
        func(*args, **kwargs)
        print(f"Function processing finished")
        print("--" * 40)

    return inner


@logger
def add(a, b):
    print(f"a+b: {a + b}")


@logger
def subtract(a, b):
    print(f"a-b: {a - b}")


@logger
def multiply(a, b):
    print(f"a*b: {a * b}")


@logger
def divide(a, b):
    print(f"a/b: {a / b}")


@logger
def square(a=20):
    print(f"a**2: {a ** 2}")


def run():
    add(10, 20)
    subtract(b=10, a=20)
    multiply(10, b=20)
    divide(10, 20)
    square(a=10)
    square()


# run()


# -------------------------------------------------------------------------------
# Parameterized Decorator

def repeat(count=1):
    def repeat_decorator(func):
        def inner(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)
            print("--" * 20)

        return inner

    return repeat_decorator


@repeat(count=3)
def function1():
    print("Inside function1")


@repeat(count=5)
def function2():
    print("Inside function2")


@repeat()
def function3():
    print("Inside function3")


def run():
    function1()
    function2()
    function3()


run()


