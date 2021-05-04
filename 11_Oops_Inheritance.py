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


# run()

# --------------------------------------------------------------------------------------------------
""" 
Protected Members - Base class members are accessible in Derived Class.

Inheritance Types: Single, Multilevel, Hierarchical, Multiple, and Hybrid
"""


# --------------------------------------------------------------------------------------------------
# Protected Members and Single Inheritance + Composition example
class Address:
    def __init__(self, city, state, country):
        self.__city = city
        self.__state = state
        self.__country = country

    def print_address(self):
        print(f"City: {self.__city}")
        print(f"State: {self.__state}")
        print(f"Country: {self.__country}")


class Person:
    def __init__(self, name, age, city, state, country):
        self._name = name
        self._age = age
        self._address = Address(city, state, country)


class Employee(Person):
    def __init__(self, empid, name, age, city, state, email, country='India'):
        Person.__init__(self, name, age, city, state, country)
        self.__empid = empid
        self.__email = email

    def print_employee(self):
        print(f"Employee Id: {self.__empid}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        self._address.print_address()
        print(f"Email: {self.__email}")
        print('--' * 40)


def run():
    manoj = Employee(1, 'Manoj Pal', 29, 'Mumbai', 'Maharashtra', 'manojpal@ubs.com', 'India')
    safa = Employee(2, 'Safrin Patil', 29, 'Wai', 'Maharashtra', 'safrinpatil@gmail.com', 'India')

    manoj.print_employee()
    safa.print_employee()


# run()

# --------------------------------------------------------------------------------------------------
# Multilevel Example: Person > Employee > SalesManager > RegionManager

class Address:
    def __init__(self, city, state, country):
        self.__city = city
        self.__state = state
        self.__country = country

    def print_address(self):
        print(f"City: {self.__city}")
        print(f"State: {self.__state}")
        print(f"Country: {self.__country}")


class Person:
    def __init__(self, name, age, city, state, country):
        self._name = name
        self._age = age
        self._address = Address(city, state, country)


class Employee(Person):
    def __init__(self, empid, name, age, city, state, email, country):
        Person.__init__(self, name, age, city, state, country)
        self._empid = empid
        self._email = email

    def _print_employee(self):
        print(f"Employee Id: {self._empid}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        self._address.print_address()
        print(f"Email: {self._email}")


class SalesManager(Employee):
    def __init__(self, empid, name, age, city, state, email, department, country='India'):
        Employee.__init__(self, empid, name, age, city, state, email, country)
        self._department = department

    def _print_manager(self):
        Employee._print_employee(self)
        print(f"Department: {self._department}")


class RegionManager(SalesManager):
    def __init__(self, empid, name, age, city, state, email, department, region, country='India'):
        SalesManager.__init__(self, empid, name, age, city, state, email, department, country='India')
        self.__region = region

    def print_regionmanager(self):
        print('--' * 40)
        SalesManager._print_manager(self)
        print(f"Region: {self.__region}")
        print('--' * 40)


def run():
    esha = RegionManager(3, 'Esha Pal', 3, 'Pune', 'Maharashtra', 'eshapal@gmail.com', 'Sales', 'US', country='India')

    esha.print_regionmanager()


# run()

# ------------------------------------------------------------
# Multiple Inheritance : Multiple Base Class - Single Derived Class
# ------------------------------------------------------------

class Batsman:
    def __init__(self, name, bat_hand):
        self._name = name
        self._bat_hand = bat_hand


class Bowler:
    def __init__(self, name, bowl_hand):
        self._name = name
        self._bowl_hand = bowl_hand


class AllRounder(Batsman, Bowler):
    def __init__(self, name, bat_hand, bowl_hand, ):
        Batsman.__init__(self, name, bat_hand)
        Bowler.__init__(self, name, bowl_hand)

    def print_info(self):
        print(f"Name: {self._name}")
        print(f"Bat Hand: {self._bat_hand}")
        print(f"Bowl Hand: {self._bowl_hand}")
        print('--' * 40)


def run():
    yuvyraj = AllRounder('Yuvraj Singh', 'Left', 'Left')
    pandya = AllRounder('Hardik Pandya', 'Right', 'Right')
    jadeja = AllRounder('RavindraSinh Jadega', 'Left', 'Left')
    raina = AllRounder('Suresh Raina', 'Left', 'Right')
    ganguly = AllRounder('Saurav Ganguly', 'Left', 'Right')

    yuvyraj.print_info()
    pandya.print_info()
    jadeja.print_info()
    raina.print_info()
    ganguly.print_info()


# run()


# ------------------------------------------------------------
# Hierarchical Inheritance :  Single Base Class --> Multiple  Derived Class
# Hybrid Inheritance: Mixture of 2 or more inheritance types
# ------------------------------------------------------------