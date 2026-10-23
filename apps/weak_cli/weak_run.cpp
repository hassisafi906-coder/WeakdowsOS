// =====================================================================
//  Weakdows OS - CLI Command Runner & Execution Engine (C++)
// =====================================================================

#include <iostream>
#include <string>
#include <cstdlib>

class WeakCLIRunner {
public:
    void displayHeader() {
        std::cout << "=====================================================\n";
        std::cout << "       Weakdows OS - Secure CLI Runner v1.0         \n";
        std::cout << "=====================================================\n";
    }

    void executeCommand(const std::string& cmd) {
        std::cout << "[WeakCLI] Executing system command -> " << cmd << "\n";
        
        // تنفيذ الأوامر بأمان داخل بيئة النظام
        #ifdef _WIN32
            std::string fullCmd = "cmd.exe /c " + cmd;
        #else
            std::string fullCmd = cmd;
        #endif

        int result = system(fullCmd.c_str());
        if (result == 0) {
            std::cout << "[SUCCESS] Command executed successfully.\n";
        } else {
            std::cout << "[WARNING] Command returned exit code: " << result << "\n";
        }
    }
};

int main(int argc, char* argv[]) {
    WeakCLIRunner runner;
    runner.displayHeader();

    if (argc > 1) {
        std::string commandToRun = "";
        for (int i = 1; i < argc; ++i) {
            commandToRun += std::string(argv[i]) + " ";
        }
        runner.executeCommand(commandToRun);
    } else {
        std::cout << "[-] No command provided. Running default system diagnostic...\n";
        runner.executeCommand("echo Weakdows CLI Environment is Active.");
    }

    return 0;
}
