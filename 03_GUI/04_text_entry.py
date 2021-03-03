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
    print(txt.get("1.0", END))

btn = Button(root, text="Click", command=onClick)
btn.pack()

root.mainloop()