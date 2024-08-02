import speech_recognition as sr
import pyttsx3
import os
import requests
import time
from facerecog import *
from gtts import gTTS
import pygame
from gpt import get_chat_response


engine = pyttsx3.init()

def speak(text):
    tts = gTTS(text, lang="id", slow=False)
    tts.save("temp.mp3")

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue
    pygame.quit()

def Elektra():
    srec = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Mendengarkan...")
        srec.adjust_for_ambient_noise(mic, duration=0.2)
        sound = srec.listen(mic)
    try:
        # time.sleep(5)
        response = srec.recognize_google(sound, language="id-ID")
        response = response.lower()
        print("User:", response)
    except Exception as e:
            # pass
            print("Elektra: Tolong katakan lagi")
            speak("Tolong katakan lagi")
            response = "Tolong katakan lagi"
    return response

def stopping(text):
    word = text.split()
    word_leng = len(word)
    if word_leng > 50:
        text = get_chat_response(f"{text} rangkum teks tersebut dalam 1 paragraf")
    return text

def name(text):
    with open("name.txt", "a") as file:
        file.write(text)

def opening():
    print('Halo saya Elektra, katakan sesuatu')
    speak('Halo saya Elektra, katakan sesuatu')

def main():
    response = Elektra()
    print(response)
    if "Tolong katakan lagi" in response:
        main()
    elif "keluar" in response:
        print("Elektra: Sampai jumpa lagi, terimakasih...")
        speak("Sampai jumpa lagi, terimakasih...")
        time.sleep(3)
        exit()
    elif "nama saya" in response:
        print(f"Okeh Nama kamu adalah {nama}")
        speak("Okeh Nama kamu sudah di simpan")
        facerecog(nama)
        name(nama)
    else:
        speak("Tunggu sebentar...")
        res = get_chat_response(response)
        word = res.split()
        word_leng = len(word)
        if word_leng > 50:
            res = get_chat_response(f"{res} rangkum teks tersebut dalam 1 paragraf")
        print(word_leng > 50)
        print("Elektra:", res)
        speak(res)

while True:
    opening()
    main()
