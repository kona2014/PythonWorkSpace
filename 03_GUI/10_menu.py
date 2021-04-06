from tkinter import *

root = Tk()
root.title("KONA Coding")
root.geometry("640x480")

def create_new_file():
    print("New File Created")

menu1 = Menu(root)

# file menu
menu_file = Menu(menu1, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All File", state="disabled")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu1.add_cascade(label="File", menu=menu_file)

# edit menu
menu1.add_cascade(label="Edit")

# language - Radio Button
menu_lang = Menu(menu1, tearoff=0)  # tearoff 가 뭐야?
menu_lang.add_radiobutton(label="KO")
menu_lang.add_radiobutton(label="EN")
menu_lang.add_radiobutton(label="ZH")
menu1.add_cascade(label="Language", menu=menu_lang)

# View Menu - Checkbox
menu_view = Menu(menu1, tearoff=0)
menu_view.add_checkbutton(label="Show Mini Map")
menu_view.add_checkbutton(label="Show Large Map")
menu_view.add_checkbutton(label="Show All User")
menu_view.add_checkbutton(label="Show Your Profile")
menu1.add_cascade(label="View", menu=menu_view)






root.config(menu=menu1)

root.mainloop()