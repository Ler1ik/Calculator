import tkinter as tk
from tkinter import messagebox
#
def add_magic(entry):
    x = ''
    s = 0
    for i in range (len(entry)):
        if s == 0:
            if entry[i] in ['+', '-', '×', '÷']:
                x += entry[i]
                s += 1
            else:
                x += entry[i]
        else:
            break
    return x, s

#Стереть всё
def Delete_0(Del):
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, '0')
    calc_etry['state'] = tk.DISABLED


#Стерать последний элемент
def Delete_1(Del):
    entry = calc_etry.get()
    entry = entry[:-1]
    if len(entry) == 0:
        entry = '0'
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED

#Стерать всё после символа операции
def Delete_2(Del):
    entry = calc_etry.get()
    entry_0, sim = add_magic(entry)
    if sim == 0:
        entry = '0'
    else:
        entry = entry_0
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED

#Противоположный элемент
def neg(neg):
    entry = str(int(calc_etry.get()) * (-1))
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED

#Сложение
def add_pl(x, y):
    return str(x + y)

#Вычитание
def add_mi(x, y):
    return str(x - y)

#Умножение
def add_um(x, y):
    return str(x * y)

#Деление
def add_de(x, y):
    try:
        return str(x / y)
    except ZeroDivisionError:
        messagebox.showerror('Ошибка', 'Деление на ноль невозможно')
        return 0

#Знаменатель "⅟х"
def denominator(denominator):
    number = float(calc_etry.get())
    try:
        entry = str(1 / number)
        calc_etry['state'] = tk.NORMAL
        calc_etry.delete(0, tk.END)
        calc_etry.insert(0, entry)
        calc_etry['state'] = tk.DISABLED
    except ZeroDivisionError:
        messagebox.showerror('Ошибка', 'Деление на ноль невозможно')
        calc_etry['state'] = tk.NORMAL
        calc_etry.delete(0, tk.END)
        calc_etry.insert(0, '0')
        calc_etry['state'] = tk.DISABLED

#Квадрат "x²"
def sq(square):
    number = float(calc_etry.get())
    entry = str(number ** 2)
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED

#Квадратный корень "√х"
def sq_r(square_root):
    number = float(calc_etry.get())
    entry = str(number ** 0.5)
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED

#Pасчёт_1
def add_calculation_1(S, x, y):
    if S == '+':
        calculation = add_pl(x, y)
    elif S == '-':
        calculation = add_mi(x, y)
    elif S == '×':
        calculation = add_um(x, y)
    elif S == '÷':
        calculation = add_de(x, y)
    return calculation

#Pасчёт_0; Разбиваем строку на 2 числа и символ между ними
def add_calculation_0(entry):
    x, y = 0, ''
    S = ''
    a = []
    while entry != '':
        i = len(entry) - 1
        a.append(entry[i])
        entry = entry[:i]
    a.reverse()
    for i in a:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            y += i
        else:
            S = i
            x = y
            y = ''
    x = float(x)
    y = float(y)
    if S != '':
        entry = add_calculation_1(S, x, y)
    else:
        entry = calc_etry.get()
    return str(entry)


# Добавить цифру
def add_digit(digit):
    entry = calc_etry.get()
    if entry[0] == '0' and len(entry) == 1:
        entry = entry[1:]
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry+digit)
    calc_etry['state'] = tk.DISABLED

#Добавить знак
def add_sign(sing):
    entry_0 = calc_etry.get()
    if sing in ['.']:
        K = 0
        for i in range(len(entry_0)):
            if entry_0[i] in ['+', '-', '×', '÷'] and (i != len(entry_0) - 1):
                K = 0
            elif entry_0[i] in ['.']:
                K += 1
        if K > 0:
            sing = ''
    if entry_0[-1] in ['+', '-', '×', '÷', '.'] and sing != '':
        entry = entry_0[:-1] + sing
    else:
        entry = entry_0 + sing
    if entry[-1] in ['+', '-', '×', '÷'] and ('+' in entry[:-1] or '-' in entry[:-1] or '×' in entry[:-1] or '÷' in entry[:-1]):
        entry = str(add_calculation_0(entry[:-1])) + entry[-1]
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED

