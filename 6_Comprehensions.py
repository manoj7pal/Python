# 1. List Comprehensions

print('--' * 40)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")
print('--' * 40)


def square():
    squares = []
    for i in numbers:
        squares.append(i ** 2)

    print(f"Squares - Traditional way: {squares}")
    print('--' * 40)

    squares = list(map(lambda x: x ** 2, numbers))
    print(f"Squares - Map Function: {squares}")
    print('--' * 40)

    squares = [i ** 2 for i in numbers]
    print(f"Squares - List Comprehension: {squares}")
    print('--' * 40)

    even_squares = [i ** 2 for i in numbers if i % 2 == 0]
    print(f"Even Squares - List Comprehension: {even_squares}")
    print('--' * 40)

    odd_squares = [i ** 2 for i in numbers if i % 2 != 0]
    print(f"Odd Squares - List Comprehension: {odd_squares}")
    print('--' * 40)


# square()


def square_cube():
    squares_cubes = []
    for i in numbers:
        if i < 6:
            squares_cubes.append(i ** 2)
        else:
            squares_cubes.append(i ** 3)
    print(f"Square & Cube - Traditional Way: {squares_cubes}")
    print('--' * 40)

    squares_cubes = list(map(lambda x: x ** 2 if x < 6 else x ** 3, numbers))
    print(f"Square & Cube - Map Function: {squares_cubes}")
    print('--' * 40)

    # [ <evaluation expression> for in <collection> <filter expression> ]
    squares_cube = [i ** 2 if i < 6 else i ** 3 for i in numbers]
    print(f"Square & Cube - List Comprehension: {squares_cubes}")
    print('--' * 40)

    num = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Num: {num}")
    odd_cubes_gt0 = [i ** 3 if i > 0 else -9999 for i in num if i % 2 != 0]
    print(f"Odd Cube, gt 0 - List Comprehension: {odd_cubes_gt0}")
    print('--' * 40)

    print('**' * 40)
    result = []
    for i in num:
        if i % 2 != 0:
            if i > 0:
                result.append(i ** 3)
            else:
                result.append(-9999)
    print(f"Result: {result}")
    print('**' * 40)


# square_cube()

# -----------------------------------------------------------
# Dictionary Comprehensions
# -----------------------------------------------------------

def func1():
    num_sq = {num: num ** 2 for num in range(11) if num > 0}
    even_sq = {num: num ** 2 for num in range(11) if num % 2 == 0 and num > 0}
    odd_sq = {num: num ** 2 for num in range(11) if num % 2 != 0}

    print(f"num_sq: {num_sq}, and type of num_sq = {type(num_sq)}")
    print(f"even_sq: {even_sq}, and type of even_sq = {type(even_sq)}")
    print(f"odd_sq: {odd_sq}, and type of odd_sq = {type(odd_sq)}")


func1()
