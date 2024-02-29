import tkinter as tk
from tkinter import font
from audio_capture import AudioRecorder
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

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

        self.record_button = tk.Button(self.center_block, text="Enregistrer", bg="cornflowerblue", fg="white", font=custom_font, width=15, command=self.start_recording)
        self.record_button.place(relx=0.05, rely=0.95, anchor=tk.SW)

        self.audio_recorder = AudioRecorder(output_folder="C:/Users/user/Desktop/LAPLATEFORME/myDiscord/audio")

        button2 = tk.Button(self.center_block, text="Send", bg="cornflowerblue", fg="white", font=custom_font, width=15)
        button2.place(relx=0.95, rely=0.95, anchor=tk.SE)

    def start_recording(self):
        # Enregistrer l'audio lorsque le bouton est cliqué
        self.audio_recorder.record_audio(record_seconds=10)
        print("Enregistrement terminé.")
        # Afficher une barre de son dans le carré gris
        self.plot_audio_waveform()

    def plot_audio_waveform(self):
        # Lire le fichier audio enregistré
        audio_data, sample_rate = self.audio_recorder.read_audio_file()
        # Créer un axe pour le tracé
        plt.figure(figsize=(6, 4))
        plt.plot(np.linspace(0, len(audio_data) / sample_rate, num=len(audio_data)), audio_data)
        plt.xlabel("Temps (s)")
        plt.ylabel("Amplitude")
        plt.title("Barre de son de l'enregistrement audio")
        plt.grid(True)
        # Afficher le tracé dans le carré gris
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.center_block)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        plt.close()  # Fermer la fenêtre de tracé

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceChat(master=root)
    app.mainloop()
