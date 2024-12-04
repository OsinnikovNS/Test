"""Тема урока: Cтроки. Часть 2. Поиск и замена
1. Методы строк count(), startswith(), endswith(), find(), rfind(), index(), rindex(), strip(), lstrip(), rstrip(),
replace()
2. Решение задач"""
# Методы поиска и замены строк внутри других строк:
# Метод count(<sub>, <start>, <end>) считает количество непересекающихся вхождений подстроки <sub> в исходную строку s
s = 'foo goo moo'
print(s.count('oo'))
print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ
# Метод startswith(<suffix>, <start>, <end>) определяет, начинается ли исходная строка s подстрокой <suffix>.
# Если исходная строка начинается с подстроки <suffix>, метод возвращает значение True, а если нет, то значение False
s = 'suffix'
print(s.startswith('suf'))
print(s.startswith('bar'))
# Метод endswith(<suffix>, <start>, <end>) определяет, оканчивается ли исходная строка s подстрокой <suffix>.
# Метод возвращает значение True, если исходная строка оканчивается на подстроку <suffix>, или False в противном случае
s = 'foobar'
print(s.endswith('bar'))
print(s.endswith('baz'))
# Метод find(<sub>, <start>, <end>) находит индекс первого вхождения подстроки <sub> в исходной строке s.
# Если строка s не содержит подстроки <sub>, то метод возвращает значение -1. Мы можем использовать данный метод
# наравне с оператором in для проверки: содержит ли заданная строка некоторую подстроку или нет.
s = 'foo bar foo baz foo qux'
print(s.find('foo'))
print(s.find('bar'))
print(s.find('qu'))
print(s.find('python'))
# Метод index(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>), за тем исключением, что он вызывает
# ошибку ValueError: substring not found во время выполнения программы, если подстрока <sub> не найдена.
#
# Метод strip() возвращает копию строки s, у которой удалены все пробелы, стоящие в начале и конце строки.
s = '     foo bar foo baz foo qux      '
print(s.strip())
# Метод lstrip() возвращает копию строки s, у которой удалены все пробелы, стоящие в начале строки.
s = '     foo bar foo baz foo qux      '
print(s.lstrip())
# Метод rstrip() возвращает копию строки s, у которой удалены все пробелы, стоящие в конце строки.
s = '      foo bar foo baz foo qux      '
print(s.rstrip())
# Метод replace(<old>, <new>) возвращает копию s со всеми вхождениями подстроки <old>, замененными на <new>.
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault'))
# Метод replace() может принимать опциональный третий аргумент <count>, который определяет количество замен.
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault', 2))
s = 'I learn Python language. Python - awesome!'
print(s.find('Python'))
# ------------------------------------------
"""Количество слов"""
# s = input()
# print(1 + s.count(' '))
# --------------------------------------
"""Минутка генетики"""
# s = input()
# s = s.lower()
# print("Аденин:", s.count('а'))
# print("Гуанин:", s.count('г'))
# print("Цитозин:", s.count('ц'))
# print("Тимин:", s.count('т'))
# ---------------------------------------------
"""Очень странные дела"""
# n = int(input())
# count = 0
# for i in range(n):
#     s = input()
#     if s.count('11') >= 3:
#         count += 1
# print(count)
# --------------------------------------------
"""Количество цифр"""
# s = input()
# count = 0
# for i in range(10):
#     count += s.count(str(i))
# print(count)
# ------------------------------------
""".com or .ru"""
# s = input()
# if s.endswith('.com') or s.endswith('.ru'):
#     print("YES")
# else:
#     print("NO")
# -------------------------------------------
"""Самый частотный символ"""
# s = input()
# count = 0
# x = ''
# for i in range(len(s)):
#     s2 = s.count(s[i])
#     if s2 >= count:
#         count = s2
#         x = s[i]
# print(x)
# -------------------------------------------------
"""Первое и последнее вхождение"""
# s = input()
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') == 0:
#     print('NO')
# else:
#     print(s.find('f'), s.rfind('f'))
# -------------------------------------------
"""Удаление фрагмента"""
s = input()
s1 = s.find('h')
s2 = s.rfind('h')
print(s[:s1] + s[s2 + 1:])