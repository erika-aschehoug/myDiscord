import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk  # import module to manipulate picture

class VoiceChat(tk.Frame):        # window initialisation
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Chat Vocal") #window settings
        self.master.geometry("750x900")
        self.master.configure(bg="darkblue")
        self.pack()

        #menu
        custom_font = font.Font(family="Bombardier", size=15, weight="normal")

        #add a block in center of window
        self.center_block= tk.Frame(self.master, bg="grey", width=300, height=300)
        self.center_block.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        #add text zone
        chat_label=tk.Label(self.center_block, text="Chat Vocal", bg="grey", fg="white", font=("Bombardier", 20))
        chat_label.place(relx=0.05, rely=0.05, anchor=tk.NW)

        #download picture 
        image = Image.open("micro.png")
        image = image.resize((50, 50))  
        photo = ImageTk.PhotoImage(image)

        #add round button 
        self.round_button = tk.Canvas(self.center_block, width=100, height=100, bg="grey", highlightthickness=0)
        self.round_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.round_button.create_oval(0, 0, 100, 100, fill="cornflowerblue")
        self.round_button.create_image(50, 50, image=photo)
        self.round_button.image = photo  # Garder une référence à l'image pour éviter qu'elle ne soit supprimée par le garbage collector

        # Add four buttons that fill the entire height of the window
        button1 = tk.Button(self.master, text="Chat vocal privé", bg="cornflowerblue", fg="white", font=custom_font, width=20)
        button1.pack(fill=tk.Y, expand=True, anchor=tk.W)

        button2 = tk.Button(self.master, text="Chat vocal public", bg="cornflowerblue", fg="white", font=custom_font, width=20)
        button2.pack(fill=tk.Y, expand=True, anchor=tk.W)

        button3 = tk.Button(self.master, text="Chat message public", bg="cornflowerblue", fg="white", font=custom_font, width=20)
        button3.pack(fill=tk.Y, expand=True, anchor=tk.W)

        button4 = tk.Button(self.master, text="Chat message privé", bg="cornflowerblue", fg="white", font=custom_font, width=20)
        button4.pack(fill=tk.Y, expand=True, anchor=tk.W)

if __name__ == "__main__":
    root=tk.Tk()
    app = VoiceChat(master=root)
    app.mainloop()
