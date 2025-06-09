# Обращение к кортежам
tom = ("Tom", 37, "Google", "software developer")
print(tom[0])       # Tom
print(tom[1])       # 37
print(tom[-1])

# Получение подкортежей
tom = ("Tom", 37, "Google", "software developer")

print(tom[1:3])   

print(tom[:3])    

print(tom[1:]) 

# Кортеж как параметр и результат функций
def get_user():
    name = "Tom"
    age = 22
    company = "Google"
    return name, age, company
 
 
user = get_user()
print(user)   

# Перебор кортежей
tom = ("Tom", 22, "Google")
for item in tom:
    print(item)

# Проверка наличия значения
user = ("Tom", 22, "Google")
name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")