import os

from tkinter import *

root = Tk()
root.title("KONA Coding")

btn1 = Button(root, text="aaa")
btn1.pack()

btn2 = Button(root, padx=10, pady=20, text="b") # padx, pady 는 버튼 내부 컨텐츠의 좌우 여백으로 버튼 사이즈 조정
btn2.pack()


btn3 = Button(root, padx=20, pady=10, text="c")
btn3.pack()

btn4 = Button(root, width=3, height=1, text="d") #  width, height 는 버튼 사이즈의 고정값.
btn4.pack()


btn5 = Button(root, fg="red", bg="yellow", text="e") #  fg = 글자색, bg = 배경색
btn5.pack()

# Current Folder Path
path = os.path.dirname(os.path.realpath(__file__))
filename = path + "\Images\KONA.png"
# filename = "Images\KONA.jpg" 
photo = PhotoImage(file=filename) # PhotoImage 함수는 JPG 파일은 사용못한다. 
btn6 = Button(root, image=photo)
btn6.pack()

def onPressButton():
    print("onPressButton")

btn7 = Button(root, text="Command", command=onPressButton)
btn7.pack()

root.mainloop()