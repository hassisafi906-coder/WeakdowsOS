# =====================================================================
#  Weakdows OS - Identity Shifting & Renaming Tool (Python)
# =====================================================================

import os
import sys

def shift_identity(target_directory):
    print(f"[WeakTools] Initializing Identity Shifting Engine on: {target_directory}")
    
    # كلمات البحث والاستبدال لتحويل الهوية البرمجية
    target_tokens = {
        "Windows": "Weakdows",
        "Microsoft": "WeakCorp",
        "WinOS": "WeakOS"
    }
    
    modified_files_count = 0
    
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            # تخطي ملف السكريبت نفسه ومجلدات البناء
            if file == "rename_identity.py" or ".git" in root or "target" in root:
                continue
                
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                
                updated = False
                for old_term, new_term in target_tokens.items():
                    if old_term in content:
                        content = content.replace(old_term, new_term)
                        updated = True
                
                if updated:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"[Shifter] Identity updated in: {file_path}")
                    modified_files_count += 1
                    
            except Exception as e:
                pass
                
    print(f"[SUCCESS] Identity shifting completed! Total modified files: {modified_files_count}")

if __name__ == "__main__":
    # مسار المشروع الافتراضي
    project_root = "."
    shift_identity(project_root)
