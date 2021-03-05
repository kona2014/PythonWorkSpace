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

drink_var = StringVar() # 문자열 속성
btn4 = Radiobutton(root, text="aaa", value="가", variable=drink_var)
btn5 = Radiobutton(root, text="kkk", value="나", variable=drink_var)
btn5.select()

btn4.pack()
btn5.pack()


def onClick():
    print(berger_var.get())


btn = Button(root, text="Click", command=onClick)
btn.pack()

root.mainloop()