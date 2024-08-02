# # from gtts import gTTS
# # import pygame
# # import tempfile
# # import os

# # # Initialize pygame mixer
# # pygame.mixer.init()

# # def text_to_speech(text):
# #     # Create a temporary file to store the speech audio
# #     temp_file = tempfile.NamedTemporaryFile(delete=True)

# #     # Convert text to speech and save it to the temporary file
# #     tts = gTTS(text=text, lang='en')
# #     tts.save(temp_file.name)

# #     # Load and play the speech using pygame mixer
# #     pygame.mixer.music.load(temp_file.name)
# #     pygame.mixer.music.play()

# #     # Wait for the audio to finish playing
# #     while pygame.mixer.music.get_busy():
# #         continue

# #     # Close the temporary file
# #     temp_file.close()

# # if __name__ == "__main__":
# #     text = "Hello, this is a real-time text-to-speech example in Python."
# #     text_to_speech(text)

# from gtts import gTTS
# import os
# import tempfile
# import pygame

# # Initialize pygame mixer
# pygame.mixer.init()

# def text_to_speech(text):
#     # Create a temporary directory to store the speech audio
#     temp_dir = tempfile.TemporaryDirectory()
#     temp_file_path = os.path.join(temp_dir.name, "output.mp3")

#     # Convert text to speech and save it as an audio file
#     tts = gTTS(text=text, lang='id')
#     tts.save(temp_file_path)

#     # Load and play the speech using pygame mixer
#     pygame.mixer.music.load(temp_file_path)
#     pygame.mixer.music.play()

#     # pygame.mixer.music.wait()
#     # Wait for the audio to finish playing
#     while pygame.mixer.music.get_busy():
#         continue

#     # Clean up the temporary directory and audio file
#     # with tempfile.TemporaryDirectory() as tempDir:
#     #     print(f"Direktori: {tempDir}")
#     # temp_dir.cleanup()

# if __name__ == "__main__":
#     text = "Bunga matahari adalah tanaman yang cantik dan menarik, dengan bunga besar yang selalu mengikuti matahari selama hari. Mereka sering ditanam sebagai dekorasi taman dan juga memiliki nilai ekologis penting karena menarik berbagai jenis serangga, terutama lebah, yang membantu dalam penyerbukan tanaman lainnya."
#     text_to_speech(text)


# from gtts import gTTS
# import pyttsx3

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# def text_to_speech(text):
#     # Convert text to speech using gTTS
#     tts = gTTS(text)
#     tts.save("temp.mp3")  # Save the speech as a temporary audio file

#     # Play the speech in real-time
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     text = "Hello, this is real-time text-to-speech in Python."
#     text_to_speech(text)

# from gtts import gTTS
# import pygame

# def text_to_speech(text):
#     tts = gTTS(text, lang="id", slow=False)
#     tts.save("temp.mp3")

#     pygame.init()
#     pygame.mixer.init()

#     pygame.mixer.music.load("temp.mp3")
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():
#         continue
#     pygame.quit()


# text_to_speech("haloo") 
# Memuat suara (ganti 'nama_suara.wav' dengan nama file suara Anda)
# sound = pygame.mixer.Sound('temp.mp3')

# Memutar suara

# Menunggu sampai suara selesai
# pygame.mixer.music.wait()
# pygame.time.wait(sound.get_length() * 1000)

# Menutup Pygame


import speech_recognition as sr

# Buat objek recognizer
recognizer = sr.Recognizer()

# Merekam suara dari mikrofon
with sr.Microphone() as source:
    print("Katakan sesuatu...")
    audio = recognizer.listen(source)

try:
    # Gunakan Google Web Speech API untuk mengenali teks dari audio
    text = recognizer.recognize_google(audio)
    print("Anda mengatakan: " + text)
except sr.UnknownValueError:
    print("Maaf, tidak dapat mengenali suara.")
except sr.RequestError as e:
    print("Error saat mengakses layanan Google: {0}".format(e))
