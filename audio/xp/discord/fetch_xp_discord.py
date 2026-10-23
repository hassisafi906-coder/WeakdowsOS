# =====================================================================
#  Weakdows OS - WeakXP Discord Hybrid Audio Profile
# =====================================================================

import os

class WeakXPDiscordAudio:
    def __init__(self):
        # توجيه الملفات مباشرة إلى مجلد ديسكورد الخاص بنسخة إكس بي
        self.target_dir = os.path.join("audio", "discord", "xp")
        
        # مزيج أسطوري يجمع بين حنين أصوات إكس بي و نغمات ديسكورد
        self.xp_discord_sounds = {
            "startup.wav": "XP_LOGON_X_DISCORD_JOIN_CHANNEL",       # نغمة الدخول الأسطورية لإكس بي + ديسكورد
            "shutdown.wav": "XP_LOGOFF_X_DISCORD_LEAVE_CHANNEL",   # نغمة الإغلاق الكلاسيكية + مغادرة الروم
            "error.wav": "XP_CRITICAL_STOP_X_DISCORD_MUTE",        # صوت الخطأ الشهير (طبعا بالصوت الأسطوري المعروف!) + كتم الصوت
            "notify.wav": "XP_DING_X_DISCORD_MESSAGE_PING",        # صوت النبيه الكلاسيكي (Ding) + تنبيه رسائل ديسكورد
            "uac_prompt.wav": "XP_ASTERISK_X_DISCORD_UNDEAFEN"     # صوت التنبيه الإداري + إلغاء كتم السماعات
        }

    def build_profile(self):
        print("[Weakdows::Audio] Building Nostalgic WeakXP + Discord Hybrid Profile...")
        
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir, exist_ok=True)
            print(f"[-] Created directory: {self.target_dir}")

        success_count = 0
        for sound_file, signature in self.xp_discord_sounds.items():
            dst_file = os.path.join(self.target_dir, sound_file)
            try:
                with open(dst_file, "w") as f:
                    f.write(signature)
                print(f"[SUCCESS] Compiled XP-Discord sound -> {sound_file}")
                success_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to generate {sound_file}: {e}")

        print(f"[SUCCESS] WeakXP Discord Sound Profile ready! ({success_count} vintage-modern tracks loaded).")

if __name__ == "__main__":
    profile = WeakXPDiscordAudio()
    profile.build_profile()
