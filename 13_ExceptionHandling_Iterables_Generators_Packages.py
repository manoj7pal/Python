# ------------------------------------------------------------------
"""
Exception Handling - using try and except block
    try --> expression to be tested for any exceptions
    except --> handling the exception occurred in above expression or in try block, gracefully.
    else --> OPTIONAL block, set of expressions to be executed after the expression(try block) is evaluated successfully, without any exceptions
    finally --> OPTIONAL block, used for resource closing. This block will be executed irrespective whether an exception occurs or not.

User Defined Exceptions:
    1. We have to create a new Class which is inherited from 'Exception' class
    2. And, use raise keyword along with the object of above created class, to throw an User defined exception.
"""


# ------------------------------------------------------------------
class InvalidAgeError(Exception):
    pass


class InvalidSalaryError(Exception):
    pass


class Employee:
    def __init__(self, name, age, salary, city):
        self.__name = name
        try:
            if age > 0:
                self.__age = age
            else:
                raise InvalidAgeError
            if salary > 0:
                self.__salary = salary
            else:
                raise InvalidSalaryError
        except InvalidAgeError:
            print("Invalid Age, it should be greater than zero.")
        except InvalidSalaryError:
            print("Invalid Salary, it should be greater than zero")
        except Exception as e:
            print(f"Some Exception occurred: {e}")
        else:
            self.__city = city
            try:
                print(f"10/0: {10 / 0}")
            except ZeroDivisionError as e:
                print(f"A number cannot be divided by zero: {e}")

        finally:
            print("Finally Block, this block will execute irrespective if any error occurred or not")

    def __str__(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nSalary: {self.__salary}"


def run():
    manoj = Employee('Manoj Pal', 29, -1000, 'Mumbai')
    print('--' * 40)
    esha = Employee('Esha Pal', 3, 10000, 'Pune')
    print(esha)


# run()

# ------------------------------------------------------------------
"""
Iterables:
"""


def run():
    a = [10, 20, 30, 40, 50]
    iterator = iter(a)
    print(f"Iterator: {iterator}, type of Iterator: {type(iterator)}")

    try:
        while True:
            print(next(iterator))
    except StopIteration as e:
        print(f"End of the List Iterable object: {e}")


# run()
# ------------------------------------------------------------------
""" 
User Defined Iterable Object: 
    - To make any object an Iterable object, the class must implement __iter__() and __next__() method
    - __iter__() --> returns an Iterable object
    - __next__() --> returns the next value in the iterable object.
    
    In this example, we will make the School Class an iterable class.
"""


# ------------------------------------------------------------------
class Student:
    def __init__(self, name, rollno):
        self._name = name
        self._rollno = rollno

    def __str__(self):
        return f"Student Name: {self._name}\nStudent RollNo: {self._rollno}\n{('--' * 40)}"


class School:
    def __init__(self, schoolname, city):
        self.__schoolname = schoolname
        self.__city = city
        self.__students = []

    def add_student(self, name, rollno):
        self.__students.append(Student(name, rollno))

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        student = self.__students[self.__index]
        self.__index += 1
        return student

    def __str__(self):
        print(f"School Name: {self.__schoolname}")
        print(f"City: {self.__city}")
        print('--' * 40)
        print("Students Information")
        print('--' * 40)

        iterator = iter(self.__students)
        try:
            while True:
                print(next(iterator))
        except StopIteration:
            pass
        finally:
            print('Please contact for admission purpose!!!')
            print('--' * 40)


def run():
    school = School("St. Anthony's High School", 'Mumbai')
    school.add_student('Manoj Pal', 1)
    school.add_student('Safrin Patil', 2)
    school.add_student('Esha Pal', 3)

    try:
        print(school)
    except:
        pass


# run()

# ------------------------------------------------------------------
# Else with FOR Loop:

def is_prime(value):
    for i in range(2, value):
        if value % i == 0:
            print(f"{value} is NOT a Prime number")
            break
    else:
        print(f"{value} is a Prime number")


def run():
    is_prime(10)
    is_prime(13)


# run()
# ------------------------------------------------------------------
"""
Generators: 
    - A generator is an object which does not store the actual values upon its creations.
    - Instead, the object can be iterated over and the value can be fetched as and when required.
    - Created similarly like List comprehensions, but uses '()' instead of '[]'.
    - A generator is an example of LAZY EVALUATION, as the evaluation of the expression is delayed until its value is required.
    - Similarly like Oracle Views.
    - Helpful while dealing with Large Datasets, as the values are not loaded in the RAM until it is referenced.
    - A GENERATOR FUNCTION is used to create a generator object. 
        a. This function 'YIELDS' a sequence of the values in the form of generator object, instead of returning any value.
        b. The returned object can be iterated over, similarly as an iterator object. 
    - A generator maintains the context/state of the last fetched value, and iterates further as and when called.
    
    - A generator object can be created using 2 ways:
        1. Using Generator Expression
        2. Generator Function 
"""


# ------------------------------------------------------------------
# Common block for iterating generator object
def iterate_over_gen_object(gen_obj):
    try:
        for i in range(5):  # First 5 values
            print(next(gen_obj))
    except StopIteration:
        pass

    print('--' * 30)
    print('Rest of values will be printed by FOR loop')
    print('--' * 30)

    for item in gen_obj:
        print(item)

    print('--' * 30)


# 1. Generator Expression
def run(num):
    result = (i for i in range(num) if i % 2 == 0 and i > 0)
    print('Generator Expression Example')
    print('--' * 30)
    print(f"result = {result}, type of result = {type(result)}")

    iterate_over_gen_object(result)


# run(20)


# --------------------------------------------------

# 2. Generator Function - YIELD a sequence of value
def num_sequence(num):
    i = 0
    while i < num:
        yield i
        i += 1


def run():
    result = num_sequence(20)
    print('Generator Function Example')
    print('--' * 30)
    print(f"result = {result}, type of result = {type(result)}")

    iterate_over_gen_object(result)


# run()

# ------------------------------------------------------------------

# Python Generators for Streaming Data:
# Dataset: https://assets.datacamp.com/production/repositories/464/datasets/2175fef4b3691db03449bbc7ddffb740319c1131/world_ind_pop_data.csv
# Pandas read_csv functions - chunksize - acts like a generator which pumps out dat chunks of specified size.

from pandas import read_csv


def load_dataset():
    # world_bank = read_csv(
    #     'https://assets.datacamp.com/production/repositories/464/datasets/2175fef4b3691db03449bbc7ddffb740319c1131/world_ind_pop_data.csv')
    # print(world_bank.info())
    # print(world_bank.isna().sum())
    # print(world_bank.head())

    for chunks in read_csv(
            'https://assets.datacamp.com/production/repositories/464/datasets/2175fef4b3691db03449bbc7ddffb740319c1131/world_ind_pop_data.csv',
            chunksize=1000):
        print(chunks)


# load_dataset()

