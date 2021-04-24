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
    # Initializer
    def __init__(self, name='Esha Pal', age=3, city='Pune'):
        self.name = name
        self.age = age
        self.city = city
        return None

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print('--' * 40)


def run():
    manoj = Person('Manoj Pal', 29, 'Mumbai')
    safrin = Person('Safrin Patil', 29, 'Wai')
    esha = Person()

    manoj.print_info()
    safrin.print_info()
    esha.print_info()


# run()


# ---------------------------------------------------------------------------------
"""
Primtive DataTypes --> Pass/Return by Value
Non-Primtive DataTypes --> Pass/Return by Reference
"""


class Number:
    def __init__(self, value):
        self.value = value

    def print_value(self, objname):
        print(f"{objname} value: {self.value}")

    def change_value(self, value):
        self.value = value


num1 = Number(100)
print(f"num1: {num1}")
num1.print_value('num1')

num2 = num1
print(f"num2: {num2}")
num2.print_value('num2')
print()
num1.change_value(200)
print("After changing num1 value to 200")
num1.print_value('num1')
num2.print_value('num2')

print(f"num1 is num2: {num1 is num2}")

print('--' * 30)

# Primitive Datatype
num3 = 300
print(f"num3: {num3}")

num4 = num3
print(f"num4: {num4}")
print()
num3 = 400
print("After changing num3 value to 400")
print(f"num3: {num3}")
print(f"num4: {num4}")

print(f"num3 is num4: {num3 is num4}")
print()

print(
    f"Conclusion: Primitive datatype(latter) is called/passed by value hence it creates a separate object for the new variable, when the original variable value is changed,\n \t \t    which is not observed in the Non-Primitve DataTypes(former) where the new variable value changes with the original value. ")
