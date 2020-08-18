from Animal import Animal
class Create_Animal:

    def __init__(self):
        #Constructor
        #Creates a list for the object that contains the animal information
        self.animal_list = []

    def create_Animal(self):
        #allows the user to add in a new animal
        #creates a new Animal object
        print("------------------------ Add -------------------------")
        print("------------------------------------------------------")
        animal_name = self.ask_Animal_name() 
        animal = Animal(animal_name) #new Animal object is created
        animal.add_Habitat_info(self.add_continent(), self.add_country())
        animal.add_Diet_info(self.add_dietType())
        animal.add_Conservation_info(self.add_conservationStatus())
        self.animal_list.append(animal) #adds the animal's name to the list
        print("New animal entry is successful")
        print("------------------------------------------------------")
        print("------------------------------------------------------")
        print()

    def ask_Animal_name(self):
        #asks the user to enter a new animal's name
        animal_name = input("Enter the name of the animal")
        while self.check_Animal(animal_name, self.animal_list) == False:
            print("This animal already exists in the database")
            animal_name = input("Enter the name of the animal")
        return animal_name.upper()

    
    def check_Animal(self, name, list):
        #checks if the animal the user entered is already in the database or not
        #input: animal's name, database's list
        for obj in list:
            if name.upper() == obj.get_Name():
                return False 
        return True
    
    def add_continent(self):
        #allows the user to enter the continent(s) the animal is from
        print("---------------------- Habitat -----------------------")
        print("--------------------- Continent ----------------------")
        continent_list = ["north america", "south america", "europe", "africa", "asia", "australia", "antarctica", "done"]
        continents = []
        continent = ""
        while continent.lower() != "done":
            continent = input("Enter the continent the animal is from or enter 'done' when finished")
            while continent.lower() not in continent_list:
                print("Incorrect input")
                continent = input("Enter the continent the animal is from or enter 'done' when finished")
            if continent.lower() != "done" and continent not in continents:
                continents.append(continent)
            elif continent in continents:
                print("This continent has already been entered")
        return continents

    def add_country(self):
        #allows the user to enter the country the animal is from
        print("---------------------- Country -----------------------")
        countries = []
        country = input("Enter the country(ies) the animal is from (when you're finished enter 'done'")
        while country.lower() != "done":
            if country in countries:
                print("This country has already been entered")
            else:
                countries.append(country)
            country = input("Enter the country(ies) the animal is from (when you're finished enter 'done'")
        return countries
    
    
    def add_dietType(self):
        #allows the user to enter the diet type of the animal
        print("--------------------- Diet Type ----------------------")
        print("Carnivore --> meat eater")
        print("Omnivore --> both meat and plant eater")
        print("Herbivore --> plant eater")
        diet_type = input("Enter a diet type")
        while diet_type.lower() != "carnivore" and diet_type.lower() != "omnivore" and diet_type.lower() != "herbivore":
            print("Incorrect input")
            diet_type = input("Enter a diet type")
        return diet_type.lower()

    def add_conservationStatus(self):
        #allows the user to enter the population/conservation status of the animal
        print("---------------- Conservation Status -----------------")
        print("LC --> Least Concern")
        print("NT --> Near Threatened")
        print("VU --> Vulnerable")
        print("EN --> Endangered")
        print("CR --> Critically Endangered")
        print("EW --> Extinct in the Wild")
        print("EX --> Extinct")
        c_s = ["LC", "NT", "VU", "EN", "CR", "EW", "EX"]
        con_status = input("Enter a conservation status short form")
        while con_status.upper() not in c_s:
            print("Incorrect input")
            con_status = input("Enter a conservation status short form")
        return con_status.upper()

    def remove_animal(self, list):
        #allows the user to remove an incorrect entry in the database
        print("----------------------- Remove -----------------------")
        print("------------------------------------------------------")
        animal_inDatabase = False #keeps track if the database contains the animal entered or not
        animal = input("Enter the animal's name you want to remove from the database")
        confirm = input("Type in 'yes' or 'no' to confirm the removal")
        if confirm.lower() == "yes":
            for obj in list:
                animal_name = obj.get_Name()
                if animal.upper() == animal_name:
                    animal_inDatabase = True
                    list.remove(obj)
            if animal_inDatabase == False:
                print("This animal does not exit in the database")
            else:
                print("The animal has been removed")
        print("------------------------------------------------------")
        print("------------------------------------------------------")
        print()

    def getList(self):
        #returns the list of the database
        return self.animal_list
    
    def addList(self, list):
        #adds a list (used to load the database's list)
        self.animal_list = list



