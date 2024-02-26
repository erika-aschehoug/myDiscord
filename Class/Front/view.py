import tkinter as tk
from Class.Front.start_page import StartPage
from Class.Front.login_page import LoginPage
from Class.Front.create_account_page import CreateAccountPage


class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("MyDiscord")
        self.geometry("750x900")
        self.resizable(width=False, height=False)  # Making the window non-resizable
        self.current_page = None
        self.show_start_page()

    # This method is used to start the application

    def main(self):
        self.mainloop()

    # This method is used to show a page

    def show_page(self, pagename):
        new_page = pagename(self)

        if self.current_page:
            self.current_page.pack_forget()
            self.current_page.destroy()

        self.current_page = new_page
        self.current_page.pack()

    def show_start_page(self):
        return self.show_page(StartPage)

    def show_login_page(self):
        return self.show_page(LoginPage)

    def show_create_account_page(self):
        return self.show_page(CreateAccountPage)
    
    
    def get_login_variables(self, mail, password):
        return self.controller.get_login_variables(mail, password)
    
    def get_create_account_variables(self, name, firstname, email, password):
        return self.controller.get_create_account_variables(name, firstname, email, password)
