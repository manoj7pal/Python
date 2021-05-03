# Inheritance

class Person:
    def __init__(self):
        self.name = "Manoj Pal"
        self.age = 29


class Employee(Person):
    pass


def run():
    p = Person()
    print(f"p = {p.__dict__}")

    e = Employee()
    print(f"e  = {e.__dict__}")


# run()

# -------------------------------------------------------------------

class Person:
    def __init__(self):
        self.name = "Manoj Pal"
        self.age = 29


class Employee(Person):
    def __init__(self):
        Person.__init__(self)
        self.empid = 1


def run():
    p = Person()
    print(f"p = {p.__dict__}")

    e = Employee()
    print(f"e  = {e.__dict__}")


# run()

"""
By default, python calls the Base Class Initializer in the derived class initializer.
So to extend the properties of the Base class in Derived Class, we should explicitly call the Base Class Initializer first, 
    in the Derived Class Initializer else the parent object will not be created. 
"""


# Example of Association(using Address Class) and Inheritance

class Address:
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

    def print_address(self):
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Country: {self.country}")


class Person:
    def __init__(self, name, age, city, state, country):
        self.name = name
        self.age = age
        self.address = Address(city, state, country)

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        self.address.print_address()


class Employee(Person):
    def __init__(self, empid, name, age, email, city, state, country='India'):
        Person.__init__(self, name, age, city, state, country)
        self.empid = empid
        self.email = email

    def print_info(self):
        print(f"Emp ID: {self.empid}")
        Person.print_info(self)
        print(f"Email: {self.email}")
        print('--' * 40)


def run():
    manoj = Employee(1, 'Manoj Pal', 29, 'manojpal@tsys.com', 'Pune', "Maharashtra")
    manoj.print_info()

    safa = Employee(2, 'Safrin Patil', 29, 'safrinpatil@gmail.com', 'Pune', 'Maharashtra')
    safa.print_info()


run()
