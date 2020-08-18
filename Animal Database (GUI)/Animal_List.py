from tkinter import *
class Animal_List:

    def __init__(self):
        self.animal_list = []
        
    def getList(self):
        #returns the list of the database
        return self.animal_list
    
    def addList(self, list):
        #adds a list (used to load the database's list)
        self.animal_list = list
    
    def remove_animal(self, window):
        #allows the user to remove an incorrect entry in the database
        window = window
        animal = ""
        self.animal_obj = None
        def remove_clicked():
            animal = entry_remove.get()
            animal_inDatabase = False
            for obj in self.animal_list:
                animal_name = obj.get_Name()
                if animal.upper() == animal_name:
                    self.animal_obj = obj
                    animal_inDatabase = True
            if animal_inDatabase == False:
                error.config(text = "Animal entered does not exist in the database")
                error.place(x = 200, y = 200, width = 400)
                confirm_b.place_forget()
            else:
                error.config(text = "Animal exists in the database, click 'Confirm' to remove the entry")
                error.place(x = 200, y = 200, width = 400)
                confirm_b.place(x = 350, y = 340, width = 100, height = 40)

        def confirm_clicked():
            self.animal_list.remove(self.animal_obj)
            remove_b.place_forget()
            confirm_b.place_forget()
            error.config(text = "Animal has successfully been removed from the database")
        
        def home_clicked():
            frame_removePage.destroy()
            
        #creating frame for removing an animal entry
        frame_removePage = Frame(window)
        frame_removePage.place(x = 0, y = 0, width = 800, height = 500)
        #title for the page
        title = Label(frame_removePage, text = "\nREMOVE\n", font = ("Gobold", "30"))
        title.pack()
        #entry to remove animal 
        entry_remove = Entry(frame_removePage)
        entry_remove.place(x = 300, y = 250, width = 200)
        #remove button 
        remove_b = Button(frame_removePage, text = "Remove", command = remove_clicked)
        remove_b.place(x = 350, y = 290, width = 100, height = 40)
        #confirm button 
        confirm_b = Button(frame_removePage, text = "Confirm", command = confirm_clicked)
        #error message
        error = Label(frame_removePage, text = "")

        #home button
        home_b = Button(frame_removePage, text = "Home", command = home_clicked)
        home_b.place(x = 350, y = 430, width = 100, height = 40)

        window.mainloop()
        """ print("----------------------- Remove -----------------------")
        print("------------------------------------------------------")
        animal_inDatabase = False #keeps track if the database contains the animal entered or not
        animal = input("Enter the animal's name you want to remove from the database")
        confirm = input("Type in 'yes' or 'no' to confirm the removal")
        if confirm.lower() == "yes":
            for obj in self.animal_list:
                animal_name = obj.get_Name()
                if animal.upper() == animal_name:
                    animal_inDatabase = True
                    self.animal_list.remove(obj)
            if animal_inDatabase == False:
                print("This animal does not exit in the database")
            else:
                print("The animal has been removed")
        print("------------------------------------------------------")
        print("------------------------------------------------------")
        print() """