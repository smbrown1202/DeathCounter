from audioop import add
import datetime
from re import L
from tkinter import ttk
from tkinter import *
from turtle import update
from webbrowser import get

def popup():
    global death_count
    def get_death_count():
        with open(death_file, 'r') as file:
            return len(file.readlines())
    
    def update_recent_death(string):        
        count_message.configure(text=string)
        count_message.update()
        count_message.pack()
        
    def update_death_string_label(string):
        global recent_death_string
        recent_death_string = string
        success_text.configure(text=recent_death_string)
        success_text.update()
        success_text.pack()
        
    death_file = "c://Source//python//DeathCounter//deathcount.txt"
    death_count = get_death_count()
    global additional_deaths
    additional_deaths = 0

        
    #create function to display text when button calls it
    def add_death(original_death_count):
        global additional_deaths
        global recent_death_string
        
        #writes info to file
        def submit_death():
            
            def update_death_count_in_death_string(current_death_count):
                return "Death %d: Killed by %s in %s on %s \n"%(current_death_count, death_reason.get(), death_location, death_time.strftime("%c"))

            def successful_submit(current_death_count):
                update_recent_death("Total Deaths: %d"%current_death_count)
                death_string = update_death_count_in_death_string(current_death_count)
                update_death_string_label("Added death:\n%s"%death_string)
                
                global additional_deaths 
                additional_deaths = additional_deaths + 1
            
            def repeat_death():
                return None
            
            death_location = location_list.get()
            death_time = datetime.datetime.now()
            
            if (death_location == "Select a location" or death_reason.get() == ""):
                invalid_message = Label(frame, text="Please enter valid reason and location")
                invalid_message.pack()
        
            else:
                global additional_deaths
                new_death_count = death_count + 1 + additional_deaths
                
                death_string = update_death_count_in_death_string(new_death_count) 

                with open(death_file, 'a+') as file:
                    file.write(death_string)
                    
                new_death_count = get_death_count()
                if (new_death_count > original_death_count):
                    successful_submit(new_death_count)
                new_death_window.destroy()
        
        new_death_window = Toplevel()
        new_death_window.title("Add Death")
        new_death_window.geometry('500x150')
        
        frame = Frame(new_death_window)
        frame.pack()
        
        death_reason = Entry(frame, width=20)
        death_reason.pack(padx=5, pady=5)
        
        locations = ["Limgrave", "Stormfront Catacombs", "Gatefront Ruins", "Stormgate", "Stormhill", "Stormveil Castle"]
        
        location_list = ttk.Combobox(frame, values = locations)
        location_list.set("Select a location")
        location_list.pack()
        
        submit = Button(frame, text="Submit", command=submit_death)
        submit.pack()
        
        if (additional_deaths != 0):
            repeat_recent_death = Button(frame, text="Repeat Last Death", command=repeat_death)
            repeat_recent_death.pack()
        
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
    add_death_button = Button(main, text='Add Death', compound=LEFT, command=lambda: add_death(original_death_count))
    
    add_death_button.pack(ipadx=5, ipady=5, expand=True)

    main.mainloop()
    
popup()