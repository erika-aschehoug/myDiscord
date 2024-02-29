import pyaudio  #capture audio
import wave     #file format to read audio
import os       #make the link between record and current hour of recording
from datetime import datetime       #to have the precise date and hour of record
from pydub import AudioSegment
from pydub.playback import play
from base64 import b64encode

#save audio
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

        except Exception as e:
            print(f"Error writing WAV file {wave_output_filename}:", e)  # Display an error if writing the .wav file fails

    def close(self):
        self.audio.terminate()  # Terminate the PyAudio object

#play audio 

    def audio_player (self,audio_file):
        try:
            audio = AudioSegment.from_file(audio_file)
            play(audio)
            print(f"Audio {audio_file} played successfully")
        except Exception as e:
            print(f"Error playing audio {audio_file}:", e)

if __name__ == "__main__":
    recorder = AudioRecorder(output_folder="C:/Users/user/Desktop/LAPLATEFORME/myDiscord/audio")
    # recorder.record_audio(record_seconds=10)
    recorder.audio_player("C:/Users/user/Desktop/LAPLATEFORME/myDiscord/Class/Back/Voip/audio/2024-02-28_14-49-23.wav")
    recorder.close()
