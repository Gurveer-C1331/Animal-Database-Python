from Create_Animal import Create_Animal
from Animal_List import Animal_List
from Search import Search
from Display_Page import Display_Page
from Save_Load_Database import Save_Load_Database
from tkinter import *
class Main_Menu:
    ##Constructor
    ##Runs the welcome function
    def __init__(self, w):
        self.window = w #main window
        self.window.geometry("800x500") #window size
        self.window.title("Animal Database")

        #Creates Animal_List object 'animal_list'
        self.animal_list = Animal_List()
        self.welcome()
    
    ##this function runs the main menu of the Animal Database
    def main(self):
        #destroy instructions page
        self.frame_instructions.destroy()
        #create the main menu frame
        self.frame_main = Frame(self.window)
        self.frame_main.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #title for the page ("Animal Database")
        title = Label(self.frame_main, text = "\nAnimal Database", font = ("Gobold", "40"))
        title.pack()
        
        #buttons
        #add button
        add_b = Button(self.frame_main, text = "Add", command = self.add)
        add_b.place(x = 250, y = 140, width = 300, height = 40)
        #remove button
        remove_b = Button(self.frame_main, text = "Remove", command = self.remove)
        remove_b.place(x = 250, y = 190, width = 300, height = 40)
        #search button
        search_b = Button(self.frame_main, text = "Search", command = self.search)
        search_b.place(x = 250, y = 240, width = 300, height = 40)
        #display button
        display_b = Button(self.frame_main, text = "Display", command = self.display)
        display_b.place(x = 250, y = 290, width = 300, height = 40)
        #exit button
        exit_b = Button(self.frame_main, text = "Exit", command = self.exit)
        exit_b.place(x = 10, y = 450, width = 100, height = 40) 

    ##this function runs the start menu of the Animal Database
    ##talks about the function and purpose of the Animal Database
    def welcome(self):
        #create welcome frame
        self.frame_welcome = Frame(self.window)
        self.frame_welcome.place(x = 0, y = 0, width = 800, height = 500)
        #welcome title ("Welcome to the Animal Database")
        welcome_title = Label(self.frame_welcome, text = "\n\n\n\nWelcome\nto the\nAnimal Database\n", font = ("Gobold", "30"))
        welcome_title.pack()
        #continue button
        cont_b = Button(self.frame_welcome, text = "Continue", activeforeground = 'blue', command = self.instructions)
        cont_b.place(x = 350, y = 300, width = 100, height = 40)

        #loads the existing list of the database and adds it to the animal_list (object) using addList function
        self.animal_list.addList(Save_Load_Database.load_Database("", self.animal_list.getList()))

    ##this function represents the instruction page of the Animal Database
    ##displays the instructions
    def instructions(self):
        #destroy welcome page
        self.frame_welcome.destroy()
        #create instruction's frame
        self.frame_instructions = Frame(self.window)
        self.frame_instructions.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #instructions title ("Instructions")
        instructions_title = Label(self.frame_instructions, text = "\nInstructions", font = ("Gobold", "30"))
        instructions_title.pack()
        #instructions (text)
        inst_text = '''\nSearching
        There are 2 ways to search for an animal
        One way is searching by name and the other is to search by continent
        By entering the keyword 'search', the search function will be brought up
        \nAdding
        The add function allows you to enter an animal that is not inside the database
        By entering the keyword 'add', the add function will be brought up
        \nRemoving:
        By entering 'remove', you can remove an incorrect entry in the database
        \nDisplay:
        By entering 'display', you can display the database information
        \nExiting:
        By entering 'exit', you can exit the database and save the progress\n\n''' 
        instructions = Label(self.frame_instructions, text = inst_text)
        instructions.pack()
        #next button
        next_b = Button(self.frame_instructions, text = "Next", command = self.main)
        next_b.place(x = 350, y = 420, width = 100, height = 40)
        
    ##this function would launch the adding interface of the Animal Database
    ##allows the user to add animals into the database
    def add(self):
        #destroy main page fram
        Create_Animal(self.window, self.animal_list.getList())

    ##this function would launch the removing interface of the Animal Database
    ##allows the user to remove an incorrect entry to the database
    def remove(self):
        self.animal_list.remove_animal(self.window)

    ##this function would launch the search interface of the Animal Database
    ##allows the user to search the database for an animal in the database
    def search(self):
        Search(self.window, self.animal_list.getList())

    ##this function would lauch the diplay interface of the Animal Database
    ##allows the user to display the Animal Database
    def display(self):
        Display_Page(self.window, self.animal_list.getList(), "", "")
    
    ##this function saves the database's list and exits from the Animal Database interface
    def exit(self):
        Save_Load_Database.save_Database("", self.animal_list.getList())
        self.window.destroy()
    
main_window = Tk() #the main window for the Animal Database interface
Animal_database = Main_Menu(main_window) #launching the Animal Database interface
main_window.mainloop()

