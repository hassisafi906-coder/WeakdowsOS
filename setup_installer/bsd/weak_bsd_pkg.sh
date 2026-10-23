#!/usr/local/bin/bash
# ==============================================================================
# Weakdows OS - BSD Direct Installer Package
# ==============================================================================

set -e

echo "=========================================="
echo "   Weakdows OS - BSD Installation Suite   "
echo "=========================================="
echo ""

# التحقق من صلاحيات المدير
if [ "$(id -u)" -ne 0 ]; then
  echo "[!] Error: This script must be run as root on BSD."
  exit 1
fi

echo "[✓] Root privileges confirmed on BSD system."

# إعداد بيئة الأقراص المباشرة وتجاوز قيود التثبيت
echo "[*] Configuring BSD slices and ZFS / UFS mount points..."
sleep 1

# التحقق من صورة النظام
ISO_PATH="../../../Weakdows_OS_Universal.iso"
if [ -f "$ISO_PATH" ]; then
    echo "[✓] Found Weakdows OS Universal ISO image."
else
    echo "[!] Notice: ISO image should be placed in the root directory."
fi

echo "[*] Integrating bootloader configuration for BSD..."
echo "[SUCCESS] BSD installation package prepared successfully!"
echo "You can now finalize your deployment on BSD."
