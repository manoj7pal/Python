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
