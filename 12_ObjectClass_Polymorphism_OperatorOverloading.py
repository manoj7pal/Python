# --------------------------------------------------------------------------
""" Root Class: object
        Every class in Python is inherited directly or indirectly from Root class i.e 'object'.
"""


# --------------------------------------------------------------------------
class NewPerson(object):
    def __init__(self, name, age, city):
        self._name = name
        self._age = age
        self._city = city


class Person:
    def __init__(self, name, age, city):
        self._name = name
        self._age = age
        self._city = city


class Employee(Person):
    def __init__(self, empid, name, age, city):
        Person.__init__(self, name, age, city)
        self.__empid = empid


def run():
    print(f"Employee Base Class: {Employee.__base__}")
    print('--' * 40)
    print(f"Person Base Class: {Person.__base__}")
    print('--' * 40)
    print(f"NewPerson Base Class: {Person.__base__}")


# run()
# --------------------------------------------------------------------------
""" 
Polymorphism: 
    a. Early Binding or Static Resolution or Compile Time Polymorphism
        - Achieved via Method Overloading
        - Not possible, as data types are inferred automatically in Python.
        - Also, we have Default Arguments and Variable Length arguments in method definition.
        
    b. Late Binding or Dynamic Resolution or RunTime Polymorphism
        - Achieved via Method Over-riding and inheritance
        - Possible, derived class methods have first preference, if not found then it searches in Base Class until it founds in ROOT Class. 
            This phenomenon of dynamically resolving the method name is called DYNAMIC RESOLUTION, which is possible in Runtime Polymorphism only.
    
"""


# --------------------------------------------------------------------------
# Method Overriding

class Person:
    def __init__(self, name, age, city):
        self._name = name
        self._age = age
        self._city = city

    def print_info(self):
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"City:{self._city}")


class Student(Person):
    def __init__(self, name, age, city, rollno, marks):
        Person.__init__(self, name, age, city)
        self.__rollno = rollno
        self.__marks = marks

    def print_info(self):
        Person.print_info(self)
        print(f"Roll No: {self.__rollno}")
        print(f"Marks: {self.__marks}")


def run1():
    person1 = Person('Manoj', 29, 'Mumbai')
    person1.print_info()
    print('--' * 40)
    student1 = Student('Esha', 3, 'Pune', 10, 89)
    student1.print_info()

    print('--' * 40)


# run1()

def run2():
    print('--' * 40)
    print('print() --> returns different output for primitive and non-primitve datypes. \n'
          '\t\tTherefore, to standardize the return value of them, we have to override the __str__() method for non-primitive types.')
    print('--' * 40)
    num1 = 100;
    num2 = 200
    print(num1);
    print(num1.__str__())

    print(num2)
    print(num2.__str__())

    print('--' * 40)
    person1 = Person('Manoj', 29, 'Mumbai')
    student1 = Student('Esha', 3, 'Pune', 10, 89)

    print(person1)
    print(person1.__str__())

    print(student1)
    print(student1.__str__())


# run2()

class NewPerson:
    def __init__(self, name, age, city):
        self._name = name
        self._age = age
        self._city = city

    def __str__(self):
        return f" Name: {self._name}\n Age: {self._age}\n City:{self._city}"


class NewStudent(Person):
    def __init__(self, name, age, city, rollno, marks):
        Person.__init__(self, name, age, city)
        self.__rollno = rollno
        self.__marks = marks

    def __str__(self):
        return f"{NewPerson.__str__(self)}\n Roll No: {self.__rollno}\n Marks: {self.__marks}"


def run3():
    print('--' * 40)
    print('After overriding __str__() method')
    print('--' * 40)

    person2 = NewPerson('Manoj', 29, 'Mumbai')
    print(person2)
    print('--' * 40)
    student2 = NewStudent('Esha', 3, 'Pune', 10, 89)
    print(student2)


# run3()
# --------------------------------------------------------------------------
# Operator Overloading

"""
== --> __eq__       
!= --> __ne__
> --> __gt__
>= --> __ge__
< --> __lt__
<= --> __le__

+ --> __add__
- --> __sub__
* --> __mul__
/ --> __truediv__
// --> __floordiv__
** --> __pow__
% --> __mod__

We have to explicitly implement/override above methods like __eq__(), as it is not part of the reference/non-primitve type, else it says 'NotImplemented' when called.
This method is called implicitly when we use the above operators.

"""


# --------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __eq__(self, other):
        return self._name == other._name and self._age == other._age

    def __gt__(self, other):
        return self._age > other._age


class Number:
    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        return self.__value == other.__value


def run():
    num1 = 10
    num2 = 10
    print(num1, num2)  # Value Type/ Primitive DataType
    print(f"num1 == num2: {num1 == num2}")
    print(f"num1.__eq__(num2): {num1.__eq__(num2)}")

    print('--' * 40)

    num1 = Number(10)
    num2 = Number(10)
    print(num1, num2)  # Reference Type/ Non-Primitive Data Type
    print(f"num1 == num2: {num1 == num2}")
    print(f"num1.__eq__(num2): {num1.__eq__(num2)}")

    print('--' * 40)

    person1 = Person('Manoj', 29)
    person2 = Person('Manoj', 29)
    person3 = Person('Esha', 3)

    print(person1, person2)  # Reference Type/ Non-Primitive Data Type
    print(f"person1 == person2: {person1 == person2}")
    print(f"person1.__eq__(person2): {person1.__eq__(person2)}")

    print(f"person1 > person3: {person1 > person3}")

# run
