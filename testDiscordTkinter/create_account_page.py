import tkinter as tk

class CreateAccountPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Page de création de compte")
        self.label.pack(pady=10)

        self.back_button = tk.Button(self, text="Retour", command=self.go_to_login)
        self.back_button.pack(pady=5)

    def go_to_login(self):
        self.master.show_login_page()