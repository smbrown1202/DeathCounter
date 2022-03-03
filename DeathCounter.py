import datetime
from tkinter import ttk
from tkinter import *


        
def popup():
    
    death_file = "//DeathCounter//deathcount.txt"
    
    def get_death_count():
        with open(death_file, 'r') as file:
            return len(file.readlines())
    
    def update_recent_death(string):        
        count_message.configure(text=string)
        count_message.update()
        count_message.pack()
        
    def update_death_string(string):
        success_text.configure(text=string)
        success_text.update()
        success_text.pack()
        
    #create function to display text when button calls it
    def add_death():
        
        #writes info to file
        def submit_death():
            
            def successful_submit():
                update_recent_death("Total Deaths: %d"%get_death_count())
                update_death_string("Added death:\n%s"%death_string)
            
            death_location = location_list.get()
            death_time = datetime.datetime.now()
            
            if (death_location == "Select a location" or death_reason.get() == ""):
                invalid_message = Label(frame, text="Please enter valid reason and location")
                invalid_message.pack()
        
            else:
                death_count = original_death_count + 1
                #TO DO - original_death_count + 1 limits this to only updating the death count in this string once
                death_string = "Death %d: Killed by %s in %s on %s \n"%(death_count, death_reason.get(), death_location, death_time.strftime("%c"))

                with open(death_file, 'a+') as file:
                    file.write(death_string)
                if (get_death_count() > original_death_count):
                    successful_submit()
                new_death_window.destroy()
        
        new_death_window = Toplevel()
        new_death_window.title("Add Death")
        new_death_window.geometry('500x150')
        
        frame = Frame(new_death_window)
        frame.pack()
        
        death_reason = Entry(frame, width=20)
        death_reason.pack(padx=5, pady=5)
        
        locations = ["Limgrave", "Stormfront Catacombs", "Gatefront Ruins", "Stormgate", "Stormhill"]
        
        location_list = ttk.Combobox(frame, values = locations)
        location_list.set("Select a location")
        location_list.pack()
        
        submit = Button(frame, text="Submit", command=submit_death)
        submit.pack()
        
    #main window object
    main = Tk()

    #title and dimensions of window
    main.title("Death Counter")
    main.geometry('300x150')
    
    original_death_count = get_death_count()
    
    count_message = Label(main, text="Total Deaths: %d"%original_death_count)
    
    success_text = Label(main, wraplength=250)
    
    count_message.pack(fill='x')

    #create button
    add_death_button = Button(main, text='Add Death', compound=LEFT, command=add_death)
    
    add_death_button.pack(ipadx=5, ipady=5, expand=True)



    main.mainloop()
    
popup()