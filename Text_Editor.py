import os 
from tkinter import *
from tkinter import filedialog,colorchooser,font
from tkinter .messagebox import *
from tkinter .filedialog import *

def change_color():
    color=colorchooser.askcolor(title='pick a color')
    text_area.config(fg=color[1])  #ask color returns a tuple of representation of a color but we only need one

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
screen_width= window.winfo_screenwidth() # will retrive window width while the window is displayed
screen_height= window.winfo_screenheight()# will retrive window height while the window is displayed

#calculating the coordinates (x, y) for placing the window at the center of the screen.
x= int((screen_width /2) -(window_width/2)) 
y= int((screen_height /2) -(window_height/2))

window.geometry( f"{window_width}x{window_height}+{x}+{y}")

font_name= StringVar(window)
font_name.set("Arial") #default font

font_size= StringVar(window)
font_size.set('25') # default font size

text_area= Text(window, font=(font_name.get(),font_size.get()))

scroll_bar=Scrollbar(text_area) 
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W) # the text area will fill the entire window

frame= Frame(window)
frame.grid()

color_button=Button(frame,text="Change Color",command=change_color)
color_button.grid(row=0,column=0)

font_box=OptionMenu(frame,font_name, *font.families(),command=change_font)
font_box.grid(row=0,column=1)

scroll_bar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)
window.mainloop()