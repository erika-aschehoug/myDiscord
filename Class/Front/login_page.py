import tkinter as tk  # Importing the tkinter module for GUI
import datetime  # Importing the datetime module to work with dates and times

class LoginPage(tk.Frame):  # Creating a class StartPage which inherits from tk.Tk
    def __init__(self, master):  # Defining the constructor
        super().__init__(master)  # Calling the constructor of the parent class
        self.create_widget()

    
    def create_widget(self):
        frame = tk.Frame(master=self, bg="darkblue", width=750, height=900)
        frame.pack()

        self.master.title("Connexion")  # Setting the title of the window

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

        self.update_time()  # Calling the update_time method to display the current time and date
        
        # Create a frame for the login fields
        self.login_frame = tk.Frame(master=frame, bg="cornflowerblue", width=300, height=200)
        self.login_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create and place the email label and entry field
        self.email_label = tk.Label(self.login_frame, text="Identifiant (mail) : ", bg="cornflowerblue", fg="white", font=("Agency FB", 25, "italic"))
        self.email_label.grid(row=2, column=0, sticky='w')
        self.email_entry = tk.Entry(self.login_frame, font=("Agency FB", 20))
        self.email_entry.grid(row=2, column=1, sticky='ew', padx=(0, 25))  

        # Create and place the password label and entry field
        self.password_label = tk.Label(self.login_frame, text="Mot de passe :", bg="cornflowerblue", fg="white", font=("Agency FB", 25, "italic"))
        self.password_label.grid(row=3, column=0, sticky='w')
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Agency FB", 20))
        self.password_entry.grid(row=3, column=1, sticky='ew', padx=(0, 25))

        # Create and place the show password button
        self.show_password_button = tk.Button(self.login_frame, text="Afficher", width=10, bg="gray20", fg="white", font=("Agency FB", 15, "italic"), command=self.toggle_password)
        self.show_password_button.grid(row=3, column=2, sticky='e', padx=(0, 25))
        
        # Create and place the go back button
        self.go_back_button = tk.Button(self.login_frame, text="Retour", bg="darkblue", fg="white", font=("Agency FB", 15, "italic"), command=self.master.show_start_page)
        self.go_back_button.grid(row=4, column=0, sticky='ew', padx=(25, 5), pady=(0,10))

        # Create and place the connection button
        self.create_account_button = tk.Button(self.login_frame, text="Connexion", bg="darkblue", fg="white", font=("Agency FB", 18, "italic"), command=self.connection)
        self.create_account_button.grid(row=4, column=1, columnspan=2, sticky='ew', padx=(5, 25), pady=(0,10))
        # binding the enter key to the connection method
        self.master.bind('<Return>', lambda event: self.connection())

        # Create and place the error of entry or connection label
        self.error_label = tk.Label(self.login_frame, text="", bg="cornflowerblue", fg="darkred", font=("Agency FB", 25))
        self.error_label.grid(row=5, column=0, columnspan=3, sticky='ew', padx=(25, 25), pady=(0,10))
        

    # # Test the error of entry and connection
    def connection(self, event=None):
        # Code to create the account
        mail = self.email_entry.get()
        password = self.password_entry.get()
        self.master.get_login_variables(mail, password)

    def go_home(self):
        # Code to go back to the home page
        self.master.show_start_page()

    def update_time(self):  # Method to update the time and date
        current_time = datetime.datetime.now().strftime("%H:%M")  # Getting the current time
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")  # Getting the current date
        self.time_label.config(text=current_time)  # Updating the time label
        self.date_label.config(text=current_date)  # Updating the date label
        self.after(1000, self.update_time)  # Calling the update_time method after 1 second
        self.toggle_colon()  # Calling the toggle_colon method to blink the colon in the time
    
    def toggle_password(self):
            if self.password_entry.cget("show") == "*":
                self.password_entry.config(show="")
                self.show_password_button.config(text="Masquer")
            else:
                self.password_entry.config(show="*")
                self.show_password_button.config(text="Afficher")

    def toggle_colon(self):  # Method to blink the colon in the time
        current_time = self.time_label.cget("text")  # Getting the current time from the label
        if ":" in current_time:  # If the colon is in the time
            current_time = current_time.replace(":", " ")  # Replace the colon with a space
        else:  # If the colon is not in the time
            current_time = current_time.replace(" ", ":")  # Replace the space with a colon
        self.time_label.config(text=current_time)  # Updating the time label
        self.after(1000, self.toggle_colon)  # Calling the toggle_colon method after 1 second

    def set_error_entry(self):
        self.error_label.config(text="Erreur de connexion")
