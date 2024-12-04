"""Тема урока: Методы строк. Часть 1. Методы и функции
1. Методы строк capitalize(), swapcase(), title(), lower(), upper()
2. Решение задач"""
# Метод capitalize() возвращает копию строки s, в которой первый символ имеет верхний регистр,
# а все остальные символы имеют нижний регистр.
s = 'i Learn Python language'
print("Метод capitalize():", s.capitalize())
# Метод swapcase() возвращает копию строки s, в которой все символы, имеющие верхний регистр, преобразуются в символы
# нижнего регистра и наоборот.
s = 'FOO Bar 123 baz qUX'
print("Метод swapcase():", s.swapcase())
# Метод title() возвращает копию строки s, в которой первый символ каждого слова переводится в верхний регистр.
s = 'the sun also rises'
print('Метод title():', s.title())
# Метод lower() возвращает копию строки s, в которой все символы имеют нижний регистр.
s = 'FOO Bar 123 baz qUX'
print("Метод lower():", s.lower())
# Метод upper() возвращает копию строки s, в которой все символы имеют верхний регистр.
s = 'FOO Bar 123 baz qUX'
print("Метод upper():", s.upper())
"""
capitalize — писать прописными буквами, закрепить.
swapcase — обменять регистр. swap — гл. обмениваться, case — случай, регистр, падеж, дело, расследование...
title — заголовок, титул.
lower — нижний.
upper — верхний.
"""
s = '$12344%^$#@!'
print(s.lower())
s1 = 'a'
s2 = s1.upper()
print(s1, s2)
s = 'i LEARN Python LAnguaGE'
print(s.upper())
s = 'i LEARN Python LAnguaGE'
print(s.swapcase())
# ---------------------------------------------------------
"""Заглавные буквы"""
# s = input()
# if s == s.title():
#     print('YES')
# else:
#     print('NO')
# ---------------------------------------------------
"""sWAP cASE"""
# s = input()
# print(s.swapcase())
# ------------------------------------------------
"""Хороший оттенок"""
# s = input()
# if "хорош" in s.lower():
#     print('YES')
# else:
#     print('NO')
# ----------------------------------------------
"""Нижний регистр"""
s = input()
s2 = s.upper()
counter = 0
for i in range(len(s)):
    if s[i] != s2[i]:
        counter += 1
print(counter)