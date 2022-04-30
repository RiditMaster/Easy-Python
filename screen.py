from tkinter import *

def screen(title,size,icon):
    if (title == "",size == ""):
        raise NameError("TypeError: screen() 2 required positional arguments: 'title', 'size' is empty")
    w=Tk()
    w.title=title
    w.geometry=size
    w.iconbitmap=icon