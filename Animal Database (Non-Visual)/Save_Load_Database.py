from Animal import Animal
import ast
class Save_Load_Database:

    def __init__(self, list, action):
        #Constructor
        #takes the action variable to determine if the database is being saved or loaded
        #input: database's list, action type
        if action.lower() == "save":
            self.save_Database(list)
        else:
            self.load_Database(list)
    
    def save_Database(self, list):
        #saves the database's list in a text file
        #input: database's list
        animal_dict = {}
        for obj in list: #create a list to hold all the information entered to the database
            habitat = obj.get_Habitat_info()
            diet_type = obj.get_Diet_info()
            con_status = obj.get_Conservation_info()
            animal_info = []
            animal_info.append(habitat)
            animal_info.append(diet_type)
            animal_info.append(con_status)
            animal_dict[obj.get_Name()] = animal_info #creates a new entry to the list            
        print(animal_dict)
        s_dict = str(animal_dict)
        nameHandle = open(r"Animal Database (Non-Visual) (Animal as objects)\Animal_database", "w")
        nameHandle.write(s_dict)
    
    def load_Database(self, list):
        #loads the database's list from a text file and returns the list
        #input: database's list
        nameHandle = open(r"Animal Database (Non-Visual) (Animal as objects)\Animal_database", "r")
        s_dict = nameHandle.read()
        d_dict = ast.literal_eval(s_dict) #converts the string containing the list into a list
        animal_list = []
        for animal in d_dict:
            animal_info = d_dict[animal]
            obj = Animal(animal)
            habitat_info = animal_info[0]
            obj.add_Habitat_info(habitat_info[0], habitat_info[1])
            obj.add_Diet_info(animal_info[1])
            obj.add_Conservation_info(animal_info[2])
            animal_list.append(obj) #adds the Animal object to the list
        return animal_list