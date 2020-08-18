from tkinter import *
from PIL import Image, ImageTk
class Display_Page:

    def __init__(self, window, list, name, display_type):
        #Constructor
        #takes the display_type and does the appropriate display type (used for me to check list)
        #input: database's list, animal's name, display type
        self.window = window  
        if display_type == "search" and name != "": #calls to display animal page
            self.display_animalPage(list, name.upper())
        elif display_type == "": #calls to ask user which display type they want
            self.asking_displayType(list)
        elif display_type == "list1": #calls the print the list
            self.display_list(list)

        self.window.mainloop()

    def asking_displayType(self, list):
        #Acts as another constructor if no display_type is given when class is called
        #asks the user the display type they want if not given (used for the user)
        #input: database's list

        def list1_clicked():
            self.display_list(list)
        def list2_clicked():
            self.display_listofAnimals(list)

        #create the frame to ask the user for a display type
        self.frame_askDisplayType = Frame(self.window)
        self.frame_askDisplayType.place(x = 0, y = 0, width = 800, height = 500)
        #title for the page
        title = Label(self.frame_askDisplayType, text = "\nDISPLAY\n", font = ("Gobold", "30"))
        title.pack()
        #subtitle (countries)
        subt_coun = Label(self.frame_askDisplayType, text = "Display Type", font = ("Gobold", "20"))
        subt_coun.place(x = 300, y = 150, width = 200)
        #explaining display types (text)
        disType_text = '''\nDisplay Types
        \nList1 --> this display option displays the list of Animal objects of the Animal Database
        \nList2 --> this display option displays the list of animals of the Animal Database\n''' 
        disType = Label(self.frame_askDisplayType, text = disType_text)
        disType.pack()
        #List1 button
        list1_b = Button(self.frame_askDisplayType, text = "List1", command = list1_clicked)
        list1_b.place(x = 350, y = 300, width = 100, height = 40)
        #List2 button
        list2_b = Button(self.frame_askDisplayType, text = "List2", command = list2_clicked)
        list2_b.place(x = 350, y = 350, width = 100, height = 40)

    def display_animalPage(self, list, name):
        #Acts as another constructor if display_type given is 'search' along with animal name
        #displays the individual animal page
        #input: database's list, animal's name

        #getting all the required information of the Animal object
        habitat_list = None 
        diet_type = None
        conservation_status = None
        image_path = "Animal Database (GUI)/Images/"
        img = ""
        for obj in list:
            if name.upper() == obj.get_Name():
                habitat_list = obj.get_Habitat_info() #habitat information
                animal_class = obj.get_Animal_class() #animal class information
                diet_type = obj.get_Diet_info() #diet type information
                conservation_status = obj.get_Conservation_info() #conservation status
                image_path = image_path + obj.get_Image() #image 
                img = ImageTk.PhotoImage(Image.open(image_path))

        continent = habitat_list[0] #continent information
        countries = habitat_list[1] #countries information
        if countries == []:
            countries = "Covers a very large part of the continent(s)"

        def home_clicked():
            self.frame_animalPage.destroy()
            
        #creating frame for displaying animal page
        self.frame_animalPage = Frame(self.window)
        self.frame_animalPage.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #title for the page
        title = Label(self.frame_animalPage, text = "\nDISPLAY\n", font = ("Gobold", "30"))
        title.pack()
        
        #picture label
        picture = Label(self.frame_animalPage, bg = 'black', image = img)
        picture.place(x = 10, y = 120, width = 300, height = 300)
        font_style = ("American Typewriter Light", 18)
        font_style2 = ("American Typewriter", 18)
        #name label
        name_label = Label(self.frame_animalPage, text = "Name: ", font = font_style2, anchor = "w")
        name_label.place(x = 320, y = 120, width = 60)
        #name information label
        name_info_label = Label(self.frame_animalPage, text = name.upper(), font = font_style, anchor = "w")
        name_info_label.place(x = 380, y = 120, width = 500)
        #habitat subtitle
        habitat_sub = Label(self.frame_animalPage, text = "Habitat:", font = font_style2, anchor = "w")
        habitat_sub.place(x = 320, y = 160, width = 500)
        #continent label
        cont_label = Label(self.frame_animalPage, text = "Continent(s): ", font = font_style2, anchor = "w")
        cont_label.place(x = 320, y = 185, width = 120)
        #continent information label
        cont_info_label = Label(self.frame_animalPage, text = self.string_list(continent), font = font_style, anchor = "w")
        cont_info_label.place(x = 440, y = 185, width = 500)
        #countries label
        coun_label = Label(self.frame_animalPage, text = "Countries: ", font = font_style2, anchor = "w")
        coun_label.place(x = 320, y = 210, width = 100)
        #countries information label
        coun_info_label = Label(self.frame_animalPage, text = self.string_list(countries), font = font_style, anchor = "w")
        coun_info_label.place(x = 415, y = 210, width = 500)
        #animal class label
        aClass_label = Label(self.frame_animalPage, text = "Animal Class: ", font = font_style2, anchor = "w", justify = LEFT)
        aClass_label.place(x = 320, y = 250, width = 500)
        #animal class information label
        aClass_info_label = Label(self.frame_animalPage, text = animal_class, font = font_style, anchor = "w", justify = LEFT)
        aClass_info_label.place(x = 320, y = 270, width = 500)
        #diet type label
        dType_label = Label(self.frame_animalPage, text = "Diet Type: ", font = font_style2, anchor = "w", justify = LEFT)
        dType_label.place(x = 320, y = 310, width = 500)
        #diet type information label
        dType_info_label = Label(self.frame_animalPage, text = diet_type, font = font_style, anchor = "w", justify = LEFT)
        dType_info_label.place(x = 320, y = 333, width = 500)
        #conservation status label
        cStatus_label = Label(self.frame_animalPage, text = "Conservation Status: ", font = font_style2, anchor = "w", justify = LEFT)
        cStatus_label.place(x = 320, y = 370, width = 500)
        #conservation status information label
        cStatus_label = Label(self.frame_animalPage, text = conservation_status, font = font_style, anchor = "w", justify = LEFT)
        cStatus_label.place(x = 320, y = 390, width = 500)

        #home button
        home_b = Button(self.frame_animalPage, text = "Home", command = home_clicked)
        home_b.place(x = 10, y = 450, width = 100, height = 40)

    def print_list(self, list):
        #prints the list of continents and countries the animal is from
        #input: list of continents/countries
        for con in list:
            print(con, end=", ")
        print()

    def string_list(self, list):
        #creates a string for the list of continents and countries the animal is from
        #input: list of continents/countries
        str_list = ""
        if type(list) == str:
            return list
        else:
            for con in list:
                str_list = str_list[:] + str(con) + ", "
            return str_list

    def display_list(self, list):
        #prints out the list of the database
        #input: database's list

        def home_clicked():
            self.frame_displayList.destroy()
            self.frame_listbox.destroy()

        #destroy previous frame
        self.frame_askDisplayType.destroy()

        #create frame for displaying list
        self.frame_displayList = Frame(self.window)
        self.frame_displayList.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #title for the page
        title = Label(self.frame_displayList, text = "\nDISPLAY\n", font = ("Gobold", "30"))
        title.pack()
        #subtitle (countries)
        subt_coun = Label(self.frame_displayList, text = "List", font = ("Gobold", "20"))
        subt_coun.place(x = 300, y = 150, width = 200)

        #frame for listbox
        self.frame_listbox = Frame(self.window)
        self.frame_listbox.place(x = 250, y = 200, width = 300, height = 200)
        #scrollbar 
        scroll = Scrollbar(self.frame_listbox)
        #listbox
        dis_Listbox = Listbox(self.frame_listbox, selectmode = BROWSE, yscrollcommand = scroll.set)
        for i in range(len(list)):
            dis_Listbox.insert(i, list[i])
        dis_Listbox.config(width = 30)
        dis_Listbox.pack(side = LEFT, fill = BOTH)
        scroll.config(command = dis_Listbox.yview)
        scroll.pack(side = RIGHT, fill = BOTH)

        #home button
        home_b = Button(self.frame_displayList, text = "Home", command = home_clicked)
        home_b.place(x = 350, y = 430, width = 100, height = 40)

    def display_listofAnimals(self, list):
        #prints out a list of all the animals in the Animal Database
        #input: database's list

        list_animals = []
        for i in range(len(list)):
            list_animals.append(list[i].get_Name())
        list_animals.sort() #sorts the list of animal names alphabetically

        def home_clicked():
            self.frame_displayAnimalList.destroy()
            self.frame_listbox1.destroy()

        #destroy previous frame
        self.frame_askDisplayType.destroy()

        #create frame for displaying list
        self.frame_displayAnimalList = Frame(self.window)
        self.frame_displayAnimalList.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #title for the page
        title = Label(self.frame_displayAnimalList, text = "\nDISPLAY\n", font = ("Gobold", "30"))
        title.pack()
        #subtitle (countries)
        subt_coun = Label(self.frame_displayAnimalList, text = "List of Animals", font = ("Gobold", "20"))
        subt_coun.place(x = 300, y = 150, width = 200)

        #frame for listbox
        self.frame_listbox1 = Frame(self.window)
        self.frame_listbox1.place(x = 250, y = 200, width = 300, height = 200)
        #scrollbar 
        scroll = Scrollbar(self.frame_listbox1)
        #listbox
        dis_Listbox = Listbox(self.frame_listbox1, selectmode = BROWSE, yscrollcommand = scroll.set)
        for i in range(len(list_animals)):
            dis_Listbox.insert(i, list_animals[i])
        dis_Listbox.config(width = 30)
        dis_Listbox.pack(side = LEFT, fill = BOTH)
        scroll.config(command = dis_Listbox.yview)
        scroll.pack(side = RIGHT, fill = BOTH)

        #home button
        home_b = Button(self.frame_displayAnimalList, text = "Home", command = home_clicked)
        home_b.place(x = 350, y = 430, width = 100, height = 40)


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
    
    
    
