// =====================================================================
//  Weakdows OS - Office Suite Engine (C++)
// =====================================================================

#include <iostream>
#include <string>
#include <cstdlib>

class WeakOfficeSuite {
private:
    std::string docName;
    bool isModified;

public:
    WeakOfficeSuite(std::string name) {
        docName = name;
        isModified = false;
        std::cout << "[WeakOffice] Initialized document workspace: " << docName << "\n";
    }

    void writeContent(const std::string& text) {
        std::cout << "[WeakOffice] Writing text to buffer -> \"" << text << "\"\n";
        isModified = true;
    }

    void saveDocument() {
        if (!isModified) {
            std::cout << "[WeakOffice] No changes to save.\n";
            return;
        }
        std::cout << "[WeakOffice] Saving document [" << docName << "] via Rust Memory Buffer...\n";
        
        // استدعاء محرك إدارة الذاكرة بـ Rust للحفظ السريع
        int exitCode = system("cargo run --bin memory_buffer --quiet");
        
        if (exitCode == 0) {
            std::cout << "[SUCCESS] Document saved securely and instantly via Rust engine!\n";
            isModified = false;
        } else {
            std::cout << "[WARNING] Memory buffer process returned exit code: " << exitCode << "\n";
        }
    }
};

int main() {
    WeakOfficeSuite myDoc("weak_sheet_project.wks");
    myDoc.writeContent("Hello from Weakdows Office - Ultra lightweight document processor.");
    myDoc.saveDocument();

    return 0;
}
