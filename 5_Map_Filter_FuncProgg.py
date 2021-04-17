def func():
    nums = [1, 2, 3, 4, 5]
    a = list(map(lambda num: num ** 2, nums))
    print(a)


# func()

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def execute(func):
    print(f"Parameter is: {func}, and type of the parameter is {type(func)}")
    print(f"Result: {func(10, 20)}")


# execute(add)
# execute(subtract)
# execute(multiply)
# execute(divide)

# FILTER

def func2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_nos = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers are: {even_nos}")


# func2()


# Squares of Even numbers
def func3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Squares of Even numbers: {list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))}")
    print(f"Cube of Odd numbers: {list(map(lambda x: x ** 3, filter(lambda x: x % 2 != 0, numbers)))}")

    for even_num in filter(lambda x: x % 2 == 0, numbers):
        print(even_num)


# func3()


def func4():
    cars = [
        {'name': 'i20', 'company': 'hyundai', 'price': 7.5, 'year': 2010},
        {'name': 'nano', 'company': 'tata', 'price': 2.5, 'year': 2006},
        {'name': 'laura', 'company': 'skoda', 'price': 17, 'year': 2011},
        {'name': 'x5', 'company': 'bmw', 'price': 40, 'year': 2014},
        {'name': 'gld350', 'company': 'mercedes', 'price': 85, 'year': 2018}
    ]

    car_price = list(map(lambda car: {'car': car['name'], 'price': car['price']}, cars))
    print(car_price)

    affordable_cars = list(map( lambda car: {'car': car['name'], 'price': car['price']},
                                filter(lambda car: car['price'] < 10, cars)))
    print(f"Affordable cars: {affordable_cars}")

    # Model and Company of Non-affordable cars
    print(f"Non-affordable car name and company information: "
          f"{list(map(lambda car: {'car': car['name'], 'company': car['company']}, filter(lambda car: car['price'] > 20, cars)))}")


func4()
