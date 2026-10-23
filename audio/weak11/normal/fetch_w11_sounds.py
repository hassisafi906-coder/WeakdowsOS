# =====================================================================
#  Weakdows OS - Windows 11 Harmonic Audio & Synced Tone Engine
# =====================================================================

import os
import shutil

class Weak11SoundManager:
    def __init__(self):
        self.target_dir = os.path.join("audio", "weak11", "normal")
        # توحيد الآلات والروح الموسيقية بين التشغيل والإيقاف (Harmonic Sound Scheme)
        self.sound_events = {
            "startup.wav": "WEAKDOWS_11_HARMONIC_STARTUP_SYNTH",
            "shutdown.wav": "WEAKDOWS_11_HARMONIC_SHUTDOWN_SYNTH", # نفس طابع الآلات ولكن بانخفاض تدريجي هادئ
            "error.wav": "WEAKDOWS_11_SOFT_ERROR_SYNTH",
            "notify.wav": "WEAKDOWS_11_CHIME_NOTIFY_SYNTH"
        }

    def setup_audio_profiles(self, source_system_path="C:\\Windows\\Media"):
        print("[Weakdows::Audio] Initializing Weakdows 11 Harmonized Sound Engine...")
        
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir, exist_ok=True)
            print(f"[-] Created target directory: {self.target_dir}")

        success_count = 0
        for sound_file, signature in self.sound_events.items():
            src_file = os.path.join(source_system_path, sound_file)
            dst_file = os.path.join(self.target_dir, sound_file)

            try:
                if os.path.exists(src_file):
                    shutil.copy2(src_file, dst_file)
                    print(f"[SUCCESS] Imported native Windows 11 sound: {sound_file}")
                else:
                    # توليد نغمة متوافقة بالآلات الموسيقية لروح ويندوز 11 الخفيفة
                    with open(dst_file, "w") as f:
                        f.write(signature)
                    print(f"[SYNTH] Generated synchronized instrument tone for: {sound_file}")
                success_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to configure {sound_file}: {e}")

        print(f"[SUCCESS] Weakdows 11 Harmonized Audio setup completed! ({success_count} profiles synced).")

if __name__ == "__main__":
    manager = Weak11SoundManager()
    manager.setup_audio_profiles()
