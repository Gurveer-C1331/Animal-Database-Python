class Display_Page:

    def __init__(self, list, name, display_type):
        #Constructor
        #takes the display_type and does the appropriate display type (used for me to check list)
        #input: database's list, animal's name, display type
        print("---------------------- Display -----------------------")
        print("------------------------------------------------------")
        if display_type == "search" and name != "": #calls to display animal page
            self.display_animalPage(list, name.upper())
        elif display_type == "": #calls to ask user which display type they want
            self.asking_displayType(list)
        elif display_type == "list1": #calls the print the list
            self.display_list(list)
        print("------------------------------------------------------")
        print("------------------------------------------------------")
        print()

    def asking_displayType(self, list):
        #Acts as another constructor if no display_type is given when class is called
        #asks the user the display type they want if not given (used for the user)
        #input: database's list
        print("Display Type:")
        print("list1 --> displays the list") #might remove later
        print("list2 --> displays the list of animals")
        display_type = input("Enter a display type")
        print()
        while display_type.lower() != "list1" and display_type.lower() != "list2":
            print("Incorrect input")
            display_type = input("Enter a display type")
        if display_type == "list1":
            self.display_list(list)
        elif display_type == "list2":
            self.display_listofAnimals(list)
    
    def display_animalPage(self, list, name):
        #Acts as another constructor if display_type given is 'search' along with animal name
        #displays the individual animal page
        #input: database's list, animal's name
        habitat_list = None 
        diet_type = None
        conservation_status = None
        for i in range(len(list)):
            if name.upper() == list[i].get_Name():
                habitat_list = list[i].get_Habitat_info()
                diet_type = list[i].get_Diet_info()
                conservation_status = list[i].get_Conservation_info()

        continent = habitat_list[0]
        countries = habitat_list[1]
        self.print_dashlineLong(name.upper())
        print("-- Habitat --")
        print("Continent(s): ", end="")
        self.print_list(continent)
        print("Countries: ", end="")
        self.print_list(countries)
        print("-- Diet Type --")
        print(diet_type)
        print("-- Conservation Status --")
        print(conservation_status)

    def print_list(self, list):
        #prints the list of continents and countries the animal is from
        #input: list of continents/countries
        for con in list:
            print(con, end=", ")
        print()

    def display_list(self, list):
        #prints out the list of the database
        #input: database's list
        print("-- List --")
        print(list)

    def display_listofAnimals(self, list):
        #prints out a list of all the animals in the Animal Database
        #input: database's list
        print("------------------------ List ------------------------")
        list_animals = []
        for i in range(len(list)):
            list_animals.append(list[i].get_Name())
        list_animals.sort() #sorts the list of animal names alphabetically
        for animal in list_animals:
            print(animal)

    def print_dashlineLong(self, title_name):
        #prints out the dashline header (long version)
        #input: header's title
        line = "------------------------------------------------------"
        half_length = int((len(line)-(len(title_name)+2))/2)
        for i in range((len(line)-(len(title_name)+2))+1):
            if i == half_length:
                print(" "+title_name.upper()+" ",end="")
            else:
                print("-",end="")
        print()
    
    
    
