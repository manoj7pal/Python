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
num = 100
print(f"global num: {num}")
print('--' * 30)


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


outer()
print(f"global num: {num}")
print('--' * 30)


