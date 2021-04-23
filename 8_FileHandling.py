# FILE HANDLING

def function1():
    """
    File Open Mode:
        1. w: write
        2. r: read
        3. a: append
    """

    # Create a file object for writing.
    file = open("./output/myfile.txt", mode='w')

    # Perform file operation
    file.write("This is test statement.")

    # Close the file object
    file.close()


# function1()

# ---------------------------------------------------------------------------

# Logger using File Handling

def logger(func):
    def inner(*args, **kwargs):
        file = open('./output/log.txt', mode='a')

        file.write("In Logger ----- Function Call\n")
        file.write(f"Function: {func}\n")
        file.write(f"Parameters: args=> {args}, kwargs => {kwargs}\n")
        result = func(*args, **kwargs)
        file.write(f"Result: {result}\n")
        file.write("Function Processing finished.\n")
        file.write("--" * 40 + "\n")

        file.close()

    return inner


@logger
def add(a, b):
    result = a + b
    print(f"a+b: {result}")
    return result


@logger
def subtract(a, b):
    result = a - b
    print(f"a-b: {result}")
    return result


@logger
def multiply(a, b):
    result = a * b
    print(f"a*b: {result}")
    return result


@logger
def divide(a, b):
    result = a / b
    print(f"a/b: {result}")
    return result


@logger
def square(a=20):
    result = a ** 2
    print(f"a**2: {result}")
    return result


def run():
    add(10, 20)
    subtract(b=10, a=20)
    multiply(10, b=20)
    divide(10, 20)
    square(a=10)
    square()


# run()

# Reading a File
def read_log(file_name):
    file = open(f'./output/{file_name}.txt', mode='r')
    data = file.read()
    print(data)


# read_log('log')

# --------------------------------------------------------------
def initialize():
    with open('./output/file.csv', 'w') as file:
        file.write('-----------------------------------Function Call--------------------------------------\n')
        file.write("Function, Args, Kwargs, Result, Status\n")


def write_csv(func):
    def inner(*args, **kwargs):
        with open('./output/file.csv', 'a') as file:
            result = func(*args, **kwargs)
            file.write(f"{func.__name__}, {args}, {kwargs}, {result}, Success\n")

    return inner


@write_csv
def add(a, b):
    result = a + b
    print(f"a+b: {result}")
    return result


@write_csv
def subtract(a, b):
    result = a - b
    print(f"a-b: {result}")
    return result


@write_csv
def multiply(a, b):
    result = a * b
    print(f"a*b: {result}")
    return result


@write_csv
def divide(a, b):
    result = a / b
    print(f"a/b: {result}")
    return result


@write_csv
def square(a=20):
    result = a ** 2
    print(f"a**2: {result}")
    return result


def run():
    initialize()

    add(10, 20)
    subtract(b=10, a=20)
    multiply(10, b=20)
    divide(10, 20)
    square(a=10)
    square()


# run()


def read_csv(filename):
    with open(f"./output/{filename}.csv", mode='r') as file:
        print(file.read())


# read_csv('file')
