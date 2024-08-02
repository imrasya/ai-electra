import speech_recognition as sr

# Buat objek recognizer
recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio, language="id-ID")
            text = text.lower()

            print(text)
    except sr.UnknownValueError():
        recognizer = sr.Recognizer()
        continue
        
# Merekam suara dari mikrofon
with sr.Microphone() as source:
    print("Katakan sesuatu...")
    audio = recognizer.listen(source)

