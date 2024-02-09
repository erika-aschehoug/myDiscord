import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Page de connexion")
        self.label.pack(pady=10)

        self.login_button = tk.Button(self, text="Connexion", command=self.login)
        self.login_button.pack(pady=5)

        self.create_account_button = tk.Button(self, text="Créer un compte", command=self.create_account)
        self.create_account_button.pack(pady=5)

    def login(self):
        # Ajoutez ici votre logique de connexion
        print("Connexion réussie")
        self.master.show_chat_page()

    def create_account(self):
        self.master.show_create_account_page()
