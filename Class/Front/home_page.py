import tkinter as tk  # Importing the tkinter module for GUI
import datetime  # Importing the datetime module to work with dates and times

class HomePage(tk.Frame):  # Creating a class StartPage which inherits from tk.Tk
    def __init__(self, master=None):  # Defining the constructor
        super().__init__(master)  # Calling the constructor of the parent class

        self.master.get_user_info()
        self.public_notifications = self.master.get_new_messages(self.master.user_Id, 1)
        self.create_widget()

    def create_widget(self):
        frame = tk.Frame(master=self, width=750, height=900, bg="darkblue")
        frame.pack()

        self.master.title("Home")  # Setting the title of the window
        # self.master.geometry("750x900")  # Setting the size of the window
        # self.master.resizable(width=False, height=False)  # Making the window non-resizable
        # self.master.configure(bg="darkblue")  # Setting the background color of the window

        #picture loading and resizing
        self.private_message_chat_icon = tk.PhotoImage(file="Class/Front/Pictures/private_message_chat_icon.png")
        self.private_message_chat_icon = self.private_message_chat_icon.subsample(14, 14) # Resizing the image
        self.message_chat_icon = tk.PhotoImage(file="Class/Front/Pictures/message_chat_icon.png")
        self.message_chat_icon = self.message_chat_icon.subsample(22, 22) # Resizing the image
        self.private_voice_chat_icon = tk.PhotoImage(file="Class/Front/Pictures/private_voice_chat_icon.png")
        self.private_voice_chat_icon = self.private_voice_chat_icon.subsample(15, 15)  # Resizing the image
        self.voice_chat_icon = tk.PhotoImage(file="Class/Front/Pictures/voice_chat_icon.png") 
        self.voice_chat_icon = self.voice_chat_icon.subsample(15, 15)  # Resizing the image   

        # Creating and configuring a frame for the buttons field
        self.left_frame = tk.Frame(master=frame, bg="DodgerBlue3", width=300, height=400)
        self.left_frame.pack(side="left")
        self.left_frame.place(x=50, y=250)


        # Creating and configuring the public voice chat button
        self.public_voice_chat_button = tk.Button(master=frame, text="Salon Vocal Public", bg="RoyalBlue4", fg="white", width=20, height=1)
        self.public_voice_chat_button.pack()
        self.public_voice_chat_button.config(font=("Agency FB", 20, "italic"), relief="groove")
        self.public_voice_chat_button.place(x=110, y=275)

        # Place the icons
        self.voice_chat_icon_label = tk.Label(master=frame, image=self.voice_chat_icon, bg="DodgerBlue3")
        self.voice_chat_icon_label.pack()
        self.voice_chat_icon_label.place(x=50, y=275)
    
        self.private_voice_chat_icon_label = tk.Label(master=frame, image=self.private_voice_chat_icon, bg="DodgerBlue3")
        self.private_voice_chat_icon_label.pack()
        self.private_voice_chat_icon_label.place(x=50, y=365)

        self.message_chat_icon_label = tk.Label(master=frame, image=self.message_chat_icon, bg="DodgerBlue3")
        self.message_chat_icon_label.pack()
        self.message_chat_icon_label.place(x=50, y=485)

        self.private_message_chat_icon_label = tk.Label(master=frame, image=self.private_message_chat_icon, bg="DodgerBlue3")
        self.private_message_chat_icon_label.pack()
        self.private_message_chat_icon_label.place(x=50, y=575)

        # Creating and configuring the private voice chat button
        self.private_voice_chat_button = tk.Button(master=frame, text="Salon Vocal Privé", bg="RoyalBlue4", fg="white", width=20, height=1)
        self.private_voice_chat_button.pack()
        self.private_voice_chat_button.config(font=("Agency FB", 20, "italic"), relief="groove")
        self.private_voice_chat_button.place(x=110, y=365)

        # Creating and configuring the public text chat button
        self.public_text_chat_button = tk.Button(master=frame, text="Salon Message Public", bg="RoyalBlue4", fg="white", width=20, height=1)
        self.public_text_chat_button.pack()
        self.public_text_chat_button.config(font=("Agency FB", 20, "italic"), relief="groove")
        self.public_text_chat_button.place(x=110, y=485)
        # Adding the logic to show the public text chat page when the public text chat button is clicked
        self.public_text_chat_button["command"] = self.master.show_public_text_chat_page

        # Creating and configuring the private text chat button
        self.private_text_chat_button = tk.Button(master=frame, text="Salon Message Privé", bg="RoyalBlue4", fg="white", width=20, height=1)
        self.private_text_chat_button.pack()
        self.private_text_chat_button.config(font=("Agency FB", 20, "italic"), relief="groove")
        self.private_text_chat_button.place(x=110, y=575)

        # Creating and configuring the deconnection button
        self.deconnection_button = tk.Button(master=frame, text="Déconnexion", bg="cornflowerblue", fg="white", width=20, height=1, command=self.deconnection)
        self.deconnection_button.pack()
        self.deconnection_button.config(font=("Agency FB", 20, "italic"), relief="groove")
        self.deconnection_button.place(x=480, y=780)

        # Creating and configuring the time label
        self.time_label = tk.Label(master=frame, bg="darkblue", fg="white")
        self.time_label.pack()
        self.time_label.config(font=("Agency FB", 40))
        self.time_label.place(x=645, y=20)

        # Creating and configuring the date label
        self.date_label = tk.Label(master=frame, bg="darkblue", fg="white")
        self.date_label.pack()
        self.date_label.config(font=("Agency FB", 25, "italic"))
        self.date_label.place(x=600, y=80)


        self.update_time()  # Calling the update_time method to update the time and date

    def deconnection(self):  # Method to return to the start page
        self.master.reset_user_info()  # Calling the reset method of the master attribute
        self.master.show_start_page() # Calling the show_home_page method of the master attribute

    def update_time(self):  # Method to update the time and date
        current_time = datetime.datetime.now().strftime("%H:%M")  # Getting the current time
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")  # Getting the current date
        self.time_label.config(text=current_time)  # Updating the time label
        self.date_label.config(text=current_date)  # Updating the date label
        self.after(1000, self.update_time)  # Calling the update_time method after 1 second
        self.toggle_colon()  # Calling the toggle_colon method to blink the colon in the time

    def toggle_colon(self):  # Method to blink the colon in the time
        current_time = self.time_label.cget("text")  # Getting the current time from the label
        if ":" in current_time:  # If the colon is in the time
            current_time = current_time.replace(":", " ")  # Replace the colon with a space
        else:  # If the colon is not in the time
            current_time = current_time.replace(" ", ":")  # Replace the space with a colon
        self.time_label.config(text=current_time)  # Updating the time label
        self.after(1000, self.toggle_colon)  # Calling the toggle_colon method after 1 second

    def hide(self):
        self.pack_forget()

    def show(self):
        self.pack(fill="both", expand=True)


if __name__ == "__main__":  # If the script is run directly
    root = tk.Tk()  # Create an instance of the Tk class    
    app = HomePage(master=root)  # Create an instance of the StartPage class
    app.mainloop()  # Start the main event loop