import os 
from tkinter import *
from tkinter import filedialog,colorchooser,font
from tkinter .messagebox import *
from tkinter .filedialog import *

def change_color():
    pass

def change_font(*args):
    pass

def new_file():
    pass

def open_file():
    pass

def save_file():
    pass

def cut():
    pass

def copy():
    pass

def about():
    pass

def quit():
    pass

window= Tk()
window.title("Text Editor programg")
file= None
window_width= 500
window_height=500
screen_width= window.winfo_screenwidth()
screen_height= window.winfo_screenheight()

x= int((screen_width /2) -(window_width/2))
y= int((screen_height /2) -(window_height/2))

window.geometry( "{}x{}+{}+{}".format(window_width,window_height,x,y))

print("Delete function")
window.mainloop()