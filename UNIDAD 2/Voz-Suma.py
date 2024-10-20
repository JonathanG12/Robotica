import sys
import os
import json
from vosk import Model, KaldiRecognizer
import pyaudio
import time

if not os.path.exists("model"):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    sys.exit(1)

model = Model("model")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Listening...")

word_to_num = {
    "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
    "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
    "diez": 10, "once": 11, "doce": 12, "trece": 13, "catorce": 14,
    "quince": 15, "dieciséis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
    "veinte": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50, 
    "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90,
    "cien": 100, "doscientos": 200, "trescientos": 300, "cuatrocientos": 400,
    "quinientos": 500, "seiscientos": 600, "setecientos": 700, "ochocientos": 800,
    "novecientos": 900, "mil": 1000
}

def words_to_number(words):
    total = 0
    current = 0
    for word in words:
        if word in word_to_num:
            value = word_to_num[word]
            if value == 1000:  
                current *= value
                total += current
                current = 0
            else:
                current += value
    total += current  
    return total

while True:
    data = stream.read(8000)
    
    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()  
        result_dict = json.loads(result)  
        text = result_dict.get('text', '')  
        
        if text:
            print(f"Recognized: {text}") 
            
            if "suma" in text:
                words = text.split()
                numbers = []

                for word in words:
                    if word.isdigit():
                        numbers.append(int(word))
                    elif word in word_to_num:
                        numbers.append(word_to_num[word])

                total = sum(numbers)
                
                print(f"Números reconocidos: {numbers}")
                print(f"Resultado de la suma: {total}")
    else:
        pass
    time.sleep(0.1)  