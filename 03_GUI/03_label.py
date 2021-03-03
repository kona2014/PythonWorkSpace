import os

from tkinter import *

root = Tk()
root.title("KONA Coding")

root.geometry("640x480")

lable01 = Label(root, text="Label 01")
lable01.pack()

filename = "03_GUI\Images\KONA.png"

photo = PhotoImage(file=filename)
lable02 = Label(root, image=photo)
lable02.pack()

def onClick():
    lable01.config(text="BBB")

    global photo2  # 전역변수로 선언해줘야 업데이트 된다. 

    photo2 = PhotoImage(file="03_GUI\Images\image2.png")
    btn.config(image=photo2)    

btn = Button(root, text="click", command=onClick)
btn.pack()




root.mainloop()