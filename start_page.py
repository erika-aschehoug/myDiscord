import tkinter as tk
import datetime

class StartPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Projet Discord")
        self.geometry("750x900")
        self.resizable(width=False, height=False)
        self.configure(bg="darkblue")

        self.time_label = tk.Label(self, bg="darkblue", fg="white")
        self.time_label.pack()
        self.time_label.config(font=("Agency FB", 40))
        self.time_label.place(x=660, y=20)

        self.date_label = tk.Label(self, bg="darkblue", fg="white")
        self.date_label.pack()
        self.date_label.config(font=("Agency FB", 25, "italic"))
        self.date_label.place(x=605, y=80)

        self.button_connexion = tk.Button(self, text="Connexion", bg="cornflowerblue", fg="white", width=35)
        self.button_connexion.pack()
        self.button_connexion.config(font=("Agency FB", 20, "italic"))  # Texte en italique
        self.button_connexion.place(x=210, y=390)

        self.button_creation = tk.Button(self, text="Création de compte", bg="cornflowerblue", fg="white", width=35)
        self.button_creation.pack()
        self.button_creation.config(font=("Agency FB", 20, "italic"))
        self.button_creation.place(x=210, y=460)

        self.update_time()

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.toggle_colon()  # Appel de la fonction pour faire clignoter les deux-points

    def toggle_colon(self):
        current_time = self.time_label.cget("text")
        if ":" in current_time:
            current_time = current_time.replace(":", " ")
        else:
            current_time = current_time.replace(" ", ":")
        self.time_label.config(text=current_time)
        self.after(1000, self.toggle_colon)

if __name__ == "__main__":
    app = StartPage()
    app.mainloop()
