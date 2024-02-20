import tkinter as tk
from tkinter import font

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

#multiple choice menu
        self.menu_list = tk.Listbox(self.master, selectmode=tk.MULTIPLE, bg="grey", fg="white", font=custom_font)
        self.menu_list.insert(1, "Chat Vocal public")
        self.menu_list.insert(2, "Chat Vocal privé")
        self.menu_list.insert(3, "Chat message public")
        self.menu_list.insert(4, "Chat message privé")
        self.menu_list.place(relx=0, rely=0, anchor=tk.NW)

    
#add a block in center of window
        self.center_block= tk.Frame(self.master, bg="grey", width=300, height=300)
        self.center_block.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#add text zone
        chat_label=tk.Label(self.center_block, text="Chat Vocal", bg="grey", fg="white", font=("Bombardier", 20))
        chat_label.place(relx=0.05, rely=0.05, anchor=tk.NW)

if __name__ == "__main__":
    root=tk.Tk()
    app = VoiceChat(master=root)
    app.mainloop()