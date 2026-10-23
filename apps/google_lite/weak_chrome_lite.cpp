// =====================================================================
//  Weakdows OS - Weak Chrome Lite Browser (C++)
// =====================================================================

#include <iostream>
#include <string>

class WeakChromeLite {
private:
    std::string homepage;
    bool memorySaverEnabled;

public:
    WeakChromeLite(std::string url) {
        homepage = url;
        memorySaverEnabled = true;
        std::cout << "[WeakChrome] Initialized with Memory Saver active. Homepage: " << homepage << "\n";
    }

    void navigateTo(const std::string& url) {
        std::cout << "[WeakChrome] Navigating securely to -> " << url << "\n";
        std::cout << "[WeakChrome] Low RAM mode active: Unnecessary background scripts blocked.\n";
    }
};

int main() {
    WeakChromeLite browser("https://www.google.com");
    browser.navigateTo("https://github.com/weakdows-os");
    
    return 0;
}
