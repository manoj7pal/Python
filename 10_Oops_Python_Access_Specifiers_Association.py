# Access Specifiers

# Public
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print("--" * 40)


def run():
    safrin = Person('Safrin Patil', 29, 'Wai')
    safrin.print_info()

    safrin.name = 'Safa'
    safrin.print_info()


# run()

"""
By default, all the members of the class are PUBLIC. 
Hence, we can change the state of the class from outside the class scope with the help of the object.

So, to maintain the security of the class members, we can make them PRIVATE using '__'. e.g: self.__name
"""


# PRIVATE
class Person:
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.city = city  # Public, hence it can be changed outside class scope.

    def print_info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"City: {self.city}")
        print("--" * 40)


def run():
    safrin = Person('Safrin Patil', 29, 'Wai')
    print(f"safrin.__dict__: {safrin.__dict__}")
    safrin.print_info()

    safrin.__name = 'Safa'  # this creates a new member, outside class scope --> Public scope
    safrin.city = 'Pune'
    print(f"safrin.__name: {safrin.__name}")
    print(f"safrin.__dict__: {safrin.__dict__}")
    safrin.print_info()


# run()

# ------------------------------------------------------------
"""
Method Types:
    1. Initializer
    2. Mutator(Setter)
    3. Inspector(Getter)
    4. Facilitator
    5. De-initializer: This method gets called automatically. In order to call this explicitly use 'del <object_name>'. e.g: del <object_name>
"""


class Person:
    # 1. Initializer
    def __init__(self, name, age, city):
        print("Inside Initializer")
        self.__name = name
        self.__age = age
        self.__city = city

    # 2. Mutator
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_city(self, city):
        self.__city = city

    # 3. Inspector
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_city(self):
        return self.__city

    # 4. Facilitator
    def print_info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"City: {self.__city}")
        print("--" * 40)

    # 5. Deinitialilzer
    # def __del__(self):
    #     """This method gets called automatically. In order to call this explicitly use 'del <object_name>'. e.g: del safrin"""
    #     print("Inside De-Initializer")


def run():
    safrin = Person('Safrin Patil', 28, 'Wai')
    print(f"Name: {safrin.get_name()}")
    print(f"Age: {safrin.get_age()}")
    print(f"City: {safrin.get_city()}")
    print('--' * 40)

    safrin.set_name('Safrin Manoj Pal')
    safrin.set_age(29)
    safrin.set_city('Pune')

    print(f"Name: {safrin.get_name()}")
    print(f"Age: {safrin.get_age()}")
    print(f"City: {safrin.get_city()}")


# run()

# ----------------------------------------------------------------------

"""
Association: 
    1. One of the ways to make your Code Modular(Reusable.), other one is Inheritance.
    2. has-a relationship. e.g: Person has-a Address, House has-a Address, Humans has-a heart, Animals has-a heart etc.
    3. 2 Types: 
        a. Aggregation: Weak Relationship, Independent entities involved
            e.g: Organization has-a Employee => In this case, a organization can exist without one employee.
        b. Composition: Strong Relationship, Dependent entities involved, can also be used for COMPOSED_OF relationship.
            e.g: Humans has-a brain/heart etc.

"""


class Address:
    def __init__(self, city, state, country):
        self.__city = city
        self.__state = state
        self.__country = country

    def print_info(self):
        print(f"City: {self.__city}")
        print(f"State: {self.__state}")
        print(f"Country: {self.__country}")
        print("--" * 40)


class Person:
    def __init__(self, name, city, state, country):
        self.__name = name
        self.__address = Address(city, state, country)

    def print_info(self):
        print('Person Information: ')
        print(f"Name: {self.__name}")
        self.__address.print_info()

    def __del__(self):
        del self.__address


class House:
    def __init__(self, name, city, state, country):
        self.__name = name
        self.__address = Address(city, state, country)

    def print_info(self):
        print('House Information: ')
        print(f"Name: {self.__name}")
        self.__address.print_info()

    def __del__(self):
        del self.__address


def run():
    safrin = Person('Safrin Patil', 'Pune', 'MH', 'India')
    safrin_native = House('Harihareshwar Complex', 'Wai', 'MH', 'India')

    safrin.print_info()
    safrin_native.print_info()


run()
