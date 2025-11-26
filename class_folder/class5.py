# Class in Python demonstrating basic class structure and methods
# Why do we need classes in Python?
# Classes are used to create user-defined data structures that encapsulate data and functionality together.
# They help in organizing code, promoting reusability, and implementing object-oriented programming principles.
# Example of a simple class definition:

class Person:
    # The __init__ method is a special method that is automatically called when a new object of the class is created.
    # It is used to initialize the attributes of the class.
    # Is this very time needed to define __init__ method in class?
    # No, it's not strictly necessary, but it's a good practice to define it when you want to initialize object attributes.
    # What is object attributes?
    # Object attributes are variables that belong to an instance of a class. They hold data specific to that instance.
    # Example: In the Person class, name and age are object attributes.
    # How to define object attributes?
    # Object attributes are typically defined within the __init__ method using the self parameter.
    def __init__(self, name, age, phone=None):
        self.name = name
        self.age = age
        self.phone = phone

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. and My phone number is {self.phone}"

    def have_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age} years old."
    
# Creating an instance of the Person class\
person1 = Person("Alice", 30, "123-456-7890")
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(person1.have_birthday())  # Output: Happy birthday Alice! You are now 31 years old.
print(repr(person1))  # Why repr used here?
# The repr() function returns a string representation of the object that is meant to be unambiguous and useful for debugging.
# By default, it shows the memory address of the object, but you can customize it by defining the __repr__ method in your class.
