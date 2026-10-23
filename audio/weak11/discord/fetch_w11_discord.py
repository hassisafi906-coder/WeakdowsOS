# =====================================================================
#  Weakdows OS - Weak11 Discord Hybrid Audio Profile
# =====================================================================

import os

class Weak11DiscordAudio:
    def __init__(self):
        # المسار الخاص بأصوات Weak11 الهجينة مع ديسكورد
        self.target_dir = os.path.join("audio", "discord", "weak11")
        
        # مزيج سينمائي هادئ يدمج الآلات الموسيقية لـ Windows 11 مع نغمات Discord
        self.w11_discord_sounds = {
            "startup.wav": "W11_ATMOSPHERIC_LOGON_X_DISCORD_STREAM_START",  # نغمة تشغيل W11 الموسيقية + بدء البث
            "shutdown.wav": "W11_ATMOSPHERIC_LOGOFF_X_DISCORD_STREAM_END", # نغمة إغلاق W11 الهادئة + إنهاء البث
            "error.wav": "W11_ATMOSPHERIC_ERROR_X_DISCORD_DEAFEN",         # صوت أخطاء W11 الناعم + كتم السماعات
            "notify.wav": "W11_ATMOSPHERIC_NOTIFY_X_DISCORD_REACTION",     # إشعارات W11 اللطيفة + صوت التفاعلات (Reactions)
            "uac_prompt.wav": "W11_ATMOSPHERIC_UAC_X_DISCORD_JOIN_CALL"     # نغمة UAC الانسيابية + دخول المكالمة
        }

    def build_profile(self):
        print("[Weakdows::Audio] Building Atmospheric (Weak11) + Discord Hybrid Profile...")
        
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir, exist_ok=True)
            print(f"[-] Created directory: {self.target_dir}")

        success_count = 0
        for sound_file, signature in self.w11_discord_sounds.items():
            dst_file = os.path.join(self.target_dir, sound_file)
            try:
                with open(dst_file, "w") as f:
                    f.write(signature)
                print(f"[SUCCESS] Compiled Weak11-Discord sound -> {sound_file}")
                success_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to generate {sound_file}: {e}")

        print(f"[SUCCESS] Weak11 Discord Sound Profile ready! ({success_count} atmospheric hybrid tracks loaded).")

if __name__ == "__main__":
    profile = Weak11DiscordAudio()
    profile.build_profile()
