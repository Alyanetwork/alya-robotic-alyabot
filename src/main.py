# src/main.py

from modules.security.threat_analysis import ThreatAnalysis
from modules.security.attack_prevention import AttackPrevention
from modules.security.jammer_control import JammerControl
from modules.recognition.face_recognition import FaceRecognition
from modules.recognition.sound_recognition import SoundRecognition
from modules.recognition.object_detection import ObjectDetection
from modules.mapping.map_management import MapManagement
from modules.mapping.traffic_analysis import TrafficAnalysis
from modules.energy.energy_converter import EnergyConverter
from modules.telepathy.neural_interface import NeuralInterface
from modules.telepathy.emotion_recognition import EmotionRecognition
from config import THREAT_ANALYSIS, JAMMER_SETTINGS, RECOGNITION_SETTINGS, MAP_MANAGEMENT, ENERGY_SETTINGS, TELEPATHY_SETTINGS

def main():
    # Güvenlik ve Tehdit Yönetimi
    threat_analysis = ThreatAnalysis(THREAT_ANALYSIS)
    attack_prevention = AttackPrevention()
    jammer = JammerControl(JAMMER_SETTINGS)

    # Tanıma Sistemleri
    face_recognition = FaceRecognition(RECOGNITION_SETTINGS)
    sound_recognition = SoundRecognition(RECOGNITION_SETTINGS)
    object_detection = ObjectDetection(RECOGNITION_SETTINGS)

    # Harita ve Trafik Yönetimi
    map_management = MapManagement(MAP_MANAGEMENT)
    traffic_analysis = TrafficAnalysis(MAP_MANAGEMENT)

    # Enerji Yönetimi
    energy_converter = EnergyConverter(ENERGY_SETTINGS)

    # Telepatik Bağlantı
    neural_interface = NeuralInterface(TELEPATHY_SETTINGS)
    emotion_recognition = EmotionRecognition(TELEPATHY_SETTINGS)

    # 1. Tehlike Analizi ve Güvenlik Önlemleri
    threat_detected = threat_analysis.analyze_threat()
    if threat_detected:
        print("Tehdit algılandı, acil durum moduna geçiliyor.")
        attack_prevention.activate_defense()
        jammer.activate_jammer()

    # 2. Yüz, Ses ve Nesne Tanıma
    face_recognition.identify_faces()
    sound_recognition.detect_sound()
    object_detection.identify_objects()

    # 3. Harita ve Trafik Yönetimi
    map_management.update_map()
    traffic_analysis.analyze_traffic()

    # 4. Enerji Yönetimi
    energy_converter.convert_environmental_energy()

    # 5. Telepatik Bağlantı ve Duygu Analizi
    neural_interface.connect()
    emotion = emotion_recognition.detect_emotion()
    print(f"Kullanıcının ruh hali: {emotion}")

if __name__ == "__main__":
    main()
