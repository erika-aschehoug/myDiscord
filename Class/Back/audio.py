import pyaudio  #capture audio
import wave     #file format to read audio
import os       #make the link between record and current hour of recording
from datetime import datetime       #to have the precise date and hour of record
from pydub import AudioSegment
from pydub.playback import play
import mysql.connector

class AudioRecorder:
    def __init__(self, output_folder):
        self.CHUNK = 1024        # Size of audio data chunks (1024 bytes)
        self.FORMAT = pyaudio.paInt16  # Audio data format (16-bit, signed)
        self.CHANNELS = 1  # Number of audio channels (mono)
        self.RATE = 44100   # Audio sampling rate (44100 samples per second)
        self.output_folder = output_folder  # Output folder for audio files

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)  # Create the output folder if it doesn't exist

        self.audio = pyaudio.PyAudio()  # Initialize PyAudio object for handling audio input/output

    def record_audio(self, record_seconds=10):
        current_time = datetime.now()
        date_time_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        wave_output_filename = os.path.join(self.output_folder, f"{date_time_str}.wav")

        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

        print(f"Recording {wave_output_filename}...")

        frames = []  # List to store audio frames

        for _ in range(0, int(self.RATE / self.CHUNK * record_seconds)):
            data = stream.read(self.CHUNK)  # Read audio data from the stream
            frames.append(data)  # Append audio data to the frames list

        print(f"Finished recording {wave_output_filename}.")

        stream.stop_stream()  # Stop the audio stream
        stream.close()  # Close the audio stream

        # Write the audio data to a .wav file
        try:
            wf = wave.open(wave_output_filename, 'wb')  # Open a .wav file in binary write mode
            wf.setnchannels(self.CHANNELS)  # Set the number of channels
            wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))  # Set the sample width
            wf.setframerate(self.RATE)  # Set the sampling rate
            wf.writeframes(b''.join(frames))  # Write audio frames to the .wav file
            wf.close()  # Close the .wav file

            print(f"WAV file {wave_output_filename} written successfully.")

            #conversion wav file to blob
            audio_blob = open(wave_output_filename, "rb").read()

            #insert blob data into db
            record_time = datetime.now()
            self.insert_audio_blob(record_time, audio_blob)

        except Exception as e:
            print(f"Error writing WAV file or inserting into the database:", e)

    def connection_database(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="db_discord"
            )
            print("Connected to the database successfully.")
            return conn
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")
            return None

    def insert_audio_blob(self, record_time, audio_blob):
        conn = self.connection_database()
        if conn:
            try:
                cursor = conn.cursor()
                insert_query = "INSERT INTO audio_record (record_time, audio_blob) VALUES (%s, %s)"
                cursor.execute(insert_query, (record_time, audio_blob))
                conn.commit()
                cursor.close()
                conn.close()
                print("Audio blob inserted into the database successfully.")
            except mysql.connector.Error as e:
                print(f"Error inserting audio blob into the database: {e}")


    def close(self):
        self.audio.terminate()  # Terminate the PyAudio object

    def audio_player(self):
        conn = self.connection_database()
        if conn:
            try:
                cursor = conn.cursor()
                select_query = "SELECT audio_blob FROM audio_record ORDER BY record_time DESC LIMIT 1"
                cursor.execute(select_query)
                result = cursor.fetchone()
                if result:
                    audio_blob = result[0]      #list which contain the result of query sql
                    audio_filename = "latest_audio.wav"
                    with open(audio_filename, "wb") as audio_file:
                        audio_file.write(audio_blob)
                    audio = AudioSegment.from_file(audio_filename)  #read file      
                    play(audio)                 
                    print("Latest audio played successfully.")
                else:
                    print("No audio records found in the database.")
                cursor.close()
                conn.close()
            except mysql.connector.Error as e:
                print(f"Error retrieving latest audio from the database: {e}")


if __name__ == "__main__":
    recorder = AudioRecorder(output_folder="C:/Users/user/Desktop/LAPLATEFORME/myDiscord/audio")
    recorder.record_audio(record_seconds=10)
    recorder.close()

