import tkinter as tk

class ChatPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Page de chat")
        self.label.pack(pady=10)

        self.notification_button = tk.Button(self, text="Notifications", command=self.go_to_notifications)
        self.notification_button.pack(pady=5)

        self.logout_button = tk.Button(self, text="Déconnexion", command=self.logout)
        self.logout_button.pack(pady=5)

    def go_to_notifications(self):
        self.master.show_notification_page()

    def logout(self):
        # Ajoutez ici votre logique de déconnexion
        print("Déconnexion réussie")
        self.master.show_login_page()