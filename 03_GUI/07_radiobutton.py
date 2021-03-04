import os

from tkinter import *

root = Tk()
root.title("KONA Coding")

root.geometry("640x480")

berger_var = IntVar()
btn1 = Radiobutton(root, text="aaa", value=1, variable=berger_var)
btn2 = Radiobutton(root, text="kkk", value=3, variable=berger_var)
btn3 = Radiobutton(root, text="lll", value=5, variable=berger_var)
btn3.select()
btn2.select()

btn1.pack()
btn2.pack()
btn3.pack()

def onClick():
    print(berger_var.get())


btn = Button(root, text="Click", command=onClick)
btn.pack()

root.mainloop()