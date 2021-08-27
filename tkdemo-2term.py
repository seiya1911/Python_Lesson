import tkinter as tk

current_number = 0
first_term = 0
second_term = 0
result = 0


def do_plus():
    global current_number
    global first_term
    first_term = current_number
    current_number = 0


def do_eq():
    global second_term
    global result
    global current_number
    second_term = current_number
    result = first_term + second_term
    current_number = 0


# def key1():
#     key(1)


# def key2():
#     key(2)


# def key3():
#     key(3)


# def key4():
#     key(4)


# def key5():
#     key(5)


# def key6():
#     key(6)


# def key7():
#     key(7)


# def key8():
#     key(8)


# def key9():
#     key(9)


# def key0():
#     key(0)


def key(n):
    global current_number
    current_number = current_number*10 + n
    show_number(current_number)


def clear():
    global current_number
    current_number = 0
    show_number(current_number)


def plus():
    do_plus()
    show_number(current_number)


def eq():
    do_eq()
    show_number(result)


def show_number(num):
    e.delete(0, tk.END)
    e.insert(0, str(num))


root = tk.Tk()
f = tk.Frame(root, bg='#ffffc0')
f.grid()

b1 = tk.Button(f, text='1', command=lambda: key(1),
               highlightbackground='#ffffff', width=2, font=('Helvetica', 14))
b2 = tk.Button(f, text='2', command=lambda: key(2),
               highlightbackground='#ffffff', width=2, font=('Helvetica', 14))
b3 = tk.Button(f, text='3', command=lambda: key(3),
               highlightbackground='#ffffff', width=2, font=('Helvetica', 14))
b4 = tk.Button(f, text='4', command=lambda: key(4),
               highlightbackground='#ffffff', width=2, font=('Helvetica', 14))
b5 = tk.Button(f, text='5', command=lambda: key(5),
               highlightbackground='#ffffff', width=2, font=('Helvetica', 14))
b6 = tk.Button(f, text='6', command=lambda: key(6),
               highlightbackground='#ffffff', width=2, font=('Helvetica', 14))
b7 = tk.Button(f, text='7', command=lambda: key(7),
               highlightbackground='#ffffff', width=2, font=('Helvetica', 14))
b8 = tk.Button(f, text='8', command=lambda: key(8),
               highlightbackground='#ffffff', width=2, font=('Helvetica', 14))
b9 = tk.Button(f, text='9', command=lambda: key(9),
               highlightbackground='#ffffff', width=2, font=('Helvetica', 14))
b0 = tk.Button(f, text='0', command=lambda: key(0),
               highlightbackground='#ffffff', width=2, font=('Helvetica', 14))
bc = tk.Button(f, text='C', command=clear,
               highlightbackground='#ff0000', width=2, font=('Helvetica', 14))
bp = tk.Button(f, text='+', command=plus,
               highlightbackground='#00ff00', width=2, font=('Helvetica', 14))
be = tk.Button(f, text='=', command=eq,
               highlightbackground='#00ff00', width=2, font=('Helvetica', 14))

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=0)
bc.grid(row=1, column=3)
be.grid(row=4, column=3)
bp.grid(row=2, column=3)

e = tk.Entry(f)
e.grid(row=0, column=0, columnspa=4)
clear()

root.mainloop()
