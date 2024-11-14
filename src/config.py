# src/config.py

# Drone bağlantı ayarları
DRONE_CONNECTION_STRING = '127.0.0.1:14550'

# Tehlike ve Tehdit Yönetimi Ayarları
THREAT_ANALYSIS = {
    "sensitivity_level": 0.8,  # Tehlike algılama hassasiyeti
    "emergency_response": True,  # Acil durum modunun etkinliği
}

# Jammer Yönetimi Ayarları
JAMMER_SETTINGS = {
    "active": True,  # Jammer aktif/pasif durumu
    "signal_strength": 0.75,  # Sinyal gücü
    "duration": 10,  # Jammer süresi (saniye)
}

# Tanıma Ayarları
RECOGNITION_SETTINGS = {
    "face_recognition_threshold": 0.6,  # Yüz tanıma hassasiyeti
    "sound_keywords": ["yardım", "tehdit"],  # Ses tanıma anahtar kelimeler
    "object_detection_classes": ["silah", "bıçak"]  # Tehdit içeren nesneler
}

# Harita ve Trafik Yönetimi Ayarları
MAP_MANAGEMENT = {
    "update_interval": 5,  # Harita güncelleme aralığı (saniye)
    "traffic_avoidance": True,  # Kalabalık alanlardan kaçınma
}

# Enerji Yönetimi Ayarları
ENERGY_SETTINGS = {
    "enable_conversion": True,  # Çevresel enerjiyi dönüştürme
    "battery_capacity": 100,  # Batarya kapasitesi (%)
}

# Zihin Etkileşimi Ayarları
TELEPATHY_SETTINGS = {
    "enable_telepathy": True,  # Zihin bağlantısı aktif/pasif
    "emotion_recognition": True,  # Duygu tanıma aktif/pasif
}
