from Display_Page import Display_Page
class Search:

    def __init__(self, list):
        #Constructor
        #takes the search_type to determine which search type to run
        #input: database's list, search type, name (animal's name or continent)
        #dict = {'C LYNX': [(['north america'], []), 'carnivore', 'LC'], 'E LYNX': [(['europe'], []), 'carnivore', 'LC'], 'I LYNX': [(['europe'], []), 'carnivore', 'CR'], 'A LYNX': [(['asia'], []), 'carnivore', 'EX'], 'S LYNX': [(['south america'], []), 'carnivore', 'EX'], 'A2 LYNX': [(['asia'], []), 'carnivore', 'EX'], 'EURASIAN LYNX': [(['europe'], ['spain']), 'carnivore', 'LC']}
        print("----------------------- Search -----------------------")
        print("------------------------------------------------------")
        self.asking_searchType(list)

    def asking_searchType(self, list):
        #asks the user which search type they want to run
        #input: database's list
        print("Search Type:")
        print("name --> searches the database by animal name")
        print("continent --> searches the database by continent")
        search_type = input("Enter a search type")
        while search_type.lower() != "name" and search_type.lower() != "continent":
            print("Incorrect input")
            search_type = input("Enter a search type")
        if search_type.lower() == "name":
            self.search_byName(list)
        else:
            self.search_byContinent(list)

    def search_byName(self, list):
        #uses the name and searches the database by animal's name and then displays a list of possible animals
        #input: database's list
        name = input("Enter an animal's name to search")
        print()
        print("---------------------- Results -----------------------")
        results = [] #list of all animals that fit the search
        for obj in list: #adds animals that fit the search into results list
            animal_name = obj.get_Name()
            if name.upper() in animal_name:
                results.append(animal_name)
        count = 1 #makes sure 4 animals are printed in one line
        animal_inDatabase = False #tracks if such animal exists in the database or not
        for animal in results:
            if count < 5:
                print(animal, end= "        ")
                animal_inDatabase = True
                count += 1
            if count == 5:
                count = 1
                print()
        print()
        if animal_inDatabase == False:
            print("SUCH ANIMAL DOES NOT EXIST IN THIS DATABASE")
        else:
            self.confirm_search(list)

    def search_byContinent(self, list):
        #uses the name and searches the database by continent and then displays a list of possible animals
        #input: database's list
        continent_list = ["north america", "south america", "europe", "africa", "asia", "australia", "antarctica"]
        continent = input("Enter the continent")
        while continent.lower() not in continent_list:
            print("Incorrect input")
            continent = input("Enter the continent")
        print()
        print("---------------------- Results -----------------------")
        results = [] #list of all animals that fit the search
        for obj in list: #adds animals that fit the search into results list
            animal_habitat_info = obj.get_Habitat_info()
            if continent in animal_habitat_info[0]:
                results.append(obj.get_Name())
        count = 1 #makes sure 4 animals are printed in one line
        animal_inDatabase = False #tracks if such animal exists in the database or not
        for animal in results:
            if count < 5:
                print(animal, end= "        ")
                #print(animal)
                animal_inDatabase = True
                count += 1
            if count == 5:
                count = 1
                print()
        print()
        if animal_inDatabase == False:
            print("NO ANIMAL EXISTS IN THSI CONTINENT IN THIS DATABASE")
        else:
            self.confirm_search(list)

    def confirm_search(self, list):
        #using the list displayed, asks user to enter animal's name again to confirm the search
        #input: database's list
        print("------------------------------------------------------")
        print("------------------------------------------------------")
        print()
        animal_name_list = []
        for i in range(len(list)):
            animal_name_list.append(list[i].get_Name())
        name = input("Enter the animal's you want to learn about in the results to confirm your search")
        while name.upper() not in animal_name_list:
            print("Incorrect input")
            name = input("Enter the animal's you want to learn about in the results to confirm your search")
        print()
        Display_Page(list, name.upper(), "search")


