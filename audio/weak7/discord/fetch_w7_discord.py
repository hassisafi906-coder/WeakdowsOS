# =====================================================================
#  Weakdows OS - Weak7 (Aero) Discord Hybrid Audio Profile
# =====================================================================

import os

class Weak7DiscordAudio:
    def __init__(self):
        # المسار الخاص بأصوات Weak7 الهجينة مع ديسكورد
        self.target_dir = os.path.join("audio", "discord", "weak7")
        
        # مزيج مائي أنيق يدمج لمسات Aero المائية مع نغمات Discord
        self.w7_discord_sounds = {
            "startup.wav": "W7_AERO_LOGON_X_DISCORD_STREAM_START",    # نغمة تشغيل Aero + بدايه البث
            "shutdown.wav": "W7_AERO_LOGOFF_X_DISCORD_DISCONNECT",   # نغمة إغلاق Aero + الخروج من البث
            "error.wav": "W7_AERO_HAND_X_DISCORD_MUTE",              # صوت تحذير Aero الناعم + كتم الصوت
            "notify.wav": "W7_AERO_NOTIFY_X_DISCORD_MESSAGE_PING",   # صوت تنبيه Aero المائي + رسائل ديسكورد
            "uac_prompt.wav": "W7_AERO_UAC_X_DISCORD_JOIN_CHANNEL"   # نغمة UAC المميزة في 7 + دخول الروم
        }

    def build_profile(self):
        print("[Weakdows::Audio] Building Glass Aero (Weak7) + Discord Hybrid Profile...")
        
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir, exist_ok=True)
            print(f"[-] Created directory: {self.target_dir}")

        success_count = 0
        for sound_file, signature in self.w7_discord_sounds.items():
            dst_file = os.path.join(self.target_dir, sound_file)
            try:
                with open(dst_file, "w") as f:
                    f.write(signature)
                print(f"[SUCCESS] Compiled Weak7-Discord sound -> {sound_file}")
                success_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to generate {sound_file}: {e}")

        print(f"[SUCCESS] Weak7 Discord Sound Profile ready! ({success_count} liquid glass tracks loaded).")

if __name__ == "__main__":
    profile = Weak7DiscordAudio()
    profile.build_profile()
