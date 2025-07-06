# random(): генерирует случайное число от 0.0 до 1.0

# randint(): возвращает случайное число из определенного диапазона

# randrange(): возвращает случайное число из определенного набора чисел

# shuffle(): перемешивает список

# choice(): возвращает случайный элемент списка

# import random

# number = random.random()
# print(number)

# number = random.random() * 100
# print(number)


# number = random.randint(25, 50)
# print(number)


# number = random.randrange(10)
# print(number)
# number = random.randrange(10,50)
# print(number)
# number = random.randrange(10,100,4)
# print(number)

# # randrange(stop): в качестве набора чисел, из которых происходит извлечение случайного значения, будет использоваться диапазон от 0 до числа stop

# # randrange(start, stop): набор чисел представляет диапазон от числа start до числа stop

# # randrange(start, stop, step): набор чисел представляет диапазон от числа start до числа stop, при этом каждое число в диапазоне отличается от предыдущего на шаг step

# number = [4,5,1,3,2,6,7,9]
# random.shuffle(number)
# print(number)
# random_num = random.choice(number)
# print(random_num)



# secrets.choice(seq): возвращает случайно выбранный элемент из непустой последовательности.

# secrets.randbelow(exclusive_upper_bound): возвращает случайное целое число в диапазоне [0, exclusive_upper_bound].

# secrets.randbits(k): возвращает неотрицательное целое число с k случайными битами.

# import secrets
# import string

# parol = string.ascii_letters + string.digits
# password = "".join(secrets.choice(parol) for i in range(8))

# print(password)


# chislo = secrets.randbelow(100)
# print(chislo)

# number = secrets.randbits(7)
# print(number)


# # secrets.token_bytes([nbytes=None]): возвращает случайную строку байтов, содержащую nbytes байтов.
# #  Если nbytes равно None или не указано, используется разумное значение по умолчанию.

# # secrets.token_hex([nbytes=None]): возвращает случайную текстовую строку в шестнадцатеричном формате.
# #  Строка содержит nbytes случайных байтов, каждый байт преобразован в две шестнадцатеричные цифры. Если nbytes равно None или не указано, используется разумное значение по умолчанию.

# # secrets.token_urlsafe([nbytes=None]): возвращает случайную текстовую строку, безопасную для URL, содержащую nbytes случайных байтов.
# #  Текст закодирован в Base64, поэтому в среднем каждый байт дает приблизительно 1,3 символа. Если nbytes равно None или не указано, используется разумное значение по умолчанию.


# token = secrets.token_bytes()
# print(token)
# token = secrets.token_bytes(10)
# print(token)
# token = secrets.token_hex(16)
# print(token)
# url = secrets.token_urlsafe(16)
# print(url)



# pow(num, power): возведение числа num в степень power
# sqrt(num): квадратный корень числа num
# ceil(num): округление числа до ближайшего наибольшего целого
# floor(num): округление числа до ближайшего наименьшего целого
# factorial(num): факториал числа
# degrees(rad): перевод из радиан в градусы
# radians(grad): перевод из градусов в радианы
# cos(rad): косинус угла в радианах
# sin(rad): синус угла в радианах
# tan(rad): тангенс угла в радианах
# acos(rad): арккосинус угла в радианах
# asin(rad): арксинус угла в радианах
# atan(rad): арктангенс угла в радианах
# log(n, base): логарифм числа n по основанию base
# log10(n): десятичный логарифм числа n


# англосаксонская система
# 1,234.567
# европейская система
# 1.234,567

# LC_ALL: применяет локализацию ко всем категориям - к форматированию чисел, валют, дат и т.д.

# LC_NUMERIC: применяет локализацию к числам

# LC_MONETARY: применяет локализацию к валютам

# LC_TIME: применяет локализацию к датам и времени

# LC_CTYPE: применяет локализацию при переводе символов в верхний или нижний регистр

# LC_COLLIATE: применяет локаль при сравнении строк



# currency(num): форматирует валюту

# format_string(str, num): подставляет число num вместо плейсхолдера в строку str
# d: для целых чисел
# f: для чисел с плавающей точкой
# e: для экспоненциальной записи чисел



