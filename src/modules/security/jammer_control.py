# src/modules/security/jammer_control.py

class JammerControl:
    def __init__(self, config):
        self.active = config["active"]
        self.signal_strength = config["signal_strength"]
        self.duration = config["duration"]

    def activate_jammer(self):
        if self.active:
            print(f"Jammer devrede, sinyal gücü: {self.signal_strength}, süre: {self.duration} sn.")
            # Jammer kontrol kodları