#Равно
def equally(eq):
    entry = calc_etry.get()
    if entry[-1] in ['+', '-', '×', '÷']:
        entry = entry + entry[:-1]
    entry = str(add_calculation_0(entry))
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED

#Меню
def menu(m):
    menu_top = tk.Toplevel(calc)
    #menu_top.overrideredirect(True)
    menu_top['bg'] = '#42313A'
    menu_top.minsize(width=320, height=500)
    menu_top.maxsize(width=320, height=500)
    tk.Button(menu_top, text='Игра', bd=3, font=('Arial', 13)).grid(row=0, column=0, sticky='wens', padx=2, pady=2)

#Ввод через клавиатуру
def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    if event.char in ['+', '-', '*', '/', '.']:
        if event.char == '*':
            event.char = '×'
        if event.char == '/':
            event.char = '÷'
        add_sign(event.char)
    if event.char in ['=', '\r']:
        equally(event.char)
    if event.char == '\x1b':
        Delete_0(event.char)
    if event.char == '\x08':
        Delete_1(event.char)
    if event.char == '`':
        Delete_2(event.char)


# Главный экран
calc = tk.Tk()
calc.title('Калькулятор')
calc['bg'] = '#42313A'
calc.minsize(width=320, height=500)
calc.maxsize(width=320, height=500)
# Поле ввода (элементы появляются справа)
calc_etry = tk.Entry(calc, justify=tk.RIGHT, font=('Arial', 20), width=20)
calc_etry.insert(0, '0')
calc_etry['state'] = tk.DISABLED
calc_etry.grid(row=0, column=0, columnspan=4, sticky='we')
# Кнопки
but1 = [
    "M", "CE", "C", "⌫",
    "⅟х", "x²", "√х", "÷",
    "7", "8", "9", "×",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "±", "0", ".", "="
]
calc.bind('<Key>', press_key)
r, c = 1, 0
for i in but1:
    if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        tk.Button(calc, text=i, bd=3, font=('Arial', 13), command=lambda v=i: add_digit(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    elif i in ['+', '-', '×', '÷', '.']:
        tk.Button(calc, text=i, bd=3, font=('Arial', 13), command=lambda v=i: add_sign(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    elif i == '=':
        tk.Button(calc, text=i, bd=3, font=('Arial', 13), command=lambda v=i: equally(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    elif i == '⅟х':
        tk.Button(calc, text=i, bd=3, font=('Arial', 13), command=lambda v=i: denominator(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    elif i == 'x²':
        tk.Button(calc, text=i, bd=3, font=('Arial', 13), command=lambda v=i: sq(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    elif i == '√х':
        tk.Button(calc, text=i, bd=3, font=('Arial', 13), command=lambda v=i: sq_r(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    elif i == 'C':
        tk.Button(calc, text=i, bd=3, font=('Arial', 13), command=lambda v=i: Delete_0(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    elif i == '⌫':
        tk.Button(calc, text=i, bd=3, font=('Arial', 13), command=lambda v=i: Delete_1(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    elif i == 'CE':
        tk.Button(calc, text=i, bd=3, font=('Arial', 13),  command=lambda v=i: Delete_2(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    elif i == '±':
        tk.Button(calc, text=i, bd=3, font=('Arial', 13), command=lambda v=i: neg(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    elif i == 'M':
        tk.Button(calc, text=i, bd=3, font=('Arial', 13), command=lambda v=i: menu(v)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)
    calc.grid_rowconfigure(r, minsize=75)
    calc.grid_columnconfigure(c, minsize=70)
    c += 1
    if c > 3:
        c = 0
        r += 1

calc.mainloop()
