// =====================================================================
//  Weakdows OS - File Explorer Core (C++)
// =====================================================================

#include <iostream>
#include <string>
#include <vector>

class WeakExplorer {
private:
    std::string currentPath;

public:
    WeakExplorer(std::string startPath) {
        currentPath = startPath;
        std::cout << "[WeakExplorer] Initialized at root path: " << currentPath << "\n";
    }

    void listDirectory() {
        std::cout << "\n[WeakExplorer] Listing contents of: " << currentPath << "\n";
        std::cout << "========================================\n";
        std::cout << "  [DIR]  apps/\n";
        std::cout << "  [DIR]  core/\n";
        std::cout << "  [DIR]  assets/\n";
        std::cout << "  [FILE] Cargo.toml\n";
        std::cout << "  [FILE] CMakeLists.txt\n";
        std::cout << "========================================\n";
    }

    void navigate(const std::string& folderName) {
        currentPath += "/" + folderName;
        std::cout << "[WeakExplorer] Successfully navigated to -> " << currentPath << "\n";
    }
};

int main() {
    WeakExplorer explorer("C:/WeakdowsOS");
    explorer.listDirectory();
    explorer.navigate("apps");
    
    return 0;
}
