import numpy as np
import sys

# List
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]


def run1():
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"List: a + b = {a + b}")

    # Numpy Array
    np_a = np.array(a)
    np_b = np.array(b)

    print(f"Numpy: a + b = {np_a + np_b}")

    # Numpy Arrays are MUTABLE Collection
    print(f"np_a[0]: {np_a[0]}")
    np_a[0] = 10
    print(f"np_a: {np_a}")

    a = [1, 2, 3, 4, 5]
    np_a = np.array(a)

    # List Memory Allocation
    for i in a:
        print(f"value: {i}, type of value: {type(i)}, and Size of each element: {sys.getsizeof(i)} bits.")
    print()

    # NUMPY has its own implementation for the primitive datatype i.e for int --> int8, int16, int64 and etc.
    for i in np_a:
        print(f"value: {i}, type of value: {type(i)}, and Size of each element: {sys.getsizeof(i)} bits.")
    print(f"Size of each element: {np_a.itemsize} bytes.")

    # While creating a numpy ARRAY, we can define the dataytype of the elements, for efficient storing.
    # In above case, by default numpy assign 32 bits(4byte) for each element, so for entire array = 32 * 5 = 160bits (40 bytes)

    print()
    np_a = np.array(a, dtype='int8')  # 8bits(1 byte) per element
    for i in np_a:
        print(f"value: {i}, type of value: {type(i)}, and Size of each element: {sys.getsizeof(i)} bits.")
    print(f"Size of each element: {np_a.itemsize} byte.")

    print()
    np_a = np.array(a, dtype='int64')  # 8bits(1 byte) per element
    for i in np_a:
        print(f"value: {i}, type of value: {type(i)}, and Size of each element: {sys.getsizeof(i)} bits.")
    print(f"Size of each element: {np_a.itemsize} byte.")


# run1()

# Element wise Operations
def run2():
    # Numpy Array
    np_a = np.array(a)
    np_b = np.array(b)

    print(f"np_a + np_b: {np_a + np_b}")
    print(f"np_a * np_b: {np_a * np_b}")
    print(f"np_a / np_b: {np_a / np_b}")
    print(f"np_a // np_b: {np_a // np_b}")
    print(f"np_a - np_b: {np_a - np_b}")


# run2()


def run3():
    np_zeros = np.zeros(shape=[3, 2])
    np_ones = np.ones(shape=[3, 3])

    print(f"np.zeros: {np_zeros}")
    print(f"np.ones: {np_ones}")


# run3()

# Processing time Comparison - Lists and Numpy Arraya
import time


def run4():
    count = 10000000

    print('List')
    print('--' * 30)
    a = list(range(count))
    b = list(range(count))
    c = []

    t1 = time.time()
    for index in range(count):
        c.append(a[index] + b[index])
    t2 = time.time()

    print(f'Processing time: {t2 - t1}')

    print('--' * 30)
    print('Numpy Array')
    print('--' * 30)

    np_a = np.arange(count)
    np_b = np.arange(count)

    t1 = time.time()
    np_c = np_a + np_b
    t2 = time.time()

    print(f'Processing time: {t2 - t1}')


# run4()


# Filtering

def run5():
    emp_salary = np.array([1000, 2000, 5000, 300, 4000, 9000, 15000, 13000, 25000, 20000])
    print(f'emp_salary: {emp_salary}')
    print()

    print(f"Emp Salary greater than 10000: {emp_salary > 10000}")
    print(f"emp_salary[emp_salary > 10000]: {emp_salary[emp_salary > 10000]}")

    emp_salary_less_than_10000 = emp_salary < 10000
    print(f"Emp Salary less than 10000: {emp_salary[emp_salary_less_than_10000]}")

    print(f"Emp salary data - reshape(2,5): {emp_salary.reshape([2, 5])}")
    print(f"Sorted Emp Salary: {np.sort(emp_salary)}")


run5()
