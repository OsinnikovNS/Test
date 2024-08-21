# Тема урока: Строковый тип данных. Модуль math.
# Площадь правильного многоугольника с длиной стороны a и
# количеством сторон n
from math import *
n, a = float(input()), float(input())
s = (n * a**2)/(4*tan(radians(pi/n)))
print(s)

# --------------------------------------------
# вещественные корни квадратного уравнения:
# Найти дискриминант (D = b2 - 4ac)
# Если дискриминант меньше нуля, то корней нет;
# Если равен нулю - корень один: x = -b / 2a;
# Если больше нуля - корней два: x1 = (-b + √D) / 2a и x2 = (-b - √D) / 2a.
from math import *
a, b, c = float(input()), float(input()), float(input())
d = b**2 - (4 * a * c)
if d > 0:
    x1 = (-b + sqrt(d))/(2 * a)
    x2 = (-b - sqrt(d))/(2 * a)
    if x1 < x2:
        print(x1)
        print(x2)
    else:
        print(x2)
        print(x1)
if d == 0:
    x = (-b)/(2 * a)
    print(x)
if d < 0:
    print('Нет корней')

# --------------------------------------------
# пол - потолок числа
from math import *
x = float(input())
a = ceil(x)  # округление числа вверх
b = floor(x)  # округление числа вниз
print(a + b)

# ---------------------------------------------
from math import *
x = float(input())
r = radians(x)
rez = sin(r) + cos(r) + tan(r) * tan(r)
print(rez)

# ---------------------------------------------
from math import *
a, b = float(input()), float(input())
sum1 = (a + b)/2
sum2 = sqrt(a*b)
sum3 = 2*a*b/(a+b)
sum4 = sqrt((a**2 + b**2)/2)
print(sum1)
print(sum2)
print(sum3)
print(sum4)

# ---------------------------------------------
from math import *
r = float(input())
s = pi * r**2
c = 2*pi*r

print(s, c)

#---------------------------------------------
# from math import *
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
# q = sqrt((x1 - x2)**2 + (y1-y2)**2)
# print(q)

# -------------------------------------------
# модуль math
# import math # или from math import *
# num1 = math.sqrt(2)     # вычисление квадратного корня из двух
# num2 = math.ceil(3.8)   # округление числа вверх
# num3 = math.floor(3.8)  # округление числа вниз
#
# print(num1)
# print(num2)
# print(num3)


# -----------------------------------------------
# программа, проверяющая корректность ввода email адреса
# s = str(input())
# if '@' in s and '.' in s:
#     print('YES')
# else:
#     print('NO')

# -----------------------------------------------------
# s = str(input())
# if 'суббота' in s or 'воскресенье' in s:
#     print('YES')
# else:
#     print('NO')
# -------------------------------------------------
# s = str(input())
# if 'синий' in s:
#     print('YES')
# else:
#     print('NO')

# ------------------------------------------------------
# s = input()
# if '.' not in s:
#     print('Введенная строка не содержит символа точки')
#
# # ----------------------------------------------
# s = input()
# if 'a' in s:
#     print('Введенная строка содержит символ а')
# else:
#     print('Введенная строка не содержит символ а')

# ----------------------------------------------
# n = 3
# name1 = str(input())
# name2 = str(input())
# name3 = str(input())
# lenght1 = len(name1)
# lenght2 = len(name2)
# lenght3 = len(name3)
# _max = max(lenght1, lenght2, lenght3)
# _min = min(lenght1, lenght2, lenght3)
# med = (lenght1 + lenght2 + lenght3)-(_max + _min)
# d = (_max - _min)/(n - 1)
# if _max - med == d and med - _min == d:
#     print('YES')
# else:
#     print('NO')

# ----------------------------------------------
# name1 = str(input())
# name2 = str(input())
# name3 = str(input())
# lenght1 = len(name1)
# lenght2 = len(name2)
# lenght3 = len(name3)
# _max = max(lenght1, lenght2, lenght3)
# _min = min(lenght1, lenght2, lenght3)
# if lenght1 == _min:
#     print(name1)
# if lenght2 == _min:
#     print(name2)
# if lenght3 == _min:
#     print(name3)
# if lenght1 == _max:
#     print(name1)
# if lenght2 == _max:
#     print(name2)
# if lenght3 == _max:
#     print(name3)
# ---------------------------------------------
# программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
# name = str(input())
# lenght = len(name)
# print('Футбольная команда', name, 'имеет длину', lenght, 'символов')

# --------------------------------------------
# firstname = str(input())
# lastname = str(input())
# print('Hello', firstname, lastname +'!', 'You have just delved into Python')

# ----------------------------------------------------
# str1 = '"Python is a great language!", said Fred. '
# str2 = "I "
# str3 = "don't"
# str4 = " ever remember having this much fun before."
# print(str1 + str2 + str3 + str4)
