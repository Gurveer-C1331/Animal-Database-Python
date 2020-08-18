from tkinter import *

m = Tk() #window
m.minsize(200, 200) #set minimum size of the window
m.resizable(0, 0) #prevents the user to change the size of the window
m.title("Main Window") #window's name

def enter_choice():
    print("Your selection is",con.get())

#radiobutton
con = StringVar()
radio_1 =  Radiobutton(m, text = "North America", variable = con, value = "North America")
radio_2 = Radiobutton(m, text = "Africa", variable = con, value = "Africa")
radio_3 = Radiobutton(m, text = "Europe", variable = con, value = "Europe")
radio_1.place(x = 10, y = 10)
radio_2.place(x = 10, y = 30)
radio_3.place(x = 10, y = 50)

#button
enter = Button(m, text = "Enter", command = enter_choice)
enter.place(x = 10, y = 80)

m.mainloop()