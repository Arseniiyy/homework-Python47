

# Задача 1: 

# MySet = {56, 98, 56, 56}
# # print(type(MySet))

# def unique_elements(input_list):
#     return list(set(input_list))
# print(unique_elements(MySet))






# Задача 2: 

# firstDicr = {
#     'name': "Первый словарь",
    
# }

# secondDict = {
#     'name': "Второй словарь"
# }

# def merge_dicts(dict1, dict2):
#     result = dict1.copy()
#     for key, value in dict2.items():
#         if key in result:
#             result[key] += value
#         else:
#             result[key] = value;
#     return result;
# print(merge_dicts(firstDicr, secondDict))


# Задача 3: 

# def count_frequency(input_list):
#     frequency = {}
#     for item in input_list:
#         if item in frequency:
#             frequency[item] += 1
#         else:
#             frequency[item] = 1
#     return frequency;

# list = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1]
# print(count_frequency(list))


# numbers = [-4,-3,-2,-1,0,1,2,3]

# positiveValue = [n for n in numbers if n > 0]
# print(positiveValue)
# print(type(positiveValue))

# dictionary = {'user1': 'Egor', 'user2': 'Ilya', 'user3': "Arseniy", 'user4': 'Karen'}
# words = [word for word in dictionary.values()]
# print(words)


# wb = ["Помада", "Консилер", "Подводка"]
# pomada, konsiler, podvodka = wb


# pomada = 1
# konsiler = 2
# podvodka = 3
# numbers =pomada,konsiler,podvodka
# print(numbers) 
