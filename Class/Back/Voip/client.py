import socket
import pyaudio
import threading
import tkinter as tk

# Configuration audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Création d'une instance de PyAudio
audio = pyaudio.PyAudio()

# Fonction pour lire l'audio
def play_audio(stream):
    while True:
        data, _ = sock.recvfrom(CHUNK)
        stream.write(data)

# Fonction pour démarrer le chat vocal
def start_voice_chat():
    try:
        # Création d'un flux audio
        stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

        # Démarrage du thread pour lire l'audio
        play_thread = threading.Thread(target=play_audio, args=(stream,))
        play_thread.start()
    except Exception as e:
        print("Erreur lors de la lecture audio:", e)
        root.quit()

# Création d'un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 12345))  # Liaison à l'adresse et au port du serveur

# Création d'une interface graphique (GUI) avec Tkinter
root = tk.Tk()
root.title("Voice Chat Server")

# Bouton pour démarrer le chat vocal
start_button = tk.Button(root, text="Start Voice Chat", command=start_voice_chat)
start_button.pack()

# Fonction pour gérer la fermeture du serveur
def on_closing():
    sock.close()
    audio.terminate()
    root.destroy()

# Liaison de la fonction on_closing à l'événement de fermeture de la fenêtre
root.protocol("WM_DELETE_WINDOW", on_closing)

# Boucle principale de la GUI
root.mainloop()
