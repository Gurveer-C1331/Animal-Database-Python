from tkinter import *
m = Tk() #window
m.minsize(200, 200) #set minimum size of the window
m.resizable(0, 0) #prevents the user to change the size of the window
m.title("Main Window") #window's name

def hello(): #when button is pressed
    print("hello")

#buttons 
buttonw = Button(m, text = "Search", command = hello) 
buttonw.place(x = 50,y = 30, height = 20, width = 100) #placing of buttonw

button_stop = Button(m, text = "Stop", command = m.destroy) #m.destroy closes the window
button_stop.place(x = 50, y = 50, height = 20, width = 100)

button_colour = Button(m, activeforeground = "white", text = "Colour", command = None)
button_colour.place(x = 50, y = 70, height = 20, width = 100)

m.mainloop()