# Перед каждым плейсхолдером ставится знак процента %, например:

# "%d"
# При выводе дробных чисел перед плейсхолдером после точки можно указать, сколько знаков в дробной части должно отображаться:

# %.2f       



# import locale

# locale.setlocale(locale.LC_ALL, "de")

# number = 23231.49109
# formatted = locale.format_string("%f", number)
# print(formatted)

# formatted = locale.format_string("%.2f", number)
# print(formatted)

# formatted = locale.format_string("%d", number)
# print(formatted)

# formatted = locale.format_string("%e", number)
# print(formatted)



# locale.setlocale(locale.LC_ALL, "")
# number = 23231.49109
# formatted = locale.format_string("%.02f", number)
# print(formatted)
# print(locale.getlocale())




# from decimal import Decimal
# number = Decimal("0.1")
# # number = number + number + number
# number = number + 2
# print(number)

# number = Decimal("0.10")
# number = 3 * number
# print(number)

# метод quantize() позволяет округлять числа

# from decimal import Decimal
# number = Decimal("0.444")
# number = number.quantize(Decimal("1.00"))
# print(number)

# number = Decimal("0.55555664")
# number = number.quantize(Decimal("1.00"))
# print(number)

# number = Decimal("0.999")
# number = number.quantize(Decimal("1.00"))
# print(number)

# По умолчанию округление описывается константой ROUND_HALF_EVEN, при котором округление происходит до ближайшего четного числа, если округляемая часть равна 5.

# from decimal import Decimal, ROUND_HALF_EVEN

# number = Decimal("23.267")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)

# from decimal import Decimal, ROUND_HALF_EVEN
 
 
# number = Decimal("10.034")      
# print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)) 

# from decimal import Decimal, ROUND_HALF_EVEN

# # ROUND_HALF_UP: округляет число в сторону повышения, если после него идет число 5 или выше

# # ROUND_HALF_DOWN: округляет число в сторону повышения, если после него идет число больше 5

# number = Decimal("10.026")
# print(number.quantize(Decimal("1.00"), ROUND_HALF_DOWN))   

# number = Decimal("10.025")
# print(number.quantize(Decimal("1.00"), ROUND_HALF_DOWN))



# # ROUND_05UP: округляет 0 до единицы, если после него идет число 5 и выше

# number = Decimal("10.005")
# print(number.quantize(Decimal("1.00"), ROUND_05UP))
 
# number = Decimal("10.025")
# print(number.quantize(Decimal("1.00"), ROUND_05UP))       



# # ROUND_CEILING: округляет число в большую сторону вне зависимости от того, какое число идет после него

# number = Decimal("10.021")
# print(number.quantize(Decimal("1.00"), ROUND_CEILING))
 
# number = Decimal("10.025")
# print(number.quantize(Decimal("1.00"), ROUND_CEILING))       



# # ROUND_FLOOR: не округляет число вне зависимости от того, какое число идет после него

# number = Decimal("10.021")
# print(number.quantize(Decimal("1.00"), ROUND_FLOOR))      
 
# number = Decimal("10.025")
# print(number.quantize(Decimal("1.00"), ROUND_FLOOR))




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
 
# tom = Person("Tom", 38)
# print(f"Name: {tom.name}  Age: {tom.age}")



# from dataclasses import dataclass
 
# @dataclass
# class Person:
#     name: str
#     age: int
 
# tom = Person("Tom", 38)
# print(f"Name: {tom.name}  Age: {tom.age}")


# def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
            #   unsafe_hash=False, frozen=False, match_args=True,
            #   kw_only=False, slots=False)

# init: если равно True, то генерируется функция __init__(). По умолчанию равно True

# repr: если равно True, то генерируется функция __repr__(), которая возвращает строковое представление объекта. По умолчанию равно True

# eq: если равно True, то генерируется функция __eq__(), которая сравнивает два объекта. По умолчанию равно True

# order: если равно True, то генерируются функции __lt__ (операция <), __le__ (<=), __gt__ (>), __ge__ (>=), которые применяются для упорядочивания объектов. По умолчанию равно False

# unsafe_hash: если равно True, то генерируется функция __hash__(), которая возвращает хеш объекта. По умолчанию равно False