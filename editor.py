from tkinter import *

PROGRAM_NAME = "text editor"

root = Tk()
root.title(PROGRAM_NAME)

# Top menu bar creating
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
edit_menu = Menu(menu_bar, tearoff=0)
view_menu = Menu(menu_bar, tearoff=0)
about_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
menu_bar.add_cascade(label='View', menu=view_menu)
menu_bar.add_cascade(label='About', menu=about_menu)

def new_file():
    pass

def open_file():
    pass

def save_file():
    pass

def save_as_file():
    pass

# File menu items
file_menu.add_command(label="New", accelerator='Ctrl+N', compound='left', image=None, underline=0, command=new_file)
file_menu.add_command(label="Open", accelerator='Ctrl+O', compound='left', image=None, underline=0, command=open_file)
file_menu.add_command(label="Save", accelerator='Ctrl+S', compound='left', image=None, underline=0, command=save_file)
file_menu.add_command(label="Save As..", accelerator='Ctrl+Shift+S', compound='left', image=None, underline=0, command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator='Ctrl+Q', compound='left', image=None, underline=0, command=root.destroy)

def undo_callback():
    pass

edit_menu.add_command(label="Undo", accelerator='Ctrl + Z', compound='left', image=None, underline=0, command=undo_callback)

root.config(menu=menu_bar)

root.mainloop()
