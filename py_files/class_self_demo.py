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