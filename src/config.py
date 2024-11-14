# src/config.py

# Tehlike ve Güvenlik Ayarları
THREAT_ANALYSIS = {
    "sensitivity_level": 0.8,
    "emergency_response": True,
}

# Jammer Ayarları
JAMMER_SETTINGS = {
    "active": True,
    "signal_strength": 0.75,
    "duration": 10,
}

# Tanıma Ayarları
RECOGNITION_SETTINGS = {
    "face_recognition_threshold": 0.6,
    "sound_keywords": ["yardım", "tehdit"],
    "object_detection_classes": ["silah", "bıçak"]
}

# Harita ve Trafik Yönetimi Ayarları
MAP_MANAGEMENT = {
    "update_interval": 5,
    "traffic_avoidance": True,
}

# Enerji Yönetimi Ayarları
ENERGY_SETTINGS = {
    "enable_conversion": True,
    "battery_capacity": 100,
}

# Telepatik Etkileşim Ayarları
TELEPATHY_SETTINGS = {
    "enable_telepathy": True,
    "emotion_recognition": True,
}
