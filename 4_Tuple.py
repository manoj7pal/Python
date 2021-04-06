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


func1()
