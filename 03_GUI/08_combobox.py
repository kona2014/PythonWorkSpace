import os

from tkinter import *

import tkinter.ttk as ttk


root = Tk()
root.title("KONA Coding")

root.geometry("640x480")

values = ["1", "2", "3"]
combo1 = ttk.Combobox(root, width=50, height=10, values=values, state="readonly")
combo1.pack()
# combo1.set("Combo") # 맨 처음 값 설정.

combo1.current(2)


def onClick():
    print(combo1.get())


btn = Button(root, text="Click", command=onClick)
btn.pack()

root.mainloop()