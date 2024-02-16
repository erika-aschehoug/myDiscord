import tkinter as tk

class NotificationPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Page de notifications")
        self.label.pack(pady=10)

        self.back_button = tk.Button(self, text="Retour au chat", command=self.go_to_chat)
        self.back_button.pack(pady=5)

    def go_to_chat(self):
        self.master.show_chat_page()