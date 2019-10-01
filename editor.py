#!/usr/bin/python3

from tkinter import *

PROGRAM_NAME = "text editor"

root = Tk()
root.minsize(600, 400) 
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

# Icons
new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')

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

# Textframe actions
def cut():
    content_text.event_generate("<<Cut>>")

def undo_callback():
    pass

def redo_callback():
    pass

def copy():
    content_text.event_generate("<<Copy>>")

def paste():
    content_text.event_generate("<<Paste>>")

def find_callback():
    pass

def select_all_callback():
    pass

# Edit menu items
edit_menu.add_command(label="Undo", accelerator='Ctrl + Z', 
    compound='left', image=None, underline=0, command=undo_callback)
edit_menu.add_command(label="Redo", accelerator='Ctrl + Y', 
    compound='left', image=None, underline=0, command=redo_callback)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator='Ctrl + X', 
    compound='left', image=cut_icon, underline=0, command=cut)
edit_menu.add_command(label="Copy", accelerator='Ctrl + C', 
    compound='left', image=copy_icon, underline=0, command=copy)
edit_menu.add_command(label="Paste", accelerator='Ctrl + V', 
    compound='left', image=paste_icon, underline=0, command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Find", accelerator='Ctrl + F', 
    compound='left', image=None, underline=0, command=find_callback)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", accelerator='Ctrl + A', 
    compound='left', image=None, underline=0, command=select_all_callback)

def about():
    pass
 
def showhelp():
    pass

# Help menu items
about_menu.add_command(label="Help", compound='left', image=None, underline=0, command=showhelp)
about_menu.add_command(label="About", compound='left', image=None, underline=0, command=about)

# View menu
show_line_no = BooleanVar()
highlight_line = BooleanVar()
show_whitespaces = BooleanVar()
view_menu.add_checkbutton(label="Show Line Number", variable=show_line_no)
view_menu.add_checkbutton(label="Highlight current line", variable=highlight_line)
view_menu.add_checkbutton(label="Show whitespaces", variable=show_whitespaces)

color_schemes = {
    'Default': '#000000.#FFFFFF',
    'Greygarious': '#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue': '#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
}

themes_menu = Menu(menu_bar, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu)
theme_choice = StringVar()
theme_choice.set('Default')
for k in sorted(color_schemes):
    themes_menu.add_radiobutton(label=k, variable=theme_choice)

# Line numbers and shortcuts menu
shortcut_bar = Frame(root, height=25, background='seagreen')
shortcut_bar.pack(expand='no', fill='x')
line_number_bar = Text(root, width=4, padx=2, takefocus=0, border=0, background='khaki', state='disabled', wrap='none')
line_number_bar.pack(side='left', fill='y')

# Textframe
content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

root.config(menu=menu_bar)

root.mainloop()
