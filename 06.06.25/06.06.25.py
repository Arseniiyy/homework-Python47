# class Counter:
#     count = 0  

#     def __init__(self):
#         Counter.count += 1

# a = Counter()
# b = Counter()
# print(Counter.count)


# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def multiply(a, b):
#         return a * b

#     @staticmethod
#     def factorial(n):
#         result = 1
#         for i in range(1, n+1):
#             result *= i
#         return result
    
# print(MathUtils.add(2, 3))
# print(MathUtils.multiply(4, 5))
# print(MathUtils.factorial(4))


# class User:
#     total_users = 0

#     def __init__(self, name):
#         self.name = name
#         User.total_users += 1

# u1 = User("Егор")
# u2 = User("Костя")
# print(User.total_users)


# задание 2

# class EmptyClass(object):
    # def __str__(self):
        # return "Это пустой класс"
    

# задание 3
# class Book:
    # def __init__(self, title, author, year):
        # self.title = title
        # self.author = author
        # self.year = year

    # def __str__(self):
        # return f"{self.title} by {self.author}, {self.year}"

    # def __repr__(self):
        # return f"Book({self.title}, {self.author}, {self.year})"
    
# задание 4

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)

#     def __mul__(self, other):
#         return self.x * other.x + self.y * other.y
    

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def sravnenie(self, other):
#         return self.area() == other.area()
    


# задание 5

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

#     def perimeter(self):
#         return 4 * self.side
    


# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Гав!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Мяу!"
    


class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class PostgresConnector(DatabaseConnector):
    def connect(self):
        print("Подключение к PostgreSQL")

    def disconnect(self):
        print("Отключение от PostgreSQL")