# class Person:
#     def __init__(self, name, age):
#         self.__name = name;
#         self.__age = age;
#     property
#     def get_age(self):
#         return self.__age
 
#     def setAge(self, age):
#         if 0 < age < 120:
#             self.__age = age
#         else:
#             print("Недопустимое значение")

#     def print(self):
#         print(f"{self.__name},{self.__age}")

# object = Person("Арсений", 70)
# object.print()
# object.setAge(16)
# object.print()

# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height

#     @property
#     def width(self):
#         return self.__width

#     @width.setter
#     def width(self, value):
#         if 0 < value < 120:
#             self.__width = value
#         else:
#             print("Недопустимое значение для ширины")

#     @property
#     def height(self):
#         return self.__height

#     @height.setter
#     def height(self, value):
#         if 0 < value < 120:
#             self.__height = value
#         else:
#             print("Недопустимое значение для высоты")

#     def display(self):
#         print(f"Ширина: {self.__width}, Высота: {self.__height}")

# obj = Rectangle("Площадь", 20)  
# obj.display()
# obj.height = 4
# obj.width = 5
# obj.display()