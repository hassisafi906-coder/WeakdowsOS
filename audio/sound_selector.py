# =====================================================================
#  Weakdows OS - Master Audio Profile Selector & Sound Controller
# =====================================================================

import os
import json
import winsound  # لاستعراض وتشغيل أصوات WAV على أنظمة ويندوز خفيفة

class SoundSelector:
    def __init__(self):
        self.base_dir = "audio"
        self.config_file = os.path.join(self.base_dir, "active_audio_config.json")
        
        # الإصدارات المتاحة وأنماط البروفايلات الصوتية
        self.available_editions = ["xp", "weak7", "weak10", "weak11"]
        self.available_profiles = ["normal", "discord", "futuristic"]
        
        # الإعداد الافتراضي عند تشغيل المحرك لأول مرة
        self.current_config = {
            "active_edition": "weak11",
            "active_profile": "futuristic"
        }
        self.load_config()

    def load_config(self):
        """تحميل الإعدادات الصوتية المحفوظة"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    self.current_config = json.load(f)
                print(f"[Weakdows::Audio] Loaded Config: Edition -> [{self.current_config['active_edition'].upper()}], Profile -> [{self.current_config['active_profile'].upper()}]")
            except Exception as e:
                print(f"[WARN] Failed to read config, using defaults: {e}")

    def save_config(self):
        """حفظ الإعدادات الصوتية النشطة"""
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.current_config, f, indent=4)
            print("[SUCCESS] Audio configuration saved successfully!")
        except Exception as e:
            print(f"[ERROR] Could not save audio config: {e}")

    def set_profile(self, edition: str, profile_type: str):
        """تغيير بروفايل الأصوات النشط بالنظام"""
        edition = edition.lower()
        profile_type = profile_type.lower()

        if edition not in self.available_editions:
            print(f"[ERROR] Invalid edition '{edition}'. Choose from: {self.available_editions}")
            return False

        if profile_type not in self.available_profiles:
            print(f"[ERROR] Invalid profile type '{profile_type}'. Choose from: {self.available_profiles}")
            return False

        self.current_config["active_edition"] = edition
        self.current_config["active_profile"] = profile_type
        self.save_config()
        print(f"[AUDIO CHANGED] System Sound set to: {edition.upper()} ({profile_type.upper()} Mode)")
        return True

    def get_sound_path(self, event_name: str) -> str:
        """إرجاع المسار المباشر لملف الصوت الخاص بالحدث بناءً على البروفايل النشط"""
        edition = self.current_config["active_edition"]
        profile = self.current_config["active_profile"]

        # مسارات الترجيع المقترحة حسب هيكلية مجلدات المشروع
        possible_paths = [
            os.path.join(self.base_dir, profile, edition, f"{event_name}.wav"),
            os.path.join(self.base_dir, edition, profile, f"{event_name}.wav"),
            os.path.join(self.base_dir, profile, f"{event_name}.wav")
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        # مسار احتياطي استثنائي
        return os.path.join(self.base_dir, "normal", "startup.wav")

    def play_system_sound(self, event_name: str):
        """تشغيل حدث صوتي محدد بالاستعانة بالمكتبة الصوتية المدمجة"""
        sound_path = self.get_sound_path(event_name)
        print(f"[PLAYING AUDIO] Event: '{event_name}' -> Path: {sound_path}")
        
        if os.path.exists(sound_path):
            try:
                # تشغيل الصوت بشكل غير متزامن لتجنب تجميد الواجهة (SND_ASYNC)
                winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                print(f"[AUDIO PLAYBACK ERROR] Could not play sound file: {e}")
        else:
            print(f"[WARN] Audio file for '{event_name}' not found at location.")

if __name__ == "__main__":
    selector = SoundSelector()
    
    # اختبار المبدل الرئيسي
    print("\n--- Testing Weakdows Sound Selector ---")
    selector.set_profile(edition="weak11", profile_type="futuristic")
    selector.play_system_sound("startup")
    
    selector.set_profile(edition="xp", profile_type="discord")
    selector.play_system_sound("notify")
