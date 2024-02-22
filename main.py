import tkinter as tk
from Class.Front.start_page import StartPage
from Class.Front.login_page import LoginPage
from Class.Front.create_account_page import CreateAccountPage
from Class.Back.Connection import Connection
#from home_page import HomePage
#from notification_page import NotificationPage
#from public_voice_chat_page import PublicVoiceChatPage
#from private_voice_chat_page import PrivateVoiceChatPage
#from public_text_chat_page import PublicTextChatPage
#from private_text_chat_page import PrivateTextChatPage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("MyDiscord")
        self.geometry("750x900")
        self.resizable(width=False, height=False)  # Making the window non-resizable
        
        self.current_page = None
        self.show_start_page()

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
    
    def login(self, mail, password):
        connection = Connection()
        return connection.login(mail, password)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
