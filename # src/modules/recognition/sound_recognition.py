# src/modules/recognition/sound_recognition.py

class SoundRecognition:
    def __init__(self, config):
        self.keywords = config["sound_keywords"]

    def detect_sound(self):
        print("Anahtar kelimeler dinleniyor...")
        # Anahtar kelimelere göre ses tanıma
