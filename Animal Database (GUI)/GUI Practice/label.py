from tkinter import *
from PIL import Image, ImageTk

m = Tk() #window
m.minsize(200, 200) #set minimum size of the window
m.resizable(0, 0) #prevents the user to change the size of the window
m.title("Main Window") #window's name

#label (text)
label_Hello = Label(m, font = ("Times New Roman", "25", "bold"), text = "Hello")
label_Hello.place(x = 0, y = 0, height = 50, width = 60)

#label (image) Method 1
""" venom = PhotoImage(file = "Carnage1.png")
label_Venom = Label(m, image = venom)
label_Venom.place(x = 0, y = 0) """

#label (image) Method 2
""" load = Image.open("Carnage1.png")
w = int(load.size[0]*.045)
h = int(load.size[1]*.045)
load = load.resize((w, h))
render = ImageTk.PhotoImage(load)
img = Label(m, image=render)
img.image = render
img.place(x=0, y=0) """

m.mainloop()