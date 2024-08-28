# -------------------------------------------------
# # сортировка по убыванию:
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# my_numbers.sort(key=lambda x: -x)
# print(my_numbers)
# -----------------------------------
# # сортировка по убыванию, если х >=5 и по возрастанию, если иначе
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# my_numbers.sort(key=lambda x: -x if x >= 5 else x)
# print(my_numbers)
# ------------------------------------------------
# # сортировка сложных списков:
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
# my_pairs = list(zip(my_numbers, they_numbers))
# print(my_pairs)
# -------------------------------------------
# # cортировка по ключу:
# my_pairs = [(3, 2), (1, 7), (4, 1), (1, 8), (5, 2), (9, 8), (2, 1), (6, 8)]
# print(my_pairs)
# my_pairs.sort(key=lambda x: x[0])  # сортировка по первому элементу
# # my_pairs.sort(key=lambda x: x[1]) # сортировка по второму элементу
# print(my_pairs)
# ---------------------------------------------
# словарь с значениями по умолчанию
good = [
    ['спички', 12],
    ['соль', 34],
    ['крупа', 56],
    ['спички', 78],
    ['соль', 90],
    ['крупа', 100]
]
good_count = {}
for name, quantity in good:
    if name in good_count:
        good_count[name] += quantity
    else:
        good_count[name] = quantity
print(good_count)
# ------------------------------------------
# то же решение с помощью модуля collections

from collections import defaultdict

good_count = defaultdict(lambda: 0)  # можно заменить good_count = defaultdict(int) или defaultdict(list)
for name, quantity in good:
    good_count[name] += quantity
print(good_count)
# ------------------------------------------------
# from collections import OrderedDict
#
# my_pets = OrderedDict()
# my_pets['собака'] = 'Жучка'
# my_pets['мышка'] = 'Норушка'
# my_pets['кошка'] = 'Мурка'
# my_pets['попугай'] = 'Кеша'
# my_pets['рыбка'] = 'Геннадий'
# my_pets['таракан'] = 'Коля'
# my_pets['кролик'] = 'Савелий'
# print(my_pets)
# for k, v in my_pets.items():
#     print(k, v)
# --------------------------------------------
# from functools import reduce
# # умножение/сложение списка
# my_numbers = [1, 2, 3, 4, 5, 6]
# print(reduce(lambda x, y: x * y, my_numbers))
# print(sum(my_numbers))  # сложение списка функциональным способом
