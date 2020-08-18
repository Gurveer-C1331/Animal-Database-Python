from tkinter import *

m = Tk() #window
m.minsize(200, 200) #set minimum size of the window
m.resizable(0, 0) #prevents the user to change the size of the window
m.title("Main Window") #window's name

def con_selection():
    if con.get() != "--Select--":
        print("Your selection is", con.get())

#option menu
continent_list = ["north america", "south america", "europe", "africa", "asia", "australia", "antarctica"]
con = StringVar()
con.set("--Select--")
opt = OptionMenu(m, con, *continent_list)
opt.pack()

#button
enter = Button(m, text = "Enter", command = con_selection)
enter.pack()

m.mainloop()