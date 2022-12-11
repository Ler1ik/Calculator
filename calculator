import tkinter as tk


#Стереть всё
def Delete_0(Del):
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, '0')

#Стерать последний элемент
def Delete_1(Del):
    entry = calc_etry.get()
    entry = entry[:-1]
    if len(entry) == 0:
        entry = '0'
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)

#Сложение !!!САША!!!
def add_pl(x, y):
    return(x + y)

#Вычитание !!!САША!!!
def add_mi(x, y):
    return(x - y)

#Умножение !!!САША!!!
def add_um(x, y):
    return(x * y)

#Деление !!!САША!!!
def add_de(x, y):
    return(x / y)

#Знаменатель "⅟х" !!!САША!!!
def denominator(denominator):
    number = float(calc_etry.get()) #Не трогать
    entry = 1 / number
    calc_etry.delete(0, tk.END) #Не трогать
    calc_etry.insert(0, entry) #Не трогать

#Квадрат "x²" !!!САША!!!
def sq(square):
    number = float(calc_etry.get()) #Не трогать
    entry = number ** 2
    calc_etry.delete(0, tk.END)  # Не трогать
    calc_etry.insert(0, entry)  # Не трогать

#Квадратный корень "√х" !!!САША!!!
def sq_r(square_root):
    number = float(calc_etry.get()) #Не трогать
    entry = number ** 0.5
    calc_etry.delete(0, tk.END)  # Не трогать
    calc_etry.insert(0, entry)  # Не трогать

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
    x = y = ''
    z = ''
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
    entry = add_calculation_1(S, x, y)
    return entry


# Добавить цифру
def add_digit(digit):
    entry = calc_etry.get()
    if entry[0] == '0':
        entry = entry[1:]
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry+digit)

#Добавить знак
def add_sign(sing):
    entry = calc_etry.get()
    if entry[-1] in ['+', '-', '×', '÷', '.']:
        entry = entry[:-1]
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry+sing)

#Равно
def equally(eq):
    entry = calc_etry.get()
    entry = add_calculation_0(entry)
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)


# Главный экран
calc = tk.Tk()
calc.title('Калькулятор')
calc['bg'] = '#42313A'
calc.minsize(width=320, height=500)
calc.maxsize(width=320, height=500)
# Поле ввода (элементы появляются справа)
calc_etry = tk.Entry(calc, justify=tk.RIGHT, font=('Arial', 20), width=20)
calc_etry.insert(0, '0')
calc_etry.grid(row=0, column=0, columnspan=4, sticky='we')
# Кнопки
'''
but0 = ["MC", "MR", "M+", "M-", "MS", "M↓"]
c = 0
for i in but0:
    j0 = str(symbol(i))
    j1 = 'D_' + j0
    Button(calc, text=i).grid(row=1, column=c, columnspan=4)
    c += 1
'''  # but0
but1 = [
    "M", "CE", "C", "⌫",
    "⅟х", "x²", "√х", "÷",
    "7", "8", "9", "×",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "±", "0", ".", "="
]
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
    else:
        tk.Button(calc, text=i, bd=3, font=('Arial', 13)).grid(row=r, column=c, sticky='wens', padx=2, pady=2)

    calc.grid_rowconfigure(r, minsize=75)
    calc.grid_columnconfigure(c, minsize=70)
    c += 1
    if c > 3:
        c = 0
        r += 1

calc.mainloop()
