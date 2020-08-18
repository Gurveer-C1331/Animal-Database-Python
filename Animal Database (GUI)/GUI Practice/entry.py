from tkinter import *

m = Tk() #window
m.minsize(200, 200) #set minimum size of the window
m.resizable(0, 0) #prevents the user to change the size of the window
m.title("Main Window") #window's name

def text_enter():
    print(entry_1.get())
    user_input = entry_1.get()
    error = Label(m, text = "Incorrect entry")
    correct = Label(m, text = "Correct entry")
    if user_input.lower() != "north america":
        error.place(x = 0, y = 80)
    else:
        correct.place(x = 0, y = 80)

def clear_text():
    entry_1.delete(0, 'end')

#entry
entry_1 = Entry(m)
entry_1.place(x = 0, y = 0)

#button
enter = Button(m, text = "Enter", command = text_enter)
enter.place(x = 0, y = 40)

clear = Button(m, text = "Clear", command = clear_text)
clear.place(x = 50, y = 40)

stop = Button(m, text = "Stop", command = m.destroy)
stop.place(x = 0, y = 60)

m.mainloop()