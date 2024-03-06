import socket 
import pyaudio
import threading
import tkinter as tk

# audio configuration 
CHUNK = 1024            #size of datas audio sent and received (1024 octets)
FORMAT = pyaudio.paInt16    
CHANNELS = 1
RATE = 44100        #rate of audio / audio quality(taux d'échantillonage)

# Création Pyaudio object
audio = pyaudio.PyAudio()

# start audio
def play_audio(stream):  #stream is used to make the link between the file receive and the audio material of computer
    while True:
        data = conn.recv(CHUNK)  #data received from the connexion (conn) and indicate the size with (chunk)
        if not data:        #if nothing is received, means that the conn is closed so break
            break
        stream.write(data)   #write the data received on the audio flow (flux audio) stream    

# Function activated when button is pressed
def start_voice_chat():
    global conn
    global audio_thread
    conn, addr = server.accept()
    print(f"Connexion établie avec {addr}")
    # Starting the audio playback thread
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
    audio_thread = threading.Thread(target=play_audio, args=(stream,))
    audio_thread.start()

# Window creation
root = tk.Tk()
root.title("Voice Chat Server")

# button creation
start_button = tk.Button(root, text="Start Voice Chat", command=start_voice_chat)
start_button.pack()

# Server socket creation
server_host = '127.0.0.1'  # Server IP address
server_port = 5000         # Server listening port
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((server_host, server_port))
server.listen(1)  # Maximum number of pending connections

print("Serveur vocal en attente de connexion...")

# main loop GUI
root.mainloop()

# cleaning and closing GUI
conn.close()
server.close()
audio.terminate()
