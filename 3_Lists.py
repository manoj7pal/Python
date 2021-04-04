# Python Collection

def func1():
    a = [1, 2, 3, 4, 5]
    print(f"a: {a}, Type of a: {type(a)}")

    for i in a:
        print(f"Value: {i}, Type of {i} is {type(i)}")
    print('--' * 20)
    for index, value in enumerate(a):
        print(f"Value at {index} position: {value}")


# func1()

def func2():
    a = list(range(0, 5))
    print(f"Value of a: {a}, type of a: {type(a)}")


# func2()

def func3():
    a = ["India", 'USA', 1, True, int(False)]
    print(f"Value of a: {a}, type of a: {type(a)}")

    for i in range(len(a)):
        print(f"Item: {a[i]}, type of {a[i]}: {type(a[i])}")


# func3()

# -----------------------------------
# List Operations -
# -----------------------------------
a = list(range(10, 110, 10))
print(a)


def list_operations():
    # List Length
    print(f"Length of the list a: {len(a)}")

    # append() method: Add a value to the list - it will be added at the end of the list
    a.append(120)
    print(f"After appending 120, a: {a}")

    # pop() method: Remove the last value of the list
    del_value = a.pop()
    print(f"After deleting the last value, a: {a}")
    print(f"Deleted value: {del_value}")

    # insert(): insert a value in between
    a.insert(10, 120)
    print(f"After adding 120 at 11th position, a: {a}")
    a.insert(2, 25)
    print(f"After adding 25 at 3rd position, a: {a}")

    # pop(): Delete Value in Between
    del_value = a.pop()
    print(f"Deleted value: {del_value}")
    del_value = a.pop(2)
    print(f"Deleted value: {del_value}")
    print(f"After deleting the above values, a: {a}")

    # Count the occurrences of a list item
    a.append(10)
    a.append(10)
    print(a)
    print(f"Occurrences of number 10 in the list a: {a.count(10)}")

    # Index of a list item
    print(a)
    print(f"Index of number 10 in list a: {a.index(10)}")  # First Occurrence
    print(f"Index of number 10 in list a: {a.index(10, 5)}")  # Search from 5th position
    print(f"Index of number 10 in list a: {a.index(10, 11)}")  # Search from 11th position

    occurrences = []
    count = a.count(10)
    start = 0

    for i in range(count):
        idx_10 = a.index(10, start)
        occurrences.append(idx_10)
        start = idx_10 + 1

    print(f"Occurrences of number 10 in list a: {occurrences}")

    # Sorting - Asc and desc

    b = [24, 53, 2, 32, 1, 0, 41, 23, 19, 54]
    print(f"b: {b}")

    # Asc sort
    b.sort()
    print(f"Ascending Sort, b:{b}")

    # Desc sort
    b.sort(reverse=True)
    print(f"Descending Sort, b:{b}")

    # Reverse a list
    b = [24, 53, 2, 32, 1, 0, 41, 23, 19, 54]

    print(f"List before reverse: {b}")
    b.reverse()
    print(f"List after reverse: {b}")

    # Explicit - Copy of list
    b = [24, 53, 2, 32, 1, 0, 41, 23, 19, 54]
    c = b  # Reference Copy
    b.append(1000)
    print(f"List c after appending 1000 in b: {c}")

    b = [24, 53, 2, 32, 1, 0, 41, 23, 19, 54]
    d = b.copy()  # Explicit Copy
    b.append(1000)
    print(f"List d after appending 1000 in b: {d}")

    # Deleting a value by Element Value

    countries = ['India', 'USA', 'China', 'Japan']

    print(countries)
    # idx_china = countries.index('China')
    # countries.pop(idx_china)
    # print(countries)

    # OR

    countries.remove('China')  # Throws Exception, if values is not present
    print(countries)

    # countries.pop(countries.index('China'))  # Does not throws Exception, if values is not present
    # print(countries)

    # Reset/Clear all values in the list
    countries.clear()
    print(f"After clearing the list: {countries}")


list_operations()
