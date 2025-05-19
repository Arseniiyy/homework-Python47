# Задание 1
# def summa_paraments(a,b,c,d=0,e=0):
#       return a + b + c + d + e

# def sum(a,b): return a + b 
# print(sum)


# def sum(a,b,c): return a + b + c
# print(sum)

# def sum(a,b,c,d): return a + b + c + d
# print(sum)


# def sum(a,b,c,d,e): return a + b + c + d + e
# print(sum)

# Задание 2
# def even(number):
#     return number % 2 == 0

# print(even(4))
# print(even(9))

# Задание 3
# def apply_function(func, numbers):
#     return [func(num) for num in numbers]

# def is_even(number):
#     return number % 2 == 0

# numbers_list = [1, 2, 3, 4, 5]

# result = apply_function(is_even, numbers_list)
# print(result)  

# def square(x):
#     return x ** 2
# squares = apply_function(square, numbers_list)
# print(squares) 

# Задание 4
# count = 0
# if True:
#     temp = 10
#     count += temp

#     print("Внутри блока",temp)
#     print("Вне блока",count) 
# else:
#     print("Ошибка")

# Задание 5
# def createCounter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count

#     return(counter)

# Newcount = createCounter()

# print(Newcount())
# print(Newcount())
# print(Newcount())

# Задание 6

# def createCounter(step=1):
#     count = 0
#     def counter():
#         nonlocal count
#         count += step
#         return count

#     return counter

# Newcount = createCounter(2)

# print(Newcount())  # 2
# print(Newcount())  # 4
# print(Newcount())  # 6

# Newcount = createCounter(5)

# print(Newcount())  # 5
# print(Newcount())  # 10
# print(Newcount())  # 15