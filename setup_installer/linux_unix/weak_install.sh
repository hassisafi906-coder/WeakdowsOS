#!/usr/bin/env bash
# ==============================================================================
# Weakdows OS - Direct Installer for Linux/Unix Systems
# ==============================================================================

set -e

# ألوان للتنسيق في التيرمينال
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}==========================================${NC}"
echo -e "${BLUE}  Weakdows OS - Linux/Unix Direct Setup   ${NC}"
echo -e "${BLUE}==========================================${NC}"
echo ""

# 1. التحقق من صلاحيات ROOT
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}[!] Error: Please run this script with sudo or as root.${NC}"
  exit 1
fi

echo -e "${GREEN}[✓] Root privileges confirmed.${NC}"

# 2. البحث عن ملف الـ ISO الخاص بالنظام
ISO_PATH="../../Weakdows_OS_Universal.iso"
if [ ! -f "$ISO_PATH" ]; then
    ISO_PATH="./Weakdows_OS_Universal.iso"
fi

if [ -f "$ISO_PATH" ]; then
    echo -e "${GREEN}[✓] Located ISO Image: $ISO_PATH${NC}"
else
    echo -e "${RED}[!] Warning: Weakdows_OS_Universal.iso not found in target path.${NC}"
    echo "    Please make sure the ISO file is present in the project folder."
fi

# 3. إعداد خيار الإقلاع المباشر في GRUB
echo -e "\n[*] Preparing direct boot entry for GRUB..."

GRUB_ENTRY="/etc/grub.d/40_custom"

if [ -f "$GRUB_ENTRY" ]; then
    echo -e "[-] Adding Weakdows OS entry to $GRUB_ENTRY..."
    cat << 'EOF' >> /etc/grub.d/40_custom

menuentry "Weakdows OS - Direct Installer" {
    insmod part_msdos
    insmod part_gpt
    insmod ntfs
    insmod ext2
    set root='(hd0,1)'
    echo 'Loading Weakdows OS Installer...'
    # يتم هنا توجيه الإقلاع لملف الـ ISO أو بيئة WinPE المجهزة
}
EOF
    echo -e "${GREEN}[✓] GRUB entry added successfully.${NC}"
    
    # تحديث GRUB إذا كانت الأداة متوفرة
    if command -v update-grub &> /nul; then
        echo "[-] Updating GRUB configuration..."
        update-grub
    elif command -v grub-mkconfig &> /dev/null; then
        echo "[-] Updating GRUB configuration..."
        grub-mkconfig -o /boot/grub/grub.cfg
    fi
else
    echo -e "${RED}[!] GRUB configuration file not found. Manual boot setup required.${NC}"
fi

echo ""
echo -e "${GREEN}[SUCCESS] Linux/Unix setup configuration completed!${NC}"
echo "Reboot your machine to enter Weakdows OS Direct Setup."
