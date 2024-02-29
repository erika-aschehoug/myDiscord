import tkinter as tk
from tkinter import font
from audio_capture import AudioRecorder

class VoiceChat(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Chat Vocal")
        self.master.geometry("750x900")
        self.master.configure(bg="darkblue")
        self.pack()

        custom_font = font.Font(family="Bombardier", size=15, weight="normal")

        self.center_block = tk.Frame(self.master, bg="grey", width=300, height=300)
        self.center_block.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        chat_label = tk.Label(self.center_block, text="Chat Vocal", bg="grey", fg="white", font=("Bombardier", 20))
        chat_label.place(relx=0.05, rely=0.05, anchor=tk.NW)

        # add button to record
        self.record_button = tk.Button(self.center_block, text="Démarrer l'enregistrement...", bg="cornflowerblue", fg="white", font=custom_font, width=29, command=self.start_recording)
        self.record_button.place(relx=0.05, rely=0.95, anchor=tk.SW)

        # Initialiser audio recording
        self.audio_recorder = AudioRecorder(output_folder="C:/Users/user/Desktop/LAPLATEFORME/myDiscord/audio")

        # button2 = tk.Button(self.center_block, text="Send", bg="cornflowerblue", fg="white", font=custom_font, width=15)
        # button2.place(relx=0.95, rely=0.95, anchor=tk.SE)

    def start_recording(self):
        # record audio when button is clicked
        self.audio_recorder.record_audio(record_seconds=10)
        print("Record finished.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceChat(master=root)
    app.mainloop()
