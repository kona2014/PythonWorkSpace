import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("KONA Coding")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")
    msgbox.showerror("알림", "정상적으로 예매 완료되었습니다.")
    msgbox.showwarning("알림", "정상적으로 예매 완료되었습니다.")
    response = msgbox.askokcancel("ask", "ok? cancel?")
    print(response)
    response = msgbox.askretrycancel("ask", "ok? cancel?")
    print(response)
    response = msgbox.askyesno("ask", "ok? cancel?")
    print(response)
    response = msgbox.askyesnocancel("ask", "ok? cancel?")
    print(response)

Button(root, command=info, text="Button").pack()


root.mainloop()