# 1. Empty Function
def func1():
    pass


# func1()

# 2. Parameterless Function
def func2():
    print("Inside function 2")


# func2()

# 3. Parametrized Function
def func3(a, b):
    print(f"Value of a: {a}, and type of a is {type(a)}")
    print(f"Value of b: {b}, and type of b is {type(b)}")
    print(f"Addition is: {a + b}")


# func3(10,20)

# 3.a Positional Parameter --> Default see above example --> where argument is passed in the same order of the parameters

# 3.b Named Parameter - Parameterized Function

def func4(a, b):
    print(f"Value of a: {a}, and type of a is {type(a)}")
    print(f"Value of b: {b}, and type of b is {type(b)}")
    print(f"Addition is: {a + b}")


# func4(b = 10, a = 20)

# Combination of Named and Positional parameter

def func5(a, b, c):
    print(f"Value of a: {a}, and type of a is {type(a)}")
    print(f"Value of b: {b}, and type of b is {type(b)}")
    print(f"Value of c: {c}, and type of c is {type(c)}")
    print(f"Addition is: {a + b + c}")


# func5(5, c = 10, b = 20) # Correct
# func5(c= 5, a = 10, b = 20) # Correct

# func5(c= 5, 10, b = 20) # InCorrect, as positional argument should be BEFORE keyword argument
# func5(a= 5, c = 10, 20) # InCorrect, as positional argument should be BEFORE keyword argument
# func5(a= 5, 10, c= 20) # InCorrect, as positional argument should be BEFORE keyword argument

# 4. Function with Default Argument

def func6(a, b, c=30):
    print(f"Value of a: {a}, and type of a is {type(a)}")
    print(f"Value of b: {b}, and type of b is {type(b)}")
    print(f"Value of c: {c}, and type of c is {type(c)}")
    print(f"Addition is: {a + b + c}")


# func6(10, 20)
# print('--' * 20)
# func6(10, 20, 50)

# 5. Variable Length Arguments - Type --> Tuple

def func7(*args):
    print(f"Args value is: {args}, and type of args is {type(args)}")
    print(f"Addition: {sum(args)}")


# func7(10, 20, 30)
# func7(10, 20, 30, 40, 50)
# func7(10, 20, 30, 40, 50, 60, 70)

# 6. Keyword Varibale Length Arguments - Type --> Dictionary

def func8(**kwargs):
    print(f"Args value is: {kwargs}, and type of args is {type(kwargs)}")


# func8(a=10, b=20, c=30)


# Both *args and **kwargs --> Positional argument should be BEFORE named argument
def func9(*args, **kwargs):
    print(f"Args value is: {args}, and type of args is {type(args)}")
    print(f"Kwargs value is: {kwargs}, and type of args is {type(kwargs)}")
    print('--' * 40)

# Correct Call
# func9(10, 20, 30, 40, 50, 60, 70)
# func9(a=10, b=20, c=30)
# func9(10, 20, 30, 40, 50, 60, 70, a=10, b=20, c=30)

# Incorrect call, as Positional argument should be BEFORE named argument
# func9(10, 20, 30, a=10, b=20, c=30, 40, 50, 60, 70)
# func9(a=10, b=20, c=30, 40, 50, 60, 70)
