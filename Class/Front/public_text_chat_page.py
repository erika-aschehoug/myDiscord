import tkinter as tk  # Importing the tkinter module for GUI
import datetime  # Importing the datetime module to work with dates and times

class PublicTextChatPage(tk.Frame):  # Creating a class StartPage which inherits from tk.Tk
    def __init__(self, master=None):  # Defining the constructor
        super().__init__(master)  # Calling the constructor of the parent class

        self.posts = self.master.get_post(1)
        self.all_users = self.master.get_all_users()
        self.create_widget()
        
        # #Testing the add_message method
        self.add_message("Utilisateur X s'est déconnecté", "disconnection")
        self.add_message("Ceci est un message envoyé", "sent")
        self.add_message("Ceci est un message envoyé", "sent")
        self.add_message("Ceci est un message reçu", "received")
        self.add_message("Utilisateur X s'est connecté", "connection")
        self.add_message("Ceci est un message reçu", "received")

    def set_names(self, username, userfirstname):
        self.username = username
        self.userfirstname = userfirstname

    def create_widget(self):
        frame = tk.Frame(master=self, width=750, height=900, bg="darkblue")
        frame.pack()

        self.master.title("Salon Chat Publique")  # Setting the title of the window

        # Creating and configuring the return button
        self.deconnection_button = tk.Button(master=frame, text="Quitter le chat", bg="cornflowerblue", fg="white", width=20, height=1, command=self.deconnection)
        self.deconnection_button.pack()
        self.deconnection_button.config(font=("Agency FB", 20, "italic"), relief="groove")
        self.deconnection_button.place(x=480, y=780)

        # Creating a label around the public text chat name
        self.chat_name_label_frame = tk.Frame(master=frame, bg="cornflowerblue", width=290, height=60, relief="groove")
        self.chat_name_label_frame.pack()
        self.chat_name_label_frame.place(x=50, y=195)


        #picture loading resizing and placing
        self.message_chat_icon = tk.PhotoImage(file="Class/Front/Pictures/message_chat_icon.png")
        self.message_chat_icon = self.message_chat_icon.subsample(22, 22) # Resizing the image
        self.message_chat_icon_label = tk.Label(master=frame, image=self.message_chat_icon, bg="cornflowerblue")
        self.message_chat_icon_label.pack()
        self.message_chat_icon_label.place(x=50, y=200)

        # Creating and configuring the public text chat name
        self.chat_name_label = tk.Label(master=frame, text="Salon Message Public", bg="RoyalBlue4", fg="white", width=20, height=1)
        self.chat_name_label.pack()
        self.chat_name_label.config(font=("Agency FB", 20, "italic"), relief="groove")
        self.chat_name_label.place(x=110, y=210)

        # Creating and configuring a welcome message with the user's name under the chat name
        self.welcome_message_label = tk.Label(master=frame, text=f"  Bienvenue sur le salon de discussion public {self.master.firstname} {self.master.username}  ", bg="SlateGray4", fg="white")
        self.welcome_message_label.pack()
        self.welcome_message_label.config(font=("Agency FB", 20, "italic"))
        self.welcome_message_label.place(x=50, y=250)

    
        # Creating and configuring the area to show the sent and received messages
        self.message_area = tk.Text(master=frame, bg="RoyalBlue4", fg="black", width=80, height=16)
        self.message_area.pack()
        self.message_area.config(font=("Agency FB", 15, "italic"), state="disabled")
        self.message_area.place(x=50, y=290)
        

        # Crate and configure the message entry and the send buttond
        self.message_entry = tk.Text(master=frame, width=53, height=1, font=("Agency FB", 20))
        self.message_entry.pack()
        self.message_entry.place(x=50, y=700)
        self.send_button = tk.Button(master=frame, text="Envoyer",fg="white", bg="RoyalBlue4", command=self.send_message)
        self.send_button.pack()
        self.send_button.place(x=640, y=710)

        self.master.bind("<Return>", self.send_message)  # Binding the Enter key to the send_message method

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

    def deconnection(self):  # Method to return to the start page
        self.master.show_home_page() # Calling the show_home_page method of the master attribute

    def add_message(self, message, message_type): # Method to add a message to the display area
        current_time = datetime.datetime.now().strftime("%H:%M:%S  \n%d/%m/%Y")  # Getting the current time
        self.message_area.config(state="normal")  # activating the edition
        if message_type == "sent":
            self.message_area.insert("end", f"{current_time}  \n - Vous: {message}  \n", ("sent", "right")) # adding the message to the display area
        elif message_type == "received":
            self.message_area.insert("end", f"{current_time}\n - Autre: {message}\n", ("received", "left")) # adding the message to the display area
        elif message_type == "connection":
            self.message_area.insert("end", f"{current_time}\n - {message}\n", ("connection", "center")) # adding the message to the display area
        else:  # disconnection
            self.message_area.insert("end", f"{current_time}\n - {message}\n", ("disconnection", "center")) # adding the message to the display area
        self.message_area.config(state="disabled")  # deasable the edition

        self.message_area.see("end")  # Scroll to the end of the text area
        self.message_area.tag_configure("sent", foreground="deep sky blue", justify="right") # Configuring the sent message tag
        self.message_area.tag_configure("received", foreground="ivory2", justify="left") # Configuring the received message tag
        self.message_area.tag_configure("connection", foreground="lime green", justify="center") # Configuring the connection message tag
        self.message_area.tag_configure("disconnection", foreground="red3", justify="center") # Configuring the disconnection message tag
    
    def send_message(self, event=None): # Method to send a message
        message = self.message_entry.get("1.0", "end").strip()  # Getting the message from the entry and removing the leading and trailing whitespaces
        current_time = datetime.datetime.now().strftime("%H:%M:%S  %d/%m/%Y")  # Getting the current time
        self.message_entry.delete("1.0", "end") # Clearing the message entry
        if message:  # If the message is not empty
            self.add_message(message, "sent")  # Adding the message to the display area
            self.master.get_message(message, 1, current_time, False) 

if __name__ == "__main__":  # If the script is run directly
    root = tk.Tk()  # Create an instance of the Tk class    
    app = PublicTextChatPage(master=root)  # Create an instance of the StartPage class
    app.mainloop()  # Start the main event loop