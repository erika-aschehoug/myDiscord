import tkinter as tk  # Importing the tkinter module for GUI
import datetime  # Importing the datetime module to work with dates and times
import pygame  # Importing the pygame module to work with sounds

class PrivateTextChatPage(tk.Frame):  # Creating a class StartPage which inherits from tk.Tk
    def __init__(self, master=None):  # Defining the constructor
        super().__init__(master)  # Calling the constructor of the parent class
        pygame.init()  # Initialize the pygame module
        
        self.add_admin = False
        self.user = self.master.get_all_users()
        self.count = len(self.master.get_post(2)) # Getting the number of messages in the database
        self.all_users = self.master.get_all_users() # Getting all the users from the database
        self.create_widget() # Calling the create_widget method to create the widgets
        self.get_message()  # Calling the get_message method to display the messages
        self.master.get_message(f"{self.master.firstname} {self.master.username} s'est connecté au chat", 2, datetime.datetime.now().strftime("%H:%M:%S  %d/%m/%Y"), True, False) # Adding the connection message to the database
        self.update_message()  # Calling the update_message method to update the messages in the database

    def create_widget(self):
        frame = tk.Frame(master=self, width=750, height=900, bg="darkblue")
        frame.pack()

        self.master.title("Salon Chat Privé")  # Setting the title of the window

        # Creating and configuring a members management label
        self.members_management_label = tk.Label(master=frame, text="Gestion des membres", bg="light slate gray", fg="black", width=20, height=1)
        self.members_management_label.pack()
        self.members_management_label.config(font=("Agency FB", 20, "italic"))
        self.members_management_label.place(x=60, y=20)


        self.members_list = tk.Label(master=frame, bg="light slate gray", fg="black", width=57, height=2)
        self.members_list.pack()
        self.members_list.config(font=("Agency FB", 15))
        self.members_list.place(x=40, y=65)

        #inserting users list séparate with / into members label
        user_list = []
        for user in self.all_users:
            user_list.append(user[2])
        self.members_list.config(text=f"Membres\n {" / ".join(user_list)}")

        # Creating and configuring add and delete members buttons and a fiel to enter the name of the member to add or delete
        self.add_member_button = tk.Button(master=frame, text="Ajouter un membre", bg="light slate gray", fg="darkgreen", width=20, height=1)
        self.add_member_button.pack()
        self.add_member_button.config(font=("Agency FB", 15), relief="groove")
        self.add_member_button.place(x=40, y=150)

        self.delete_member_button = tk.Button(master=frame, text="Supprimer un membre", bg="light slate gray", fg="darkred", width=20, height=1)
        self.delete_member_button.pack()
        self.delete_member_button.config(font=("Agency FB", 15), relief="groove")
        self.delete_member_button.place(x=200, y=150)
        
        self.member_entry = tk.Entry(master=frame, width=31, font=("Agency FB", 15))
        self.member_entry.pack()
        self.member_entry.place(x=40, y=120)

        # checkbutto to activate or desactivate add admin members
        self.add_admin = tk.Checkbutton(master=frame, text="Ajouter en tant qu'admin", bg="light slate gray", fg="black", width=20, height=1, variable=self.add_admin)
        self.add_admin.pack()
        self.add_admin.config(font=("Agency FB", 15))
        self.add_admin.place(x=277, y=115)
        
        # Creating and configuring the return button
        self.deconnection_button = tk.Button(master=frame, text="Quitter le chat", bg="cornflowerblue", fg="white", width=20, height=1, command=self.chat_deconnection)
        self.deconnection_button.pack()
        self.deconnection_button.config(font=("Agency FB", 20, "italic"), relief="groove")
        self.deconnection_button.place(x=480, y=780)

        # Creating a label around the public text chat name
        self.chat_name_label_frame = tk.Frame(master=frame, bg="cornflowerblue", width=290, height=60, relief="groove")
        self.chat_name_label_frame.pack()
        self.chat_name_label_frame.place(x=50, y=195)

        #picture loading resizing and placing
        self.message_chat_icon = tk.PhotoImage(file="Class/Front/Pictures/private_message_chat_icon.png")
        self.message_chat_icon = self.message_chat_icon.subsample(16, 16) # Resizing the image
        self.message_chat_icon_label = tk.Label(master=frame, image=self.message_chat_icon, bg="cornflowerblue")
        self.message_chat_icon_label.pack()
        self.message_chat_icon_label.place(x=50, y=200)

        # Creating and configuring the public text chat name
        self.chat_name_label = tk.Label(master=frame, text="Salon Message Privé", bg="RoyalBlue4", fg="white", width=20, height=1)
        self.chat_name_label.pack()
        self.chat_name_label.config(font=("Agency FB", 20, "italic"), relief="groove")
        self.chat_name_label.place(x=110, y=210)

        # Creating and configuring a welcome message with the user's name under the chat name
        self.welcome_message_label = tk.Label(master=frame, text=f"  Bienvenue sur le salon de discussion privé {self.master.firstname} {self.master.username}  ", bg="SlateGray4", fg="white")
        self.welcome_message_label.pack()
        self.welcome_message_label.config(font=("Agency FB", 20, "italic"))
        self.welcome_message_label.place(x=50, y=250)

    
        # Creating and configuring the area to show the sent and received messages
        self.message_area = tk.Text(master=frame, bg="RoyalBlue4", fg="black", width=80, height=16)
        self.message_area.pack()
        self.message_area.config(font=("Agency FB", 15), state="disabled")
        self.message_area.place(x=50, y=290)
        
        # Crate and configure the message entry and the send buttond
        self.message_entry = tk.Text(master=frame, width=53, height=1, font=("Agency FB", 20))
        self.message_entry.pack()
        self.message_entry.place(x=50, y=700)
        
        # Creating and configuring the send button
        self.send_button = tk.Button(master=frame, text="Envoyer",fg="white", bg="RoyalBlue4", command=self.send_message)
        self.send_button.pack()
        self.send_button.place(x=640, y=710)
        self.master.bind("<Return>", self.send_message)  # Binding the Enter key to the send_message method
 
        # Creating and configuring the emoji button
        emojis = ["😀", "😂", "😍", "😎", "😜", "😡", "😢", "😭", "😱", "🤩", "🥳", "🤔", "🤗", "💖", "👋", "😈", "💩", "🤬", "😻", "💔", "🙊", "🙈", "🙉", "👻"]
        section_length = len(emojis) // 3 # Getting the length of each section
        for i in range(section_length): # Looping through the first section of emojis
            emoji_button = tk.Button(master=frame, text=emojis[i], font=(20), bg="gray71", command=lambda i=i: self.insert_emoji(emojis[i]))
            emoji_button.pack()
            emoji_button.place(x=50 + (i * 50), y=750)
        for i in range(section_length, 2 * section_length): # Looping through the second section of emojis
            emoji_button = tk.Button(master=frame, text=emojis[i], font=(20), bg="gray71", command=lambda i=i: self.insert_emoji(emojis[i]))
            emoji_button.pack()
            emoji_button.place(x=50 + ((i - section_length) * 50), y=800)
        for i in range(2 * section_length, len(emojis)): # Looping through the third section of emojis
            emoji_button = tk.Button(master=frame, text=emojis[i], font=(20), bg="gray71", command=lambda i=i: self.insert_emoji(emojis[i]))
            emoji_button.pack()
            emoji_button.place(x=50 + ((i - 2 * section_length) * 50), y=850)
        
    


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


    def insert_emoji(self, emoji): # Method to insert an emoji into the message entry
        self.message_entry.insert("end", emoji)


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

    # Method emoji button and selection window
    def emoji_button(self):
        self.emoji_button = tk.Button(master=self, text="😀", command=self.emoji_selection)
        self.emoji_button.pack()
        self.emoji_button.place(x=50, y=750)
    
    def emoji_selection(self):
        self.emoji_selection = tk.Toplevel(self)
        self.emoji_selection.title("Sélectionner un emoji")
        self.emoji_selection.geometry("200x200")
        self.emoji_selection.resizable(False, False)
        self.emoji_selection.config(bg="darkblue")
        self.emoji_selection.iconbitmap("Class/Front/Pictures/emoji.ico")
        self.emoji_selection.grab_set()
        self.emoji_selection.focus_set()
        self.emoji_selection.transient(master=self)
        self.emoji_selection.mainloop()
        

    def chat_deconnection(self):  # Method to return to the start page and get the user's info
        self.master.get_message(f"{self.master.firstname} {self.master.username} s'est déconnecté du chat", 2, datetime.datetime.now().strftime("%H:%M:%S  %d/%m/%Y"), False, True) # Adding the disconnection message to the database
        """ Must add method to get datetime into the database (table notification) and/or update it"""
        self.master.show_home_page()  # Calling the show_start_page method of the master attribute
    
    def display_message(self, message, message_type, datetime, author): # Method to display a message to the display area
        current_time = datetime
        self.message_area.config(state="normal")  # activating the edition
        if message_type == "sent":
            self.message_area.insert("end", f"{current_time}  \n - {author} : {message}  \n\n", ("sent", "right")) # adding the message to the display area
        elif message_type == "received":
            self.message_area.insert("end", f"{current_time}\n - {author} : {message}\n\n", ("received", "left")) # adding the message to the display area
        elif message_type == "connection":
            full_name = f"{self.master.firstname} {self.master.username}" # Getting the full name of the user
            self.message_area.insert("end", f"{current_time}\n {message}\n\n", ("connection", "center")) # adding the message to the display area
        else:  # disconnection
            self.message_area.insert("end", f"{current_time}\n - {message}\n\n", ("disconnection", "center")) # adding the message to the display area
        self.message_area.config(state="disabled")  # deasable the edition
        self.message_area.see("end")  # Scroll to the end of the text area
        self.message_area.tag_configure("sent", foreground="deep sky blue", justify="right") # Configuring the sent message tag
        self.message_area.tag_configure("received", foreground="ivory2", justify="left") # Configuring the received message tag
        self.message_area.tag_configure("connection", foreground="lime green", justify="center") # Configuring the connection message tag
        self.message_area.tag_configure("disconnection", foreground="red3", justify="center") # Configuring the disconnection message tag
    
    def get_message(self):  # Method to get the messages
        self.posts = self.master.get_post(2)
        for post in self.posts:
            author = self.master.get_author(post[2])
            if post[5] == 1:  # If the message is a connection message
                self.display_message(post[1], "connection", post[4], author) # Adding the message to the display area
            elif post[6] == 1:  # If the message is a disconnection message
                self.display_message(post[1], "disconnection", post[4], author)
            elif self.master.user_Id == post[2]:  # If the user is the author of the message
                self.display_message(post[1], "sent", post[4], author) 
            elif self.master.user_Id != post[2]: # If the user is not the author of the message
                self.display_message(post[1], "received", post[4], author)  
           
    def update_message(self):  # Method to update the messages
        self.posts = self.master.get_post(2)
        if len(self.posts) > self.count:
            self.message_area.config(state="normal")  # activating the edition
            self.message_area.delete("1.0", "end")
            self.message_area.config(state="disabled") # deasable the edition
            self.get_message()
            self.count = len(self.posts)
        self.after(50, self.update_message) # Calling the update_message method after 50 milliseconds

    def send_message(self, event=None): # Method to send a message
        message = self.message_entry.get("1.0", "end").strip()  # Getting the message from the entry and removing the leading and trailing whitespaces
        current_time = datetime.datetime.now().strftime("%H:%M:%S  %d/%m/%Y")  # Getting the current time
        self.message_entry.delete("1.0", "end") # Clearing the message entry
        if message:  # If the message is not empty
            self.master.get_message(message, 2, current_time, False, False) # Adding the message to the database
            self.play_received_sound()
        self.play_sending_sound()

    def play_sending_sound(self): # Method to play the sending sound
        self.sending_sound = pygame.mixer.Sound("Class/Back/Sounds/sending.mp3") # Loading the sending sound
        self.sending_sound.play()

    def play_received_sound(self):
        self.received_sound = pygame.mixer.Sound("Class/Back/Sounds/received.mp3")
        self.received_sound.play()

if __name__ == "__main__":  # If the script is run directly
    root = tk.Tk()  # Create an instance of the Tk class    
    app = PrivateTextChatPage(master=root)  # Create an instance of the StartPage class
    app.mainloop()  # Start the main event loop