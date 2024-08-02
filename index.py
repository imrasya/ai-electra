import speech_recognition as sr
import pyttsx3
import os
import requests
import time
from gtts import gTTS
import pygame
from gpt import get_chat_response
import tempfile

pygame.init()
pygame.mixer.init()

engine = pyttsx3.init()

def speak(text):
    tts = gTTS(text, lang="id", slow=False)
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file_name = temp_file.name
        tts.save(temp_file_name)

    # Load and play the temporary file
    sound = pygame.mixer.Sound(temp_file_name)
    sound.play()

    # Wait until sound finishes playing
    pygame.time.wait(int(sound.get_length() * 1000))

    # Clean up the temporary file
    os.remove(temp_file_name)

def Elektra():
    srec = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Mendengarkan...")
        srec.adjust_for_ambient_noise(mic, duration=0.2)
        sound = srec.listen(mic)
    try:
        response = srec.recognize_google(sound, language="id-ID")
        response = response.lower()
        print("User:", response)
    except sr.UnknownValueError:
        print("Elektra: Tolong katakan lagi")
        speak("Tolong katakan lagi")
        response = "Tolong katakan lagi"
    except sr.RequestError as e:
        print(f"Elektra: Tidak dapat mengenali suara; {e}")
        speak("Tidak dapat mengenali suara")
        response = "Tidak dapat mengenali suara"
    return response

def stopping(text):
    word = text.split()
    word_leng = len(word)
    if word_leng > 50:
        text = get_chat_response(f"{text} rangkum teks tersebut dalam 1 paragraf")
    return text

def name(text):
    with open("name.txt", "a") as file:
        file.write(f"{text}\n\n")

def opening():
    print('Halo saya Elektra, katakan sesuatu')
    speak('Halo saya Elektra, katakan sesuatu')

def main():
    response = Elektra()
    if "Tolong katakan lagi" in response:
        main()
    elif "keluar" in response:
        print("Elektra: Sampai jumpa lagi, terimakasih...")
        speak("Sampai jumpa lagi, terimakasih...")
        time.sleep(3)
        exit()
    else:
        speak("Tunggu sebentar...")
        res = get_chat_response(response)
        res = stopping(res)
        print("Elektra:", res)
        speak(res)

if __name__ == "__main__":
    while True:
        opening()
        main()
