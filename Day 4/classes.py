# 1. Create a simple class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Usama", 22)
p1.greet()

# 2. Create a class for a Car
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} is now going at {self.speed} km/h")

    def brake(self):
        self.speed -= 5
        print(f"{self.brand} slowed down to {self.speed} km/h")

car1 = Car("Toyota", 50)
car1.accelerate()
car1.brake()

# 3. Store multiple objects in a list
students = [
    Person("Ali", 20),
    Person("Ahmed", 21),
    Person("Sara", 19)
]

for student in students:
    student.greet()

# 4. Using private variables
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print("Balance:", account.get_balance())


# 5. Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class
class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"{self.title} by {self.author}")

b1 = Book("Python Basics", "John")
b1.display()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(5, 3)
print("Area:", r.area())
print("Perimeter:", r.perimeter())

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def has_passed(self):
        return self.marks > 40

s = Student("Usama", 75)
print("Passed?", s.has_passed())

print("\n--- End of OOP Exercises ---")


class TestClass:
    test_var = "Hello"

test = TestClass()
print(test.test_var)    


class TestClass2:
    test_var = 'Something'
    another_var = 'Another'

    def test_function(self):
        print('Function in a class')
        print(self.test_var)

    def another_function(self, test_param):
        print(test_param)

test2 = TestClass2()
test2.test_function()