class Person:
    """This is a Class Doc String"""
    pass


def class_run():
    person1 = Person()

    # Common class/object dunder methods/properties
    print(f"person1: {person1}, class of person1: {person1.__class__}, and type of person1: {type(person1)}")
    print(f"person1.__class__ == type(person1): {person1.__class__ == type(person1)}")
    print(f"Person.__doc__: {Person.__doc__}, person1.__doc__: {person1.__doc__}")
    print(f"Person.__dict__: {Person.__dict__}")
    print('--' * 40)

    # Setting/Adding properties to an Object
    setattr(person1, "name", "Manoj Pal")
    setattr(person1, "age", 29)
    setattr(person1, "city", "Tampa")

    person2 = Person()
    setattr(person2, "name", "Safrin Patil")
    setattr(person2, "age", 29)
    setattr(person2, "city", "Pune")

    # Accessing Object properties
    print(f"Person1 Info: {person1.__dict__}")
    print(f"Person2 Info: {person2.__dict__}")
    print()
    print(f"Person1 Name: {getattr(person1, 'name')}")
    print(f"Person1 Age: {getattr(person1, 'age')}")
    print(f"Person1 City: {getattr(person1, 'city')}")
    print()
    print(f"Person2 Name: {getattr(person2, 'name')}")
    print(f"Person2 Age: {getattr(person2, 'age')}")
    print(f"Person2 City: {getattr(person2, 'city')}")


# class_run()

class Person:


    def __init__(self, name = 'Esha Pal', age = 3, city = 'Pune'):
        self.name = name
        self.age = age
        self.city = city

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print('--' * 40)


manoj = Person('Manoj Pal', 29, 'Mumbai')
safrin = Person('Safrin Patil', 29, 'Wai')
esha = Person()

manoj.print_info()
safrin.print_info()
esha.print_info()
