# Access Specifiers

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
By default, all the memebers of the class are PUBLIC. 
Hence, we can change the state of the class from outside the class scope with the help of the object.

So, to maintain the security of the class members, we can make them PRIVATE using '__'. e.g: self.__name
"""


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

    safrin.__name = 'Safa'  # this creates a new member, outside class scope
    safrin.city = 'Pune'
    print(f"safrin.__name: {safrin.__name}")
    print(f"safrin.__dict__: {safrin.__dict__}")
    safrin.print_info()


run()
