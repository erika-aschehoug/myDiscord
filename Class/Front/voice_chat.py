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

        #add record button
        button1 = tk.Button(self.master, text="Start / Stop record ...", bg="cornflowerblue", fg="white", font=custom_font, width=20)
        button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #add a button send 
        button2 = tk.Button(self.center_block, text="Send", bg="cornflowerblue", fg="white", font=custom_font, width=15)
        button2.place(relx=1.0, rely=1.0, anchor=tk.SE)

if __name__ == "__main__":
    root=tk.Tk()
    app = VoiceChat(master=root)
    app.mainloop()
