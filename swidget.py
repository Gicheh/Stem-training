from tkinter import *
root=Tk()

#Create a frame
My_label1=Label(root,text="Hello world!")
My_label2=Label(root,text="Hello world!")

#show it on screen
My_label1.grid(row=0,column=2)
My_label2.grid(row=1,column=0)
root.mainloop()