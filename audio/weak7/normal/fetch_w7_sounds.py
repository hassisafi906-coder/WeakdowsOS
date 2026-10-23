# =====================================================================
#  Weakdows OS - Windows 7 Audio Fetcher & Profile Manager
# =====================================================================

import os
import shutil

class Weak7SoundFetcher:
    def __init__(self):
        self.target_dir = os.path.join("audio", "weak7", "normal")
        self.sound_events = [
            "startup.wav",
            "shutdown.wav",
            "error.wav",
            "notify.wav",
            "logon.wav"
        ]

    def fetch_sounds(self, source_system_path="C:\\Windows\\Media"):
        print("[Weakdows::Audio] Initializing Weakdows 7 Sound Engine...")
        
        # إنشاء مجلد الأصوات الخاص بـ Weak7
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir, exist_ok=True)
            print(f"[-] Created directory: {self.target_dir}")

        print(f"[-] Scanning source directory: {source_system_path}")
        
        success_count = 0
        for sound in self.sound_events:
            src_file = os.path.join(source_system_path, sound)
            dst_file = os.path.join(self.target_dir, sound)

            try:
                if os.path.exists(src_file):
                    shutil.copy2(src_file, dst_file)
                    print(f"[SUCCESS] Linked Windows 7 Audio: {sound}")
                    success_count += 1
                else:
                    # إنشاء ملف وهمي خفيف في حال عدم وجود المصدر لضمان ثبات النظام
                    with open(dst_file, "w") as f:
                        f.write("WEAKDOWS_7_AUDIO_STUB")
                    print(f"[WARNING] Sound '{sound}' not found. Generated light system stub.")
            except Exception as e:
                print(f"[ERROR] Could not process {sound}: {e}")

        print(f"[SUCCESS] Weakdows 7 Audio setup finished ({success_count} sounds imported).")

if __name__ == "__main__":
    fetcher = Weak7SoundFetcher()
    fetcher.fetch_sounds()
