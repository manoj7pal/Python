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
# func5(a= 5, b=10, 20) # InCorrect, as positional argument should be BEFORE keyword argument

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


# ---------------------------------------------------------------------------------------------------------------------

# SCOPE: Global and Local Scope

num = 100


# print(f"num: {num}, Type: {type(num)}")


def func1():
    num = 400
    print("Inside func1")
    print(f"num: {num}, Type: {type(num)}")


# func1()
# print(f"num: {num}, Type: {type(num)}")

# ---------------------------------------------

num = 100


# print(f"num: {num}, Type: {type(num)}")


def func1():
    print("Inside func1")
    print(f"num: {num}, Type: {type(num)}")


# func1()
# print(f"num: {num}, Type: {type(num)}")
# ---------------------------------------------

num = 100


# print(f"num: {num}, Type: {type(num)}")


def func1():
    print("Inside func1")
    print(
        f"num: {num}, Type: {type(num)}")  # Local varibales have highest priority, so python looks for local variable 'num' which is referenced before the declaration. Hence, the error.
    num = 400


# func1()
# print(f"num: {num}, Type: {type(num)}")
# -------------------------------------------

num = 100


# print(f"num: {num}, Type: {type(num)}")


def func1():
    global num
    num = 400
    print("Inside func1")
    print(f"num: {num}, Type: {type(num)}")


# func1()
# print(f"num: {num}, Type: {type(num)}")

# -------------------------------------------
# FUNCTION ALIAS
# -------------------------------------------

def square(num):
    return num ** 2


# print(square(4))

a = square


# print(f"Value of a: {a}, type of a: {type(a)}")
# print(f"Square of 4 using function a: {a(4)}")

# ----------------------------------------------

def pow(num, raise_to):
    return num ** raise_to


# print(pow(4,2))

a = pow
# print(f"Value of a: {a}, type of a: {type(a)}")

num = 4;
raise_to = 3
# print(f"{num} raise to {raise_to} using function pow function: {a(num, raise_to)}")

# ----------------------------------------------
# LAMBDA/ANONYMOUS/UNNAMED Function: expression should include some return value
# ----------------------------------------------

a = lambda num: num ** 2
# print(f"Value of a: {a}, type of a: {type(a)}")
# print(f"Square of 4 using function a: {a(4)}")

b = lambda num, raise_to=3: num ** raise_to
# print(f"Value of b: {b}, type of b: {type(b)}")
# print(f"4 raise to 3 using function b: {b(4)}")
# print(f"4 raise to 4 using function b: {b(4,4)}")

# print((lambda num, raise_to=3: num ** raise_to)(2,2))

