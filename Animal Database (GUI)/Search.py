from Display_Page import Display_Page
from tkinter import *
class Search:

    def __init__(self, window, list):
        #Constructor
        #takes the search_type to determine which search type to run
        #input: database's list, search type, name (animal's name or continent)
        #dict = {'C LYNX': [(['north america'], []), 'carnivore', 'LC'], 'E LYNX': [(['europe'], []), 'carnivore', 'LC'], 'I LYNX': [(['europe'], []), 'carnivore', 'CR'], 'A LYNX': [(['asia'], []), 'carnivore', 'EX'], 'S LYNX': [(['south america'], []), 'carnivore', 'EX'], 'A2 LYNX': [(['asia'], []), 'carnivore', 'EX'], 'EURASIAN LYNX': [(['europe'], ['spain']), 'carnivore', 'LC']}
        self.window = window
        self.asking_searchType(list)
        
        self.window.mainloop()

    def asking_searchType(self, list):
        #asks the user which search type they want to run
        #input: database's list

        def name_clicked():
            self.type_searchName(list)
        def continent_clicked():
            self.select_searchContinent(list)

        #create frame to ask user for a search type
        self.frame_askSearchType = Frame(self.window)
        self.frame_askSearchType.place(x = 0, y = 0, width = 800, height = 500)
        #title for the page
        title = Label(self.frame_askSearchType, text = "\nSEARCH\n", font = ("Gobold", "30"))
        title.pack()
        #subtitle (countries)
        subt_coun = Label(self.frame_askSearchType, text = "Search By", font = ("Gobold", "20"))
        subt_coun.place(x = 300, y = 150, width = 200)
        #search by Name button
        name_b = Button(self.frame_askSearchType, text = "Name", command = name_clicked)
        name_b.place(x = 350, y = 200, width = 100, height = 40)
        #search by Continent button
        continent_b = Button(self.frame_askSearchType, text = "Continent", command = continent_clicked)
        continent_b.place(x = 350, y = 250, width = 100, height = 40)

    def type_searchName(self, list):
        #allows the user to type to search
        #input: str search_type (determine which search type is chosen), list (containing all the Animal objects)
        def search_clicked():
            search_entered = entry_search.get()
            self.search_byName(search_entered, list)

        #destroy previous frame
        self.frame_askSearchType.destroy()

        #creates the frame for the adding name
        self.frame_typeSearch = Frame(self.window)
        self.frame_typeSearch.place(x = 0, y = 0, width = 800, height = 500)
        #title for the page
        title = Label(self.frame_typeSearch, text = "\nSEARCH", font = ("Gobold", "30"))
        title.pack()
        #entry to make a search
        entry_search = Entry(self.frame_typeSearch)
        entry_search.place(x = 300, y = 250, width = 200)
        #search button
        search_b = Button(self.frame_typeSearch, text = "Search", command = search_clicked)
        search_b.place(x = 350, y = 300, width = 100, height = 40)

    def select_searchContinent (self, list):
        def search_clicked():
            search_selected = list_con.curselection()
            continent_selected = None
            for con in search_selected:
                continent_selected = continent_list[con]
            if continent_selected != None:
                error.place_forget()
                self.search_byContinent(continent_selected, list)
            else:
                error.place(x = 200, y = 380, width = 400)

        #destroy previous frame
        self.frame_askSearchType.destroy()

        #creates the frame for the adding name
        self.frame_selectSearch = Frame(self.window)
        self.frame_selectSearch.place(x = 0, y = 0, width = 800, height = 500)
        #title for the page
        title = Label(self.frame_selectSearch, text = "\nSEARCH", font = ("Gobold", "30"))
        title.pack()
        #listbox (options for continents)
        continent_list = ["North America", "South America", "Europe", "Africa", "Asia", "Australia", "Antarctica"] #list of all possible options
        list_con = Listbox(self.frame_selectSearch, selectmode = SINGLE)
        for i in range(len(continent_list)):
            list_con.insert(i, continent_list[i])
        list_con.place(x = 300, y = 190, width = 200)
        #search button
        search_b = Button(self.frame_selectSearch, text = "Search", command = search_clicked)
        search_b.place(x = 350, y = 420, width = 100, height = 40)
        #error label
        error = Label(self.frame_selectSearch, text = "Select a continent to search")

    def search_byName(self, search_typed, list):
        #uses the name and searches the database by animal's name and then displays a list of possible animals
        #input: database's list
        
        results = [] #list of all animals that fit the search
        for obj in list: #adds animals that fit the search into results list
            animal_name = obj.get_Name()
            if search_typed.upper() in animal_name:
                results.append(animal_name)
        results.sort() #sorts the results of the search alphabetically

        def home_clicked():
            self.frame_byName.destroy()
            self.frame_listbox.destroy()
        def confirm_clicked():
            search_selected = searchName_Listbox.curselection()
            animal_selected = None
            for i in search_selected:
                animal_selected = results[i]
            if animal_selected != None:
                error.place_forget()
                self.frame_byName.destroy()
                self.frame_listbox.destroy()
                Display_Page(self.window, list, animal_selected.upper(), "search")
            else:
                error.place(x = 570, y = 250, width = 200)

        #destroy previous frame
        self.frame_typeSearch.destroy()

        #create frame for displaying list
        self.frame_byName = Frame(self.window)
        self.frame_byName.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #title for the page
        title = Label(self.frame_byName, text = "\nSEARCH\n", font = ("Gobold", "30"))
        title.pack()
        #subtitle (countries)
        subt_coun = Label(self.frame_byName, text = "By Name", font = ("Gobold", "20"))
        subt_coun.place(x = 300, y = 150, width = 200)

        #frame for listbox
        self.frame_listbox = Frame(self.window)
        self.frame_listbox.place(x = 250, y = 200, width = 300, height = 200)
        #scrollbar 
        scroll = Scrollbar(self.frame_listbox)
        #listbox
        searchName_Listbox = Listbox(self.frame_listbox, selectmode = SINGLE, yscrollcommand = scroll.set)
        for i in range(len(results)):
            searchName_Listbox.insert(i, results[i])
        searchName_Listbox.config(width = 30)
        searchName_Listbox.pack(side = LEFT, fill = BOTH)
        scroll.config(command = searchName_Listbox.yview)
        scroll.pack(side = RIGHT, fill = BOTH)

        #home button
        home_b = Button(self.frame_byName, text = "Home", command = home_clicked)
        home_b.place(x = 10, y = 450, width = 100, height = 40)
        #confirm button
        confirm_b = Button(self.frame_byName, text = "Confirm", command = confirm_clicked)
        confirm_b.place(x = 620, y = 300, width = 100, height = 40)
        #error label
        error = Label(self.frame_byName, text = "Select a continent to search")

    def search_byContinent(self, search_selected, list):
        #uses the name and searches the database by continent and then displays a list of possible animals
        #input: database's list

        results = [] #list of all animals that fit the search
        for obj in list: #adds animals that fit the search into results list
            animal_habitat_info = obj.get_Habitat_info()
            if search_selected in animal_habitat_info[0]:
                results.append(obj.get_Name())
        results.sort() #sorts the results of the search alphabetically

        def home_clicked():
            self.frame_byContinent.destroy()
            self.frame_listbox.destroy()
        def confirm_clicked():
            search_selected = searchCont_Listbox.curselection()
            animal_selected = None
            for i in search_selected:
                animal_selected = results[i]
            if animal_selected != None:
                error.place_forget()
                self.frame_byContinent.destroy()
                self.frame_listbox.destroy()
                Display_Page(self.window, list, animal_selected.upper(), "search")
            else:
                error.place(x = 570, y = 250, width = 200)

        #destroy previous frame
        self.frame_selectSearch.destroy()

        #create frame for displaying list
        self.frame_byContinent = Frame(self.window)
        self.frame_byContinent.place(x = 0, y = 0, width = self.window.winfo_width(), height = self.window.winfo_height())
        #title for the page
        title = Label(self.frame_byContinent, text = "\nSEARCH\n", font = ("Gobold", "30"))
        title.pack()
        #subtitle (countries)
        subt_coun = Label(self.frame_byContinent, text = "By Continent", font = ("Gobold", "20"))
        subt_coun.place(x = 300, y = 150, width = 200)

        #frame for listbox
        self.frame_listbox = Frame(self.window)
        self.frame_listbox.place(x = 250, y = 200, width = 300, height = 200)
        #scrollbar 
        scroll = Scrollbar(self.frame_listbox)
        #listbox
        searchCont_Listbox = Listbox(self.frame_listbox, selectmode = SINGLE, yscrollcommand = scroll.set)
        for i in range(len(results)):
            searchCont_Listbox.insert(i, results[i])
        searchCont_Listbox.config(width = 30)
        searchCont_Listbox.pack(side = LEFT, fill = BOTH)
        scroll.config(command = searchCont_Listbox.yview)
        scroll.pack(side = RIGHT, fill = BOTH)

        #home button
        home_b = Button(self.frame_byContinent, text = "Home", command = home_clicked)
        home_b.place(x = 10, y = 450, width = 100, height = 40)
        #confirm button
        confirm_b = Button(self.frame_byContinent, text = "Confirm", command = confirm_clicked)
        confirm_b.place(x = 620, y = 300, width = 100, height = 40)
        #error label
        error = Label(self.frame_byContinent, text = "Select a continent to search")

    def confirm_search(self, list):
        #using the list displayed, asks user to enter animal's name again to confirm the search
        #input: database's list
        animal_name_list = []
        for i in range(len(list)):
            animal_name_list.append(list[i].get_Name())
        name = input("Enter the animal's you want to learn about in the results to confirm your search")
        while name.upper() not in animal_name_list:
            print("Incorrect input")
            name = input("Enter the animal's you want to learn about in the results to confirm your search")
        print()
        Display_Page("", list, name.upper(), "search")


