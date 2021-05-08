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


run()

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
