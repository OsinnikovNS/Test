# from tkinter import *
# from tkinter import ttk
#
# # Создайте экземпляр фрейма или окна tkinter
# window = Tk()
#
# # Установить размер окна
# window.geometry("700x350")
#
#
# # Создайте функцию для очистки поля со списком
# def clear_combobox():
#     combobox.set('')
#
#
# # Определить кортеж дней
# days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
#
#
# # Функция для печати индекса выбранной опции в Combobox
# def callback(*arg):
#     Label(window, text='Индекс равен' + str(combobox.current()) + ' для ' + ' ' + str(var.get()),
#           font=('Helvetica 12')).pack()
#
#
# # Создайте виджет со списком
# var = StringVar()
# combobox = ttk.Combobox(window, textvariable=var)
# combobox['values'] = days
# combobox['state'] = 'readonly'
# combobox.pack(fill='x', padx=5, pady=5)
#
# # Установите трассировку для данной переменной
# var.trace('w', callback)
#
# # Создайте кнопку, чтобы очистить выбранное текстовое значение поля со списком
# button = Button(window, text='очистить', command=clear_combobox)
# button.pack()
#
# window.mainloop()
# -----------------------------------------------------------------------------------

# import tkinter as tk
# from tkinter import ttk
#
# # Creating tkinter window
# window = tk.Tk()
# window.title('Combobox')
# window.geometry('500x250')
#
# # label text for title
# ttk.Label(window, text="GFG Combobox Widget",
#           background='green', foreground="white",
#           font=("Times New Roman", 15)).grid(row=0, column=1)
#
# # label
# ttk.Label(window, text="Select the Month :",
#           font=("Times New Roman", 10)).grid(column=0,
#                                              row=5, padx=10, pady=25)
#
# # Combobox creation
# n = tk.StringVar()
# monthchoosen = ttk.Combobox(window, width=27, textvariable=n)
#
# # Adding combobox drop down list
# monthchoosen['values'] = (' January',
#                           ' February',
#                           ' March',
#                           ' April',
#                           ' May',
#                           ' June',
#                           ' July',
#                           ' August',
#                           ' September',
#                           ' October',
#                           ' November',
#                           ' December')
#
# monthchoosen.grid(column=1, row=5)
# monthchoosen.current()
# window.mainloop()
# ------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk

# Creating tkinter window
window = tk.Tk()
window.geometry('350x250')
# Label
ttk.Label(window, text="Выберите месяц :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=15, padx=10, pady=25)

n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width=27,
                            textvariable=n)

# Adding combobox drop down list
monthchoosen['values'] = (' Январь',
                          ' Февраль',
                          ' Март',
                          ' Апрель',
                          ' Май',
                          ' Июнь',
                          ' Июль',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

monthchoosen.grid(column=1, row=15)

# Shows february as a default value
monthchoosen.current(1)
window.mainloop()

