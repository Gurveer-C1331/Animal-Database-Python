from tkinter import *

m = Tk() #window
m.minsize(200, 200) #set minimum size of the window
m.resizable(0, 0) #prevents the user to change the size of the window
m.title("Main Window") #window's name

#scrollbar
scroll = Scrollbar(m)

#listbox
list_con = Listbox(m, selectmode = MULTIPLE, width = 10, yscrollcommand = scroll.set)
for i in range(50):
    if i % 2 == 0:
        list_con.insert(1, "North America")
    elif i % 3 == 0:
        list_con.insert(2, "South America")
    elif i % 5 == 0:
        list_con.insert(3, "Europe")
    elif i % 7 == 0:
        list_con.insert(4, "Asia")
    else:
        list_con.insert(5, "Africa")
list_con.pack(side = LEFT, fill = BOTH)
scroll.config(command = list_con.yview)
#scroll.place(x = 90, y = 0, height = 200)
scroll.pack(side = RIGHT, fill = BOTH)

m.mainloop()
