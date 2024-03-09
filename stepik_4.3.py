# -----------------------------------------
# На числовой прямой даны два отрезка: [a1;b1] и [a2;b2].
# Напишите программу, которая находит их пересечение.
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if b1 < a2 or b2 < a1:
    print('пустое множество')
elif b1 == a2:
    print(a2)
elif b2 == a1:
    print(a1)
elif a1 <=a2 < b1 < b2:
    print(a2, b1)
elif a2 <= a1 < b2 < b1:
    print(a1, b2)
elif a2 < a1 < b1 <= b2:
    print(a1, b1)
elif a1 < a2 < b2 <= b1:
    print(a2, b2)
# else:
#     print(a2, b2)

# ------------------------------------------
# Цвета колеса рулетки
# a = int(input())
# if a == 0:
#     print('зеленый')
# elif a > 36  or a < 0:
#     print('ошибка ввода')
# elif 1 <= a <= 10 and a % 2 == 0:
#     print('черный')
# elif 1 <= a <= 10 and a % 2 == 1:
#     print('красный')
# elif 11 <= a <= 18 and a % 2 == 0:
#     print('красный')
# elif 11 <= a <= 18 and a % 2 == 1:
#     print('черный')
# elif 19 <= a <= 28 and a% 2 == 0:
#     print('черный')
# elif 19 <= a <= 28 and a % 2 == 1:
#     print('красный')
# elif 29 <= a <= 36 and a % 2 == 0:
#     print('красный')
# elif 29 <= a <= 36 and a % 2 == 1:
#     print('черный')

# -------------------------------------------
# a = input()
# b = input()
# if a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
#     print('фиолетовый')
# elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
#     print('оранжевый')
# elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
#     print('зеленый')
# elif a == 'красный' and b == 'красный':
#     print('красный')
# elif a == 'синий' == b:
#     print('синий')
# elif a == 'желтый' == b:
#     print('желтый')
# else:
#     print('ошибка цвета')

# -------------------------------------------
# программа калькулятор, которая считывает с клавиатуры два целых числа и строку
# a = int(input())
# b = int(input())
# c = str(input())
# if b == 0 and c == '/':
#     print('На ноль делить нельзя!')
# elif c == '*':
#     print(a * b)
# elif c == '/':
#     print(a / b)
# elif c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# else:
#     print('Неверная операция')

# ------------------------------------------
# программа, определяющая, в какой категории будет выступать данный боксер
# a = int(input())
# if a < 60:
#     print('Легкий вес')
# elif 60 <= a < 64:
#     print('Первый полусредний вес')
# elif 64 <= a < 69:
#     print('Полусредний вес')

# -----------------------------------------
# программа, которая выводит на экран количество дней в этом месяце
# a = int(input())
# if (a <= 7 and a % 2 == 1) or (8 <= a <= 12 and a % 2 == 0):
#     print(31)
# elif a == 2:
#     print(28)
# else:
#     print(30)

# ------------------------------------------
# a, b, c = int(input()), int(input()), int(input())
# if b < a < c or c < a < b:
#     print(a)
# elif a < b < c or c < b < a:
#     print(b)
# elif a < c < b or b < c < a:
#     print(c)

# -------------------------------------------
# программf, которая принимает три положительных числа и определяет вид треугольника
# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print('Равносторонний')
# elif a == b or b == c or a == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# --------------------------------------
# n, k = int(input()), int(input())
# if n > k:
#     print('NO')
# elif k > n:
#     print('YES')
# else:
#     print("Don't know")

# --------------------------------------
# Даны три целых числа. Определите, сколько среди них совпадающих
# a, b, c = int(input()), int(input()), int(input())
#
# if a == b:
#     if b == c:
#         print(3)
#     else:
#         print(2)
# else:
#     if a == c:
#         print(2)
#     else:
#         if b == c:
#             print(2)
#         else:
#             print(0)
# ----------------------------------------------
# a, b, c = int(input()), int(input()), int(input())
#
# if a == b == c:
#     print(3)
# elif a == b:
#     print(2)
# elif b == c:
#     print(2)
# elif a == c:
#     print(2)
# else:
#     print(0)
