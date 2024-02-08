import os 
from tkinter import *
from tkinter import filedialog,colorchooser,font
from tkinter .messagebox import *
from tkinter .filedialog import *

def change_color():
    color=colorchooser.askcolor(title='pick a color')
    text_area.config(fg=color[1])  #ask color returns a tuple of representation of a color but we only need one

def change_font(*args):
    text_area.config(font=(font_name.get(),size_box.get()))

def new_file():
    window.title('Untitled')
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt",file=[("All files","*.*"),
                                                         ("Text Dcouments","*.txt")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)
        
        file = open(file,"r")
        text_area.insert(1.0,file.read())

    except Exception:
        print("couldnt open file")
    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile='untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files","*.*"),
                                                   ("Text Documents","*.txt")])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file,"w")
            file.write(text_area.get(1.0,END))
        except Exception:
            print("Couldnt save file")
        finally:
            file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")


def quit():
    window.destroy()

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

size_box =Spinbox(frame, from_=1, to= 100,textvariable=font_size,command=change_font)
size_box.grid(row=0,column=2)

scroll_bar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)


menu_bar=Menu(window)
window.config(menu=menu_bar)

file_menu= Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label="New file",command=new_file)
file_menu.add_command(label="Open file",command=open_file)
file_menu.add_command(label="Save file",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)

edit_menu=Menu(menu_bar,tearoff=0)  
menu_bar.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)



window.mainloop()