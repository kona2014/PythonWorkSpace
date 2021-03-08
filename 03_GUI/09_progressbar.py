import os
import time
from tkinter import *

import tkinter.ttk as ttk


root = Tk()
root.title("KONA Coding")

root.geometry("640x480")

# bar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
bar = ttk.Progressbar(root, maximum=100, mode="determinate")
bar.start(10) #지정한 ms 마다 움직임
bar.pack()


p_bar2 = DoubleVar()
bar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_bar2)
bar2.pack()


def onClick():
    for i in range(1, 101):
        time.sleep(0.01) # 시간 지연
        p_bar2.set(i) # 값 업데이트
        bar2.update() # UI 업데이트

    

btn = Button(root, text="Stop", command=onClick)
btn.pack()

root.mainloop()