# =====================================================================
#  Weakdows OS - Windows XP Audio Fetcher & Linker
# =====================================================================

import os
import shutil

class XPSoundFetcher:
    def __init__(self):
        self.target_dir = os.path.join("audio", "xp", "normal")
        self.sound_events = ["startup.wav", "shutdown.wav", "error.wav", "notify.wav"]

    def fetch_sounds(self, source_system_path="C:\\Windows\\Media"):
        print(f"[Weakdows::Audio] Initializing XP Sound Fetcher...")
        
        # إنشاء المجلد المستهدف إذا لم يكن موجوداً
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir, exist_ok=True)
            print(f"[-] Created target directory: {self.target_dir}")

        print(f"[-] Scanning source path: {source_system_path}")
        
        success_count = 0
        for sound in self.sound_events:
            src_file = os.path.join(source_system_path, sound)
            dst_file = os.path.join(self.target_dir, sound)

            try:
                if os.path.exists(src_file):
                    shutil.copy2(src_file, dst_file)
                    print(f"[SUCCESS] Imported: {sound}")
                    success_count += 1
                else:
                    # محاكاة وإنشاء ملف فارغ خفيف في حال عدم توفر المصدر لضمان عمل النظام بدون أخطاء
                    with open(dst_file, "w") as f:
                        f.write("WEAKDOWS_XP_AUDIO_STUB")
                    print(f"[WARNING] Source not found for {sound}. Created lightweight system stub.")
            except Exception as e:
                print(f"[ERROR] Failed to process {sound}: {e}")

        print(f"[SUCCESS] XP Audio Fetcher completed! {success_count} sounds linked to Weakdows XP.")

if __name__ == "__main__":
    fetcher = XPSoundFetcher()
    # يمكنك تغيير المسار حسب مكان تثبيت النظام القديم أو ترك الافتراضي
    fetcher.fetch_sounds()
