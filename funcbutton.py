from tkinter import *
root=Tk()
def MyClick():
    Mylabel=Label(root,text="Hello motherfucker!")
    Mylabel.pack()
MyB=Button(root,text="Click me!",command=MyClick)
MyB.pack()


root.mainloop()