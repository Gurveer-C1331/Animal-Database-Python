from tkinter import *
from w2 import w2
class w:

    def __init__(self, window):
        self.w = window
        self.play()

    def play(self):
        self.w.geometry("800x500")
        self.w.title("A")
        frame = Frame(self.w)
        frame.place(x = 0, y = 0, width = 800, height = 500)
        
        conStatus_list = ["Least Concern (LC)", "Near Threatened (NT)", "Vulnerable (VU)", "Endangered (EN)", "Critically Endangered (CR)", "Extinct in the Wild (EW)", "Extinct (EX)"]
        cStatus = StringVar()
        cStatus.set(conStatus_list[0])
        opt = OptionMenu(frame, cStatus, *conStatus_list)
        opt.place(x = 300, y = 200, width = 200)

        b = Button(frame, text = "hhh", command = self.next)
        b.pack()

    def next(self):
        w2()

window = Tk()
w(window)
window.mainloop()