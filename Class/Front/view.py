import tkinter as tk
from Class.Front.start_page import StartPage
from Class.Front.login_page import LoginPage
from Class.Front.create_account_page import CreateAccountPage
from Class.Front.home_page import HomePage
from Class.Front.public_text_chat_page import PublicTextChatPage
from Class.Front.private_text_chat_page import PrivateTextChatPage

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

    # This method is used to get the user info and reset the user info

    def get_user_info(self):
        self.user_Id, self.username, self.firstname, self.user_mail = self.controller.get_user_info()

    def reset_user_info(self):
        self.user_Id = None
        self.username = None
        self.firstname = None
        self.user_mail = None
        self.controller.reset_user_info()


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
    
    def show_home_page(self):
        return self.show_page(HomePage)
    
    def show_public_text_chat_page(self):
        return self.show_page(PublicTextChatPage)
    
    def show_private_text_chat_page(self):
        return self.show_page(PrivateTextChatPage)
    
    def send_post(self, affiliate_chanel_id):
        return self.controller.send_post(affiliate_chanel_id)

    # get variables for controller

    def get_login_variables(self, mail, password):
        return self.controller.get_login_variables(mail, password)
    
    def set_error_login(self):
        return LoginPage.set_error_entry(self.current_page)
    
    def get_create_account_variables(self, name, firstname, email, password):
        return self.controller.get_create_account_variables(name, firstname, email, password)
    
    def get_message(self,message, chanel, date, connection, disconnection):
        self.message = message
        self.chanel = chanel
        self.date = date
        self.connection = connection
        self.disconnection = disconnection
        self.controller.send_post()
    
    # method for text chat

    def get_post(self, id_room):
        return self.controller.get_post(id_room)
    
    def get_all_users(self):
        return self.controller.get_all_users()
    
    def get_author(self, posts_user_id):
        return self.controller.get_author(posts_user_id)
