import tkinter as tk
#from start_page import StartPage
from chat_page import ChatPage
from login_page import LoginPage
from create_account_page import CreateAccountPage
#from home_page import HomePage
from notification_page import NotificationPage
# from public_voice_chat_page import PublicVoiceChatPage
# from private_voice_chat_page import PrivateVoiceChatPage
# from public_text_chat_page import PublicTextChatPage
# from private_text_chat_page import PrivateTextChatPage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Application de chat")
        self.geometry("400x300")
        
        self.current_page = None
        self.show_login_page()

    # def show_start_page(self):
    #     if self.current_page:
    #         self.current_page.destroy()
    #     self.current_page = StartPage(self)
    #     self.current_page.pack()

    def show_login_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = LoginPage(self)
        self.current_page.pack()

    def show_create_account_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = CreateAccountPage(self)
        self.current_page.pack()

    def show_chat_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = ChatPage(self)
        self.current_page.pack()


    # def show_home_page(self):
    #     if self.current_page:
    #         self.current_page.destroy()
    #     self.current_page = HomePage(self)
    #     self.current_page.pack()

    def show_notification_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = NotificationPage(self)
        self.current_page.pack()
"""
    def show_public_voice_chat_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = PublicVoiceChatPage(self)
        self.current_page.pack()

    def show_private_voice_chat_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = PrivateVoiceChatPage(self)
        self.current_page.pack()

    def show_public_text_chat_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = PublicTextChatPage(self)
        self.current_page.pack()

    def show_private_text_chat_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = PrivateTextChatPage(self)
        self.current_page.pack()
"""
if __name__ == "__main__":
    app = Application()
    app.mainloop()
