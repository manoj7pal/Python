def func1():
    a = [1]
    print(f"a: {a}, type of a: {type(a)}")

    # Int
    a = (1)
    print(f"a: {a}, type of a: {type(a)}")

    # Tuple - To create a tuple with one item,
    # it is mandatory to put ',' at the end else, it will be considered as primitive data type.
    a = (1,)
    print(f"a: {a}, type of a: {type(a)}")


# func1()

def function2():
    a = (1, 2, 3, 4, 5)
    print(f"a: {a}, type of a: {type(a)}")

    # Tuple unpacking - if each element is a Tuple
    persons = [('Manoj Pal', 28), ('Safrin Patil', 28)]
    for (name, age) in persons:
        print(f"Name: {name}, and age is {age} years old.")

    # Set
    a = {10, 100, 1, 1, 4, 2, 3, 3, 2, 3, 4, 3, 1, 2, 4}
    print(f"a: {a}, type of a: {type(a)}")

    a.add(50)
    a.add(50)
    print(f"a: {a}, type of a: {type(a)}")

    b = a.copy()
    a.add(55)
    print(f"a: {a}, type of a: {type(a)}")
    print(f"b: {b}, type of b: {type(b)}")

    # Operations
    a = {1, 2, 3, 4, 5, 2, 1}
    b = {3, 3, 4, 4, 5, 6, 7}

    print(f"a union b: {a.union(b)}")
    print(f"a intersection b: {a.intersection(b)}")
    print(f"a minus b: {a.difference(b)}")
    print(f"b minus a: {b.difference(a)}")

    frz_a = frozenset(a)
    print(f"frz_a: {frz_a}, type of frz_a: {type(frz_a)}")

    # IMMUTABLE : so below statement throws ERROR
    # frz_a.add(10)


function2()

# DICTIONARY
