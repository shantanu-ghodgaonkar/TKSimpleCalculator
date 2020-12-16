from tkinter import *
from tkinter.font import *

# change for github - 1
# change for github - 2

num1 = float(0)
func = str('\0')

root = Tk()
root.title('Simple Calculator')

# Create a font style for the program
fs1 = Font(family='Times New Roman', size=20)
fs2 = Font(family='Times New Roman', size=16)

# Calculator Input Field
ip = Entry(root, width=17, borderwidth=25, fg='white', bg='black', font=fs1)
ip.grid(row=0, column=0, columnspan=3, padx=15, pady=10)


def num_btn_clk(n: float):
    ip.insert(END, n)


def btn_clr():
    ip.delete(0, END)


def btn_equ():
    num2 = ip.get()
    ip.delete(0, END)
    if func == 'add':
        ip.insert(0, round((num1 + float(num2)), 5))
    elif func == 'sub':
        ip.insert(0, round((num1 - float(num2)), 5))
    elif func == 'mul':
        ip.insert(0, round((num1 * float(num2)), 5))
    elif func == 'div':
        ip.insert(0, round((num1 / float(num2)), 5))


def btn_addn():
    t1 = ip.get()
    global num1
    global func
    func = 'add'
    num1 = float(t1)
    ip.delete(0, END)


def btn_subn():
    t1 = ip.get()
    global num1
    global func
    func = 'sub'
    num1 = float(t1)
    ip.delete(0, END)


def btn_muln():
    t1 = ip.get()
    global num1
    global func
    func = 'mul'
    num1 = float(t1)
    ip.delete(0, END)


def btn_divn():
    t1 = ip.get()
    global num1
    global func
    func = 'div'
    num1 = float(t1)
    ip.delete(0, END)


# Calculator Number Buttons
btn_1 = Button(root, text='1', padx=40, pady=20, fg='white', bg='black', font=fs2, command=lambda: num_btn_clk(1))
btn_1.grid(row=1, column=0)
btn_2 = Button(root, text='2', padx=40, pady=20, fg='white', bg='black', font=fs2, command=lambda: num_btn_clk(2))
btn_2.grid(row=1, column=1)
btn_3 = Button(root, text='3', padx=40, pady=20, fg='white', bg='black', font=fs2, command=lambda: num_btn_clk(3))
btn_3.grid(row=1, column=2)
btn_4 = Button(root, text='4', padx=40, pady=20, fg='white', bg='black', font=fs2, command=lambda: num_btn_clk(4))
btn_4.grid(row=2, column=0)
btn_5 = Button(root, text='5', padx=40, pady=20, fg='white', bg='black', font=fs2, command=lambda: num_btn_clk(5))
btn_5.grid(row=2, column=1)
btn_6 = Button(root, text='6', padx=40, pady=20, fg='white', bg='black', font=fs2, command=lambda: num_btn_clk(6))
btn_6.grid(row=2, column=2)
btn_7 = Button(root, text='7', padx=40, pady=20, fg='white', bg='black', font=fs2, command=lambda: num_btn_clk(7))
btn_7.grid(row=3, column=0)
btn_8 = Button(root, text='8', padx=40, pady=20, fg='white', bg='black', font=fs2, command=lambda: num_btn_clk(8))
btn_8.grid(row=3, column=1)
btn_9 = Button(root, text='9', padx=40, pady=20, fg='white', bg='black', font=fs2, command=lambda: num_btn_clk(9))
btn_9.grid(row=3, column=2)
btn_0 = Button(root, text='0', padx=40, pady=20, fg='white', bg='black', font=fs2, command=lambda: num_btn_clk(0))
btn_0.grid(row=4, column=0)

# Calculator Function Buttons
btn_addn = Button(root, text='+', padx=93, pady=20, fg='white', bg='black', font=fs2,
                  command=btn_addn)
btn_addn.grid(row=1, column=3, columnspan=2)
btn_subn = Button(root, text='-', padx=92, pady=13, fg='white', bg='black', font=fs1,
                  command=btn_subn)
btn_subn.grid(row=2, column=3, columnspan=2)
btn_muln = Button(root, text='*', padx=94, pady=20, fg='white', bg='black', font=fs2,
                  command=btn_muln)
btn_muln.grid(row=3, column=3, columnspan=2)
btn_divn = Button(root, text='/', padx=96, pady=20, fg='white', bg='black', font=fs2,
                  command=btn_divn)
btn_divn.grid(row=4, column=3, columnspan=2)
btn_equ = Button(root, text='=', padx=93, pady=20, fg='white', bg='black', font=fs2,
                 command=btn_equ)
btn_equ.grid(row=4, column=1, columnspan=2)
btn_clr = Button(root, text='CLEAR', padx=65, pady=20, fg='black', bg='orange', font=fs2,
                 command=btn_clr)
btn_clr.grid(row=0, column=3, columnspan=1)
if __name__ == '__main__':
    root.mainloop()
