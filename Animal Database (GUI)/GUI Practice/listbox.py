from tkinter import *

m = Tk() #window
m.minsize(200, 200) #set minimum size of the window
m.resizable(0, 0) #prevents the user to change the size of the window
m.title("Main Window") #window's name

def con_selection():
    tuple_con = list_con.curselection()
    for i in range(len(tuple_con)):
        print(continent_list[tuple_con[i]])

continent_list = ["north america", "south america", "europe", "africa", "asia", "australia", "antarctica", "done"]
#listbox
list_con = Listbox(m, selectmode = MULTIPLE, width = 10)
for i in range(len(continent_list)):
    if i != len(continent_list)-1:
        list_con.insert(i, continent_list[i])
list_con.pack(side = TOP)

#button
enter = Button(m, text = "Enter", command = con_selection)
enter.pack(side = BOTTOM)

m.mainloop()

