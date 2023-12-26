# pcpp1 practice: simple calculator
    # Entry, Radiobutton, and Button widgets; grid manager
    # checking input validity, showing messages

import tkinter as tk
from tkinter import messagebox

# callbacks
def display(result):
    messagebox.showinfo('Result:', f'The result is {result}')

def get_number(entry):
    num = entry.get()
    try:
        value = float(num)
    except ValueError:
        return None
    return value

def evaluate():
    num1 = get_number(leftside)
    if num1 is None:
        messagebox.showerror('ERROR', 'Invalid number on the left')
        leftside.focus_set()
        return
    
    num2 = get_number(rightside)
    if num2 is None:
        messagebox.showerror('ERROR', 'Invalid number on the right')
        rightside.focus_set()
        return
    op = operation.get()

    if op == 0:
        display(num1 + num2)
    elif op == 1:
        display(num1 - num2)
    elif op == 2:
        display(num1 * num2)
    elif op == 3:
        if num2 != 0:
            display(num1 / num2)
        else:
            messagebox.showerror('ERROR', 'Cannot divide by 0')
            rightside.focus_set()  
            return  
    else:
        messagebox.showerror('ERROR', 'Please select a valid operator')
        return

window = tk.Tk()
window.title('Simple Calculator')

leftside = tk.Entry(window, width=20)
leftside.grid(row=2, column=0)

rightside = tk.Entry(window, width=20)
rightside.grid(row=2, column=2)

# operation radiobuttons
operation = tk.IntVar()
operation.set(0)

add = tk.Radiobutton(window, text='+', variable=operation, value=0)
add.grid(column=1, row=0)
subtract = tk.Radiobutton(window, text='-', variable=operation, value=1)
subtract.grid(column=1, row=1)
multiply = tk.Radiobutton(window, text='*', variable=operation, value=2)
multiply.grid(column=1, row=2)
divide = tk.Radiobutton(window, text='/', variable=operation, value=3)
divide.grid(column=1, row=3)

evaluate = tk.Button(window, text='Evaluate', command=evaluate)
evaluate.grid(column=1, row=4)

window.mainloop()