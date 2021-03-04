import os

from tkinter import *

root = Tk()
root.title("KONA Coding")

root.geometry("640x480")


txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "Input text...")

ent = Entry(root, width=30)
ent.pack()

ent.insert(0, "entry only 1 line...")

def onClick():
    print(txt.get("1.2", END)) # 1 - 첫번째 라인, 0 - 0번째 컬럼
    print(ent.get())

btn = Button(root, text="Click", command=onClick)
btn.pack()

def onDelete():
    txt.delete("1.0", END)
    ent.delete(2, END)

btn2 = Button(root, text="Click", command=onDelete)
btn2.pack()

root.mainloop()