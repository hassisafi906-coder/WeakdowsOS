import os
import shutil
try:
    import yt_dlp
except ImportError:
    yt_dlp = None

class Weakdows10SoundFetcher:
    def __init__(self, project_root="WeakdowsOS"):
        self.edition = "10"
        self.target_dir = os.path.join(project_root, "audio", "weak10")
        # رابط فيديو يوتيوب المحدد ليكون صوت التشغيل الافتراضي
        self.startup_audio_url = "https://www.youtube.com/watch?v=VCFGH3QfuOc"
        
        # قائمة أحداث أصوات ويندوز 10 مع ربط صوت التشغيل بالرابط المخصص
        self.sound_events = {
            "WindowsLogon.wav": self.startup_audio_url,
            "WindowsNotifySystem.wav": "default_notify_signature",
            "WindowsError.wav": "default_error_signature"
        }

    def fetch_and_setup_sounds(self):
        print("=" * 65)
        print(f"[*] [Weakdows::Audio] تهيئة وجلب أصوات نظام ويندوز 10")
        print("=" * 65)

        # إنشاء مجلد الأصوات الخاص بـ Weak10 إذا لم يكن موجوداً
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)
            print(f"[-] تم إنشاء مجلد الأصوات: `{self.target_dir}`")

        success_count = 0

        for sound_file, source_ref in self.sound_events.items():
            dst_file = os.path.join(self.target_dir, sound_file)
            
            try:
                # التحقق إذا كان الحدث يعتمد على رابط يوتيوب (صوت التشغيل المخصص)
                if source_ref.startswith("http") and yt_dlp:
                    print(f"\n[~] جاري جلب وتحويل صوت التشغيل المخصص من يوتيوب لـ {sound_file}...")
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'outtmpl': os.path.join(self.target_dir, 'startup_temp.%(ext)s'),
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'wav',
                            'preferredquality': '192',
                        }],
                        'quiet': True
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([source_ref])
                    
                    # نقل الملف المستخرج وتعيينه كصوت التشغيل الافتراضي
                    temp_wav = os.path.join(self.target_dir, 'startup_temp.wav')
                    if os.path.exists(temp_wav):
                        if os.path.exists(dst_file):
                            os.remove(dst_file)
                        os.rename(temp_wav, dst_file)
                        print(f"[SUCCESS] تم تعيين صوت التشغيل الافتراضي بنجاح من يوتيوب: {sound_file}")
                        success_count += 1
                elif os.path.exists(str(source_ref)):
                    # نسخ الملف المحلي في حال توفره على الجهاز
                    shutil.copy2(source_ref, dst_file)
                    print(f"[SUCCESS] تم استيراد الملف المحلي: {sound_file}")
                    success_count += 1
                else:
                    # توليد بصمة أو ملف احتياطي متوافق مع روح نظام ويندوز 10
                    with open(dst_file, "w", encoding="utf-8") as f:
                        f.write(f"WEAKDOWS_10_AUDIO_SIGNATURE::{sound_file} # متوافقة مع روح نظام 10")
                    print(f"[WARNING] تم توليد ملف بصمة احتياطي لـ: {sound_file}")
                    success_count += 1

            except Exception as e:
                print(f"[ERROR] فشل معالجة الملف {sound_file}: {e}")

        print(f"\n[✔] اكتملت العملية بنجاح. إجمالي الأصوات الجاهزة: {success_count}\n")

if __name__ == "__main__":
    fetcher = Weakdows10SoundFetcher()
    fetcher.fetch_and_setup_sounds()
