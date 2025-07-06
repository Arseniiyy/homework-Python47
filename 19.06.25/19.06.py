# Задание 1
openFile = open("data.txt", "w")

with open("data.txt", "w", encoding="utf8") as file:
    file.write("\n Это начальные данные.")
    print("Роберт")

with open("data.txt", "a", encoding="utf8") as file:
    file.write("\n Дополнительная информация")
    print("Акобян")

with open("data.txt", "r", encoding="utf8") as file:
    file.read()


# Задание 2
from datetime import datetime

current_datetime = datetime.now()

with open('log.txt', 'w') as file:
    file.write(current_datetime.strftime('%Y-%m-%d %H:%M:%S'))

print("Все операции с файлами завершены успешно.")
