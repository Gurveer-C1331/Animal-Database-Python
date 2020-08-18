from tkinter import *
class w2:

    def __init__(self):
        self.w2 = Toplevel()
        self.w2.geometry("800x500")
        self.w2.title("s")
        self.play2()
        self.w2.mainloop()

    def play2(self):
        self.frame2 = Frame(self.w2)
        self.frame2.place(x = 0, y = 0, width = 800, height = 500)
        conStatus_list = ["Least Concern (LC)", "Near Threatened (NT)", "Vulnerable (VU)", "Endangered (EN)", "Critically Endangered (CR)", "Extinct in the Wild (EW)", "Extinct (EX)"]
        cStatus = StringVar()
        cStatus.set(conStatus_list[0])
        opt = OptionMenu(self.frame2, cStatus, *conStatus_list)
        opt.place(x = 300, y = 200, width = 200)

        exit = Button(self.frame2, text = "exit", command = self.exit)
        exit.pack()

    def exit(self):
        self.frame2.destroy()
        self.w2.destroy()

