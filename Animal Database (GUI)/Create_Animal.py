from Animal import Animal
from tkinter import *
from tkinter import filedialog
import os

class Create_Animal():

    ##Constructor
    ##input: window (brings the main window over to this class), list (a list that contains Animal objects that have been created)
    def __init__(self, window, list):
        self.animal_list = list #class's list variable
        self.animal = None #variable to hold the Animal object that is later created

        self.window = window
        self.window.geometry("800x500")
        self.ask_Animal_name()
        self.window.mainloop()
    
    ##creates an interface where the user can enter a new animal's name
    def ask_Animal_name(self):
        def enter_clicked(): #when the enter button is clicked
            a_name = entry_animalName.get()
            if self.check_Animal(a_name, self.animal_list) == False: #if the animal name entered isn't already in the Database
                error.config(text = "This animal already exists, enter another animal again") #change error message
                cont_b.place_forget()
            else:
                self.animal = Animal(a_name.upper()) #create a new Animal object
                error.config(text = "This is a new animal, click continue") #change error message
                cont_b.place(x = 350, y = 350, width = 100, height = 40)

        def home_clicked(): #when the home button is clicked
            self.frame_addName.destroy() 
            
        #creates the frame for the adding name
        self.frame_addName = Frame(self.window)
        self.frame_addName.place(x = 0, y = 0, width = 800, height = 500)
        #title for the page ("ADD (Name)")
        title = Label(self.frame_addName, text = "\nADD\n(Name)", font = ("Gobold", "30"))
        title.pack()
        #entry to enter the animal's name
        entry_animalName = Entry(self.frame_addName)
        entry_animalName.place(x = 300, y = 250, width = 200)
        #enter button
        enter_b = Button(self.frame_addName, text = "Enter", command = enter_clicked)
        enter_b.place(x = 350, y = 300, width = 100, height = 40)
        #error label
        error = Label(self.frame_addName)
        error.place(x = 200, y = 200, width = 400)
        #continue button
        cont_b = Button(self.frame_addName, text = "Continue", command = self.add_continent)

        #home button
        home_b = Button(self.frame_addName, text = "Home", command = home_clicked)
        home_b.place(x = 350, y = 430, width = 100, height = 40)
    
    ##checks if the animal the user entered is already in the database or not
    ##input: name (animal name user entered), list (a list that contains Animal objects that have been created)
    def check_Animal(self, name, list):
        for obj in list:
            if name.upper() == obj.get_Name():
                return False 
        return True

    ##creates an interface where the user can enter the continent(s) the animal is from
    def add_continent(self):
        self.continents = [] #holds the information for continents
        def enter_clicked_continent(): #when the enter button is clicked 
            continents_selected = list_con.curselection()
            con_str = "You selected " #contains string of the continents selected
            for i in range(len(continents_selected)): #adds the continent information entered into the continent list
                self.continents.append(continent_list[continents_selected[i]])
                con_str = con_str[:] + continent_list[continents_selected[i]] + ", "                
            enter_b.place_forget()
            select_state.config(text = con_str)
            select_state.place(x = 0, y = 380, width = 800)
            cont_b.place(x = 350, y = 420, width = 100, height = 40)

        #destroy previous adding page frame
        self.frame_addName.destroy()
        #create frame for adding habitat information
        self.frame_addContinent = Frame(self.window)
        self.frame_addContinent.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #title for the page ("ADD (Habitat)")
        title = Label(self.frame_addContinent, text = "\nADD\n(Habitat)", font = ("Gobold", "30"))
        title.pack()
        #subtitle ("Continents")
        subt_cont = Label(self.frame_addContinent, text = "Continents", font = ("Gobold", "20"))
        subt_cont.place(x = 300, y = 150, width = 200)
        #listbox (options for continents)
        continent_list = ["North America", "South America", "Europe", "Africa", "Asia", "Australia", "Antarctica"] #list of all possible options
        list_con = Listbox(self.frame_addContinent, selectmode = MULTIPLE)
        for i in range(len(continent_list)):
            list_con.insert(i, continent_list[i])
        list_con.place(x = 300, y = 190, width = 200)
        #enter button 
        enter_b = Button(self.frame_addContinent, text = "Enter", command = enter_clicked_continent)
        enter_b.place(x = 350, y = 380, width = 100, height = 40)
        #selection statement (displays the selection the user made)
        select_state = Label(self.frame_addContinent)
        #continue button
        cont_b = Button(self.frame_addContinent, text = "Continue", command = self.add_country)

    ##creates an interface where the user can enter the countries the animal is from
    def add_country(self):
        countries = [] #holds the information for countries
        def add_clicked_country(): #when add button is clicked
            if entry_country.get().capitalize() not in countries: #if the country entered is a duplicate or not
                countries.append(entry_country.get().capitalize())
                error.place_forget()
            else:
                error.place(x = 200, y = 200, width = 400)
        def enter_clicked_country(): #when the enter button is clicked 
            self.animal.add_Habitat_info(self.continents, countries) #adds the habitat attribute to the Animal object
            enter_b.place_forget()
            add_b.place_forget()
            cont_b.place(x = 350, y = 420, width = 100, height = 40)

        #destroy previous adding page frame
        self.frame_addContinent.destroy()
        #create frame for adding habitat information
        self.frame_addCountry = Frame(self.window)
        self.frame_addCountry.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #title for the page ("ADD (Habitat)")
        title = Label(self.frame_addCountry, text = "\nADD\n(Habitat)", font = ("Gobold", "30"))
        title.pack()
        #subtitle ("Countries")
        subt_coun = Label(self.frame_addCountry, text = "Countries", font = ("Gobold", "20"))
        subt_coun.place(x = 300, y = 150, width = 200)
        #entry to add countries 
        entry_country = Entry(self.frame_addCountry)
        entry_country.place(x = 300, y = 250, width = 200)
        #add button (to allow more than one country to be added)
        add_b = Button(self.frame_addCountry, text = "Add", command = add_clicked_country)
        add_b.place(x = 350, y = 290, width = 100, height = 40)
        #enter button 
        enter_b = Button(self.frame_addCountry, text = "Enter", command = enter_clicked_country)
        enter_b.place(x = 350, y = 340, width = 100, height = 40)
        #error message
        error = Label(self.frame_addCountry, text = "You have already entered this country")
        #continue button
        cont_b = Button(self.frame_addCountry, text = "Continue", command = self.add_animalClass)

    ##creates an interface where the user can enter the animal class of the animal
    def add_animalClass(self):
        animalClass_list = ["Mammal", "Birds", "Reptile", "Amphibians", "Fish"] #list of all possible options for animal class
        def enter_clicked_animalClass(): #when the enter button is clicked for animal class
            self.animal.add_Animal_class(aClass.get()) #adds animal class attribute to the Animal object
            select_state.config(text = "You selected " + aClass.get())
            select_state.place(x = 300, y = 380, width = 200)
            enter_b.place_forget()
            cont_b.place(x = 350, y = 420, width = 100, height = 40)

        #destroy previous adding page frame
        self.frame_addCountry.destroy()
        #create frame for adding animal class
        self.frame_addAClass = Frame(self.window)
        #self.frame_addAClass.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        self.frame_addAClass.place(x = 0, y = 0, width = 800, height = 500)
        #title for the page ("ADD")
        title = Label(self.frame_addAClass, text = "\nADD", font = ("Gobold", "30"))
        title.pack()
        #subtitle ("Animal Class")
        subtitle = Label(self.frame_addAClass, text = "Animal Class", font = ("Gobold", "20"))
        subtitle.place(x = 300, y = 150, width = 200)
        #optionmenu (option for animal class)
        aClass = StringVar()
        aClass.set(animalClass_list[0])
        opt = OptionMenu(self.frame_addAClass, aClass, *animalClass_list)
        opt.place(x = 300, y = 200, width = 200)
        #enter button
        enter_b = Button(self.frame_addAClass, text = "Enter", command = enter_clicked_animalClass)
        enter_b.place(x = 350, y = 340, width = 100, height = 40)
        #selection statement (displays the selection the user made)
        select_state = Label(self.frame_addAClass)
        #continue button
        cont_b = Button(self.frame_addAClass, text = "Continue", command = self.add_dietType)
    
    ##creates an interface where the user can enter the diet type of the animal
    def add_dietType(self):
        diettype_list = ["Carnivore", "Herbivore", "Omnivore"] #list of all possible options for diet type
        def enter_clicked_dietType(): #when the enter button is clicked
            self.animal.add_Diet_info(dType.get()) #adds diet type attribute to the Animal object
            select_state.config(text = "You selected " + dType.get())
            select_state.place(x = 300, y = 380, width = 200)
            enter_b.place_forget()
            cont_b.place(x = 350, y = 420, width = 100, height = 40)

        #destroy previous adding page frame
        self.frame_addAClass.destroy()
        #create frame for adding diet type
        self.frame_addDType = Frame(self.window)
        self.frame_addDType.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #title for the page ("ADD (Diet)")
        title = Label(self.frame_addDType, text = "\nADD\n(Diet)", font = ("Gobold", "30"))
        title.pack()
        #subtitle ("Diet Type")
        subtitle = Label(self.frame_addDType, text = "Diet Type", font = ("Gobold", "20"))
        subtitle.place(x = 300, y = 150, width = 200)
        #optionmenu (option for diet type)
        dType = StringVar()
        dType.set(diettype_list[0])
        opt = OptionMenu(self.frame_addDType, dType, *diettype_list)
        opt.place(x = 300, y = 200, width = 200)
        #enter button
        enter_b = Button(self.frame_addDType, text = "Enter", command = enter_clicked_dietType)
        enter_b.place(x = 350, y = 340, width = 100, height = 40)
        #selection statement (displays the selection the user made)
        select_state = Label(self.frame_addDType)
        #continue button
        cont_b = Button(self.frame_addDType, text = "Continue", command = self.add_conservationStatus)

    ##creates an interface where the user can enter the conservation status of the animal
    def add_conservationStatus(self):
        #list of possible options for conservation status
        conStatus_list = ["Least Concern (LC)", "Near Threatened (NT)", "Vulnerable (VU)", "Endangered (EN)", "Critically Endangered (CR)", "Extinct in the Wild (EW)", "Extinct (EX)"]
        def enter_clicked_conStatus(): #when the enter button is clicked 
            self.animal.add_Conservation_info(cStatus.get()) #adds the conservation status attribute to the Animal object
            select_state.config(text = "You selected " + cStatus.get())
            select_state.place(x = 300, y = 380, width = 200)
            enter_b.place_forget()
            cont_b.place(x = 350, y = 420, width = 100, height = 40)

        #destroy previous adding page frame
        self.frame_addDType.destroy()
        #create frame for adding diet type
        self.frame_addCStatus = Frame(self.window)
        self.frame_addCStatus.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #title for the page ("ADD (Conservation)")
        title = Label(self.frame_addCStatus, text = "\nADD\n(Conservation)", font = ("Gobold", "30"))
        title.pack()
        #subtitle ("Conservation Status")
        subtitle = Label(self.frame_addCStatus, text = "Conservation Status", font = ("Gobold", "20"))
        subtitle.place(x = 300, y = 150, width = 200)
        #optionmenu (options for conservation status)
        cStatus = StringVar()
        cStatus.set(conStatus_list[0])
        opt = OptionMenu(self.frame_addCStatus, cStatus, *conStatus_list)
        opt.place(x = 300, y = 200, width = 200)
        #enter button
        enter_b = Button(self.frame_addCStatus, text = "Enter", command = enter_clicked_conStatus)
        enter_b.place(x = 350, y = 340, width = 100, height = 40)
        #selection statement (displays the selection the user made)
        select_state = Label(self.frame_addCStatus)
        #continue button
        cont_b = Button(self.frame_addCStatus, text = "Continue", command = self.add_imagePath)
    
    ##creates an interface where the user entered the image file name
    def add_imagePath(self):
        """ def enter_clicked(): #when the enter button is clicked
            self.animal.add_Image(entry_imagePath.get())
            cont_b.place(x = 350, y = 350, width = 100, height = 40) """
        def select_clicked():
            #ask for image directory         
            directory = filedialog.askopenfilename(initialdir = "/", filetypes = (("Image files", "*.jpg *.jpeg *.png *.svg"), ("All files", "*.*")))
            image_filename = os.path.basename(directory)
            print(image_filename)
            os.replace(directory, r"Animal Database (GUI)/Images/"+image_filename)
            self.animal.add_Image(image_filename)
            cont_b.place(x = 350, y = 250, width = 100, height = 40)
        
        #destroy previous adding page frame
        self.frame_addCStatus.destroy()
        #creates the frame for the adding name
        self.frame_addImage = Frame(self.window)
        self.frame_addImage.place(x = 0, y = 0, width = 800, height = 500)
        #title for the page ("ADD (Name)")
        title = Label(self.frame_addImage, text = "\nADD\n(Image Path)", font = ("Gobold", "30"))
        title.pack()

        """ #entry to enter the animal's name
        entry_imagePath = Entry(self.frame_addImage)
        entry_imagePath.place(x = 300, y = 250, width = 200)

        #enter button
        enter_b = Button(self.frame_addImage, text = "Enter", command = enter_clicked)
        enter_b.place(x = 350, y = 300, width = 100, height = 40) """

        #select button
        select_b = Button(self.frame_addImage, text = "Select", command = select_clicked)
        select_b.place(x = 350, y = 250, width = 100, height = 40)
        #information label
        information = Label(self.frame_addImage, text = "Click open to select an image file")
        information.place(x = 200, y = 200, width = 400)
        #continue button
        cont_b = Button(self.frame_addImage, text = "Continue", command = self.exit_Create_Animal)

    ##finishes up the adding Animal process and exits the adding Animal interface
    def exit_Create_Animal(self):
        self.animal_list.append(self.animal) #adds the new Animal object created to the Database's list
        self.frame_addImage.destroy() #destroys the previous frame to bring up the main menu's frame

