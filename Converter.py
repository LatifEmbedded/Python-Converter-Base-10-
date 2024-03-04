from tkinter import *
import tkinter as tk
def deletes() :
    user_base.config(background = 'white', fg = 'black')
    user_base.delete(0, END)
def clearing() :
    user_entry.config(background = 'white', fg = 'black')
    user_entry.delete(0, END)
def checking() :
    value = user_entry.get()
    if value.isalnum() :
        return True
    else :
        user_entry.delete(0, END)
        user_entry.config(background = 'red', fg = 'black')
        user_entry.insert(END, '_Error_')
        user_entry.after(1000, clearing)
def hex_to_dec() :
    try :
        value = int(user_entry.get(), 16)
        value = str(value)
        user_result.insert(END, value)
    except :
        user_entry.delete(0, END)
        user_entry.config(background = 'red', fg = 'black')
        user_entry.insert(END, '_Error_')
        user_entry.after(1000, clearing)
def octal_to_deci():
    try :
        value = int(user_entry.get(), 8)
        value = str(value)
        user_result.insert(END, value)
    except :
        user_entry.delete(0, END)
        user_entry.config(background = 'red', fg = 'black')
        user_entry.insert(END, '_Error_')
        user_entry.after(1000, clearing)
def binary_to_deci() :
    try :
        value = int(user_entry.get(), 2)
        value = str(value)
        user_result.insert(END, value)
    except :
        user_entry.delete(0, END)
        user_entry.config(background = 'red', fg = 'black')
        user_entry.insert(END, '_Error_')
        user_entry.after(1000, clearing)
def go_function() :
    string = user_base.get()
    if string.lower() in ['hexadecimal', 'hex'] :
        return 16
    elif string.lower() in ['octal', 'oct'] :
        return 8
    elif string.lower() in ['binary', 'bnr'] :
        return 2
    else :
        user_base.delete(0, END)
        user_base.config(background = 'red', fg = 'black')
        user_base.insert(END, '_Error_')
        user_base.after(1000, deletes)
        return False
def check(event = None) :
    state = 0
    number = True
    if user_entry.get() :
        state = checking()
        if state == True :
            number = go_function()
            if number != False :
                if number == 16 :
                    hex_to_dec()
                elif number == 8 :
                    octal_to_deci()
                else :
                    binary_to_deci()
def clear() :
    clearing()
    user_result.delete(0, END)
    deletes()
master = Tk()
master.title('Converter to Base 10')
master.minsize(300, 300)
master.maxsize(300, 300)
master.geometry('500x500+400+140')
master.resizable(False, False)
master.configure(background = 'grey')
user = Label(master, text = 'Number', background = 'grey', fg = 'black')
user.place(x = 10, y = 50)
user_entry = Entry(master, justify = CENTER, background = 'white', fg = 'black', font = ('Arial', 10), width = 27, relief = RAISED)
user_entry.place(x = 70, y = 50)
Base = Label(master, text = 'From Base', background = 'grey', fg = 'black')
Base.place(x = 4, y = 100)
user_base = Entry(master, justify = CENTER, background = 'white', fg = 'black', font = ('Arial', 10), width = 27, relief = RAISED)
user_base.place(x = 70, y = 100)
result = Label(master, text = 'Result', background = 'grey', fg = 'black')
result.place(x = 10, y = 150)
user_result = Entry(master, justify = CENTER, background = 'white', fg = 'black', font = ('Arial', 10), width = 27, relief = RAISED)
user_result.place(x = 70, y = 150)
button = Button(master, text = 'Ok', background = 'grey', fg = 'white', activebackground = 'grey', activeforeground = 'white', height = 1, width = 5, command = check)
button.place(x = 70, y = 200)
button_clear = Button(master, text = 'Clear', background = 'grey', fg = 'white', activebackground = 'grey', activeforeground = 'white', width = 5, height = 1, command = clear)
button_clear.place(x = 220, y = 200)
master.bind('<Return>', check)
master.mainloop()