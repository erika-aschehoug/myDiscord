import tkinter as tk  # Importing the tkinter module for GUI
import datetime  # Importing the datetime module to work with dates and times

class StartPage(tk.Frame):  # Creating a class StartPage which inherits from tk.Tk
    def __init__(self, master=None):  # Defining the constructor
        super().__init__(master)  # Calling the constructor of the parent class
        self.master.title("Accueil")  # Setting the title of the window
        self.master.geometry("750x900")  # Setting the size of the window
        self.master.resizable(width=False, height=False)  # Making the window non-resizable
        self.master.configure(bg="darkblue")  # Setting the background color of the window

        # Creating and configuring the time label
        self.time_label = tk.Label(self.master, bg="darkblue", fg="white")
        self.time_label.pack()
        self.time_label.config(font=("Agency FB", 40))
        self.time_label.place(x=645, y=20)

        # Creating and configuring the date label
        self.date_label = tk.Label(self.master, bg="darkblue", fg="white")
        self.date_label.pack()
        self.date_label.config(font=("Agency FB", 25, "italic"))
        self.date_label.place(x=605, y=80)

        # Creating and configuring the connection button
        self.button_connexion = tk.Button(self.master, text="Connexion", bg="cornflowerblue", fg="white", width=35, command=self.master.show_login_page)
        self.button_connexion.pack()
        self.button_connexion.config(font=("Agency FB", 20, "italic")) 
        self.button_connexion.place(x=210, y=390)

        # Creating and configuring the account creation button
        self.button_creation = tk.Button(self.master, text="Création de compte", bg="cornflowerblue", fg="white", width=35, command=self.master.show_create_account_page)
        self.button_creation.pack()
        self.button_creation.config(font=("Agency FB", 20, "italic"))
        self.button_creation.place(x=210, y=460)

        self.update_time()  # Calling the update_time method to display the current time and date

    def update_time(self):  # Method to update the time and date
        current_time = datetime.datetime.now().strftime("%H:%M")  # Getting the current time
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")  # Getting the current date
        self.time_label.config(text=current_time)  # Updating the time label
        self.date_label.config(text=current_date)  # Updating the date label
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
    app = StartPage()  # Create an instance of the StartPage class
    app.mainloop()  # Start the main event loop
