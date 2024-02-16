import tkinter as tk
from login_page import LoginPage
from create_account_page import CreateAccountPage
from chat_page import ChatPage
from testDiscordTkinter.notification_page import NotificationPage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Application de chat")
        self.geometry("400x300")
        
        self.login_page = LoginPage(self)
        self.create_account_page = CreateAccountPage(self)
        self.chat_page = ChatPage(self)
        self.notification_page = NotificationPage(self)
        
        self.show_login_page()

    def show_login_page(self):
        self.create_account_page.pack_forget()
        self.chat_page.pack_forget()
        self.notification_page.pack_forget()
        self.login_page.pack()

    def show_create_account_page(self):
        self.login_page.pack_forget()
        self.create_account_page.pack()

    def show_chat_page(self):
        self.login_page.pack_forget()
        self.create_account_page.pack_forget()
        self.notification_page.pack_forget()
        self.chat_page.pack()

    def show_notification_page(self):
        self.chat_page.pack_forget()
        self.notification_page.pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
