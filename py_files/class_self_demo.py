class Person:
    def __init__(self, name, age):
        self.name = name # Define an instance variable
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def birthday(self):
        self.age +=1 # Modify an instance variable
        self.greet() # Call another method within the class

# Create an instance of Person
person = Person("Alice", 30)
person.greet() # Outputs: Hello, my name is Alice and I am 30 years old.
person.birthday() # Updates age and outputs the greeting with the new age.

class Car:
    def __init__(self, model):
        self.model = model # Instance variable
        self.is_running = False # Instance variable initialized

    def start(self):
        self.is_running = True # Modify an instance variable
        print(f"The {self.model} is now running.")

    def stop(self):
        self.is_running = False # Modify an instance variable
        print(f"The {self.model} has stopped.")

car = Car("Chevelle")
car.start()
car.stop()

"""
A class can call objects in other instances, for example:
"""

class Driver:
    def __init__(self, name):
        self.name = name
    
    def drive(self, car): # Calling an object from a separate class, `car`
        print(f"{self.name} is driving.")
        car.start()

    def park(self, car):
        print(f"{self.name} has parked.")
        car.stop()

# Create an instance of Car and Driver
my_car = Car("Tesla")
driver = Driver("Alice")

# Driver uses methods of the Car instance
driver.drive(my_car)
driver.park(my_car)

"""
It is possible for methods within a class to operate primarily or exclusively on instances of other classes
and not use the `self` reference to its own attribute methods. This typically occurs in utility or service
classes designed to operate on other objects without maintain any internal state of their own. Such methods
might be static methods or might belong to classes that primarily act as "helpers" or "controllers" for other
objects.

A static method in a class doesn't operate on an instance of the class (`self`) and doesn't modify the class
state. It's marked with a `@staticmethod` decorator, indicating that it does not take the automatic `self`
parameter and thus doesn't access instance-specific data.
"""

# Example of Statis Method Operating on Another Class
class MathOperations:
    @staticmethod
    def add(x, y):
        return x+y
    
"""
`MathOperations` has a static method `add` that takes two numbers and adds them. It does not use or require
a `self` parameter because it does not modify or access any attributes of the `MathOperations` class itself.
The `Calculator` class uses this static method to perform addition.
"""
    
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perform_addition(self):
        return MathOperations.add(self.a, self.b)
    
# Usage
calc = Calculator(5, 3)
print(calc.perform_addition())

"""
Another common design involves classes that manage or control instance of other classes without maintaining
their own state. Such classes might interact with multiple different objects but not store or directly
manipulate data pertaining to their own instances.
"""

class Printer:
    def print_document(self, document):
        print(f"Printing: {document}")

class Office:
    def __init__(self, printer):
        self.printer = printer

    def send_to_printer(self, document):
        self.printer.print_document(document)

# Usage
printer = Printer()
office = Office(printer)
office.send_to_printer("Annual Report")  # Output: Printing: Annual Report

"""
Here, the Office class does not operate on its own data in the method send_to_printer.
It only calls methods on the Printer instance. Although it uses self to access the printer object, the primary operation is done on another class' instance.
"""

class LibraryBook:
    def __init__(self, title, author):
        self.title = title          # Title of the book, provided during instantiation
        self.author = author        # Author of the book, provided during instantiation
        self.loan_period = 14       # Fixed loan period for each book set to 14 days

    def book_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Loan Period: {self.loan_period} days")

    def renew_loan(self):
        print(f"The loan for '{self.title}' has been renewed for another {self.loan_period} days.")

# Example Usage
book1 = LibraryBook("1984", "George Orwell")
book2 = LibraryBook("Brave New World", "Aldous Huxley")

book1.book_details()
book2.book_details()

book1.renew_loan()

"""
In this example, self.loan_period = 14 demonstrates how an instance variable can be set to a fixed value. Every instance of LibraryBook will have
a loan period of 14 days, demonstrating how you can initialize certain attributes with constants that are common across all instances of a class.
"""