import os

from tkinter import *

root = Tk()
root.title("KONA Coding")

root.geometry("640x480")

chkvar = IntVar()  # chkvar 에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text="saaa", variable=chkvar)

chkbox.select() # 선택상태
chkbox.deselect()   # 선택해제 - 원래 기본값이 선택해제임.

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="aaaaa", variable=chkvar2)


chkbox.pack()
chkbox2.pack()

def onClick():
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root, text="Click", command=onClick)
btn.pack()

root.mainloop()