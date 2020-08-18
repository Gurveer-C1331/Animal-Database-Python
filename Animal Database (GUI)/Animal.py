class Animal:

    def __init__(self, name):
        #Constructor
        self.name = name

    def add_Habitat_info(self, continent, country):
        #adds the habitat information to the animal
        self.continent = continent
        self.country = country
    
    def add_Animal_class(self, animal_class):
        #adds the animal class to the animal
        self.animal_class = animal_class

    def add_Diet_info(self, diet_type):
        #adds the diet information to the animal
        self.diet_type = diet_type
    
    def add_Conservation_info(self, con_status):
        #adds the conservation information to the animal
        self.con_status = con_status
    
    def add_Image(self, image_path):
        #adds the image path information to the animal
        self.image_path = image_path

    def get_Name(self):
        #returns the name of the animal
        return self.name
        
    def get_Habitat_info(self):
        #returns the habitat information
        return (self.continent, self.country)
    
    def get_Animal_class(self):
        #returns the animal class
        return self.animal_class

    def get_Diet_info(self):
        #returns the diet information
        return self.diet_type

    def get_Conservation_info(self):
        #returns the conservation information
        return self.con_status

    def get_Image(self):
        #returns the image path
        return self.image_path

