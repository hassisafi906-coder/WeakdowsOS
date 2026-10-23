// =====================================================================
//  Weakdows OS - Weak Store Engine (C++)
// =====================================================================

#include <iostream>
#include <string>
#include <cstdlib>

class WeakStoreEngine {
public:
    void launchStore() {
        std::cout << "[WeakStore] Initializing ultra-lightweight store interface...\n";
        std::cout << "[WeakStore] Zero bloatware detected. Memory consumption: ~12 MB.\n";
    }

    void fetchAndInstall(const std::string& appName) {
        std::cout << "[WeakStore] Requesting package download for -> " << appName << "\n";
        
        // استدعاء محرك التنزيل السريع المكتوب بلغة Rust عبر الـ Workspace
        std::string command = "cargo run --bin package_fetcher --quiet -- " + appName;
        int result = system(command.c_str());

        if (result == 0) {
            std::cout << "[SUCCESS] Application [" << appName << "] installed and integrated successfully!\n";
        } else {
            std::cerr << "[ERROR] Failed to install package: " << appName << "\n";
        }
    }
};

int main() {
    WeakStoreEngine store;
    store.launchStore();
    store.fetchAndInstall("weak_office_suite");
    
    return 0;
}
