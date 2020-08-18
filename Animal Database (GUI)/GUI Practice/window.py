from tkinter import *
m = Tk() #window
m.minsize(500, 500) #set minimum size of the window
m.resizable(0, 0) #prevents the user to change the size of the window
m.title("Main Window") #window's name

f = Frame(m)
f.pack()

b = Button(f, text = "destroy", command = f.destroy)
b.pack()
m.mainloop()
