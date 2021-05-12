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
# ------------------------------------------------------------------
