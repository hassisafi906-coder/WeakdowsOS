# =====================================================================
#  Weakdows OS - WeakExplorer (Low-RAM File Manager)
# =====================================================================

import os
import sys

class WeakExplorer:
    def __init__(self, start_path="C:\\"):
        self.current_path = start_path
        self.memory_footprint_mb = 18

    def list_directory(self):
        print(f"\n=========================================================")
        print(f" WeakExplorer Lite - Path: {self.current_path}")
        print(f"=========================================================")
        try:
            items = os.listdir(self.current_path)
            for item in items:
                full_path = os.path.join(self.current_path, item)
                item_type = "[DIR]" if os.path.isdir(full_path) else "[FILE]"
                print(f" {item_type:<7} {item}")
        except Exception as e:
            print(f"[ERROR] Cannot access path: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "C:\\"
    explorer = WeakExplorer(target)
    explorer.list_directory()
