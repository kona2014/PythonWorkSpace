import os

from tkinter import *

root = Tk()
root.title("KONA Coding")

root.geometry("640x480")


listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "AA")
listbox.insert(END, "BB")
listbox.insert(1, "CCC")
listbox.insert(END, "DD")
listbox.pack()

def onClick():
    # listbox.delete(END) # delete
    print(listbox.size())
    print(listbox.get(1,2))
    print(listbox.curselection()) # 선택된 항목의 인덱스값 반환.

btn = Button(root, text="Click", command=onClick)
btn.pack()

root.mainloop()