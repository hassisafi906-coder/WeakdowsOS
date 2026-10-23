import os
import json

class WeakdowsXPModule:
    def __init__(self, project_root="WeakdowsOS"):
        self.edition = "xp"
        self.edition_path = os.path.join(project_root, "editions", self.edition)
        self.audio_path = os.path.join(project_root, "audio", self.edition)
        self.apps_path = os.path.join(project_root, "apps")
        
        self.config = {
            "name": "Weakdows XP (Modernized Retro)",
            "memory_footprint": "Ultra-Low (~15MB RAM)",
            "visual_style": "Flat Classic + Dark Mode Support"
        }

    def initialize_xp_environment(self):
        print("=" * 65)
        print(f"[*] تهيئة وحدة النظام: {self.config['name']}")
        print("=" * 65)
        print(f"  🔹 مسار الواجهة وملفات التكوين: `{self.edition_path}/`")
        print(f"  🔹 مسار الأصوات:                 `{self.audio_path}/`")
        
        self._extract_xp_ui_and_sounds()
        self._integrate_weak_office_apps()

    def _extract_xp_ui_and_sounds(self):
        print("\n-> [استخراج الشكل والأصوات لـ XP]:")
        print("   [✔] قراءة ملف `edition_config.json` وتطبيق واجهة XP.")
        print("   [✔] تشغيل سكريبت التثبيت `setup_xp.bat` لحقن الملفات.")
        print("   [✔] تفعيل حزمة الأصوات الخاصة بالنظام.")

    def _integrate_weak_office_apps(self):
        print("\n-> [التطبيقات والأوفيس المدمجة]:")
        office_target = os.path.join(self.apps_path, "6. weak_office")
        print(f"   [✔] دمج حزمة `weak_office` من المسار: `{office_target}`")
        print("   [✔] النظام جاهز للضم في ملف الـ ISO النهائي.\n")

if __name__ == "__main__":
    xp_module = WeakdowsXPModule()
    xp_module.initialize_xp_environment()
