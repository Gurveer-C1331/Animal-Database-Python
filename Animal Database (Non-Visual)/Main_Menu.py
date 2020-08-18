from Create_Animal import Create_Animal
from Search import Search
from Display_Page import Display_Page
from Save_Load_Database import Save_Load_Database
class Main_Menu:
    
    def __init__(self):
        #Constructor
        #Runs the welcome function
        #Creates Create_Animal object 'animal_list'
        self.animal_list = Create_Animal()
        self.welcome()

    def main(self):
        #this function respresents the main menu of the Animal Database
        enter = input("enter a keyword to learn about an animal")
        inputs = ["add", "remove", "search", "display", "instructions", "exit"] #list of valid inputs
        while enter.lower() not in inputs:
            print("Incorrect input")
            enter = input("enter a keyword to learn about an animal")
        if enter.lower() == "add":
            self.add()
        elif enter.lower() == "remove":
            self.remove()
        elif enter.lower() == "search":
            self.search()
        elif enter.lower() == "display":
            self.display()
        elif enter.lower() == "instructions":
            self.instructions()
        elif enter.lower() == "exit":
            self.exit() 

    def welcome(self):
        #this function represents the start menu of the Animal Database
        #talks about the function and purpose of the Animal Database
        print("----------- Welcome to the Animal Database ------------")
        print("------------------------------------------------------")
        print("This database contains information of different animals around the world")

        enter = input("enter 'instructions' to understand how to nagivate the database")
        while enter.lower() != "instructions":
            print("Incorrect input")
            enter = input("enter instructions to understand how to nagivate the database")
        #loads the existing list of the database and adds it to the animal_list (object) using addList function
        self.animal_list.addList(Save_Load_Database.load_Database(self.animal_list.getList(), "load"))
        self.instructions()

    def instructions(self):
        #this function represents the instruction page of the Animal Database
        #displays the instructions
        print("-------------------- Instructions --------------------")
        print("------------------------------------------------------")
        print("Searching:")
        print("There are 2 ways to search for an animal")
        print("One way is searching by name and the other is to search by continent")
        print("By entering the keyword 'search', the search function will be brought up")
        print("Adding:")
        print("The add function allows you to enter an animal that is not inside the database")
        print("By entering the keyword 'add', the add function will be brought up")
        print("Removing:")
        print("By entering 'remove', you can remove an incorrect entry in the database")
        print("Display:")
        print("By entering 'display', you can display the database information")
        print("Exiting:")
        print("By entering 'exit', you can exit the database and save the progress")
        print("------------------------------------------------------")
        print("------------------------------------------------------")
        print()
        self.main() 
    
    def add(self):
        #this function would launch the adding interface of the Animal Database
        #allows the user to add animals into the database
        self.animal_list.create_Animal() #runs the adding animal function
        #calls the Display_Page class and prints the list (prints the list of the object 'animal_list')
        Display_Page(self.animal_list.getList(), "", "list1")
        self.main()

    def remove(self):
        #this function would launch the removing interface of the Animal Database
        #allows the user to remove an incorrect entry to the database
        self.animal_list.remove_animal(self.animal_list.getList())
        self.main()

    def search(self):
        #this function would launch the search interface of the Animal Database
        #allows the user to search the database for an animal in the database
        Search(self.animal_list.getList())
        self.main()

    def display(self):
        #this function would lauch the diplay interface of the Animal Database
        #allows the user to display the Animal Database
        Display_Page(self.animal_list.getList(), "", "")
        self.main()
    
    def exit(self):
        #this function saves the database's list
        Save_Load_Database(self.animal_list.getList(), "save")

Animal_database = Main_Menu()
