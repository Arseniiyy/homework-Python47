# class Student:
#     def __init__(self, name, age, grades=None):
#         self.name = name
#         self.age = age
#         self.grades = grades if grades is not None else []

#     def add_grade(self,grade):
#         self.grades

#     def get_average(self):
#         if not self.grades:
#             return  None
#         return sum(self.grades)

# student1 = Student("Арсений", 30, [4, 5, 3])
# print(f"Имя: {student1.name}")
# print(f"Возраст: {student1.age}")
# print(f"Оценки: {student1.grades}")

# Обьяснение:
# Мы создаем класс Student, который моделирует с тремя атрибутами(name,age,grades).
# Метод init:
# он принимает три параметра:
# name
# age
# grades
# Если при создании обьекта передан список оценок, он присваивается атрибуту self.None
# Если оценки не переданы  то создается пустой список.
