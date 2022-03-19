from datetime import datetime
from tkinter import ttk
from tkinter import *
from turtle import title

#TODO
#refactor using new death object
#save file as array for easy retrieval and retrieve death count from it
#repeat last death
#selection of enemies, add enemy button


def popup():

    global additional_deaths
    global death_count
    
    additional_deaths = 0
    
    def read_death_count_from_file():
        with open(death_file, 'r') as file:
            return len(file.readlines())
    
    def update_total_death_count_in_main(string):        
        count_message.configure(text=string)
        count_message.update()
        
    def update_death_string_label(string):
        global recent_death_string
        recent_death_string = string
        
        success_text.configure(text=recent_death_string)
        success_text.update()
    
    def add_death_to_file(death_count):
        global additional_deaths
        global recent_death_string
        
        #add invalid input label text
        def update_invalid_input_label(string):
            invalid_input_label.configure(text=string)
            invalid_input_label.update()
            
        #writes info to file when button is pressed
        def submit_death(death_count):
            global additional_deaths

            def update_death_count_in_death_string(new_amount):
                return "Death %d: Killed by %s in %s on %s \n"%(new_amount, death_reason.get(), death_location, death_time.strftime("%c"))

            def repeat_death():
                return None
            
            #retrieve user submitted location and submission time
            death_location = location_list.get()
            death_time = datetime.now()      
            
            #validate user input
            if (death_location == "Select a location" or death_reason.get() == ""):
                update_invalid_input_label("Please enter valid reason and location")

            else:                
                #additional_deaths starts at 0
                death_count += additional_deaths
                
                death_string = update_death_count_in_death_string(death_count + 1) 

                with open(death_file, 'a+') as file:
                    file.write(death_string)
                    
                new_death_count = read_death_count_from_file()
                if (new_death_count > death_count):
                    additional_deaths += 1
                    update_total_death_count_in_main("Total Deaths: %d"%new_death_count)
                    death_string = update_death_count_in_death_string(new_death_count)
                    update_death_string_label("Added death:\n%s"%death_string)
                    
                new_death_window.destroy()
        
        #create new death window
        new_death_window = Toplevel(bg='black')
        new_death_window.attributes('-alpha', 0.9)
        new_death_window.title("Adding New Death")
        new_death_window.geometry('500x150')
        
        frame = Frame(new_death_window, bg='black')
        frame.pack()
        
        #create input box for death reason
        death_reason = Entry(frame, width=20)
        death_reason.pack(pady=10)
        
        #array of locations

        locations = ["Limgrave", "Stormfront Catacombs", "Gatefront Ruins", "Stormgate", "Stormhill", "Stormveil Castle", 
                     "Deathtouched Catacombs", "Summonwater Village", "Siofra River", "Roundtable Hold", "Stillwater Cave", 
                     "Liurnia of the Lakes", "Lakeside Crystal Caves", "Ainsel River", "Uhl Palace Ruins", "Uld Palace Ruins", 
                     "Black Knife Catacombs", "Bellum Highway", "Academy Crystal Cave", "Temple Quarter", "Road's End Catacombs",
                     "Ruin-Strewn Precipice", "Altus Plateau"]

        
        #add array of locations to selectable list
        location_list = ttk.Combobox(frame, values = locations)
        location_list.set("Select a location")
        location_list.pack()
        
        #create label instance placeholder for invalid input
        invalid_input_label = Label(frame, bg='black', fg='white')
        
        #create button for submitting death information
        add_new_death_button = Button(frame, text="Add", bg='black', fg='white', command=lambda:submit_death(death_count))
        add_new_death_button.pack(pady=10, padx=10, expand="True")
        invalid_input_label.pack(pady=10, padx=10, expand="True")
        
        if (additional_deaths != 0):
            just_added = Label(frame, text="Just added: ", bg='black', fg='white')            
            #repeat_recent_death = Button(frame, text="Repeat Last Death", command=repeat_death)
            #repeat_recent_death.pack()    

    #main logic
    death_file = "deathcount.txt"
    death_count = read_death_count_from_file()
        
    #main window object
    main = Tk()
    main.configure(bg='black')
    main.attributes('-alpha', 0.9)

    #title and dimensions of window
    main.title("Death Counter")
    main.geometry('300x150')
    main.iconbitmap('assets/eldenringicon.ico')
    
    #display total death count on top
    count_message = Label(main, text="Total Deaths: %d"%death_count, bg='black', fg='white')
    count_message.pack(ipady=10)

    #add button to middle of window
    add_death_button = Button(main, text='Add Death', compound=LEFT, bg='black', fg='white', command=lambda:add_death_to_file(death_count)) 
    add_death_button.pack(ipadx=5, ipady=5, expand=True)

    #instantiate label placeholder for recently added deaths area at bottom
    success_text = Label(main, text="Go die a few more times", bg='black', fg='white', wraplength=250)
    success_text.pack(ipady=10)

    main.mainloop()
    
popup()