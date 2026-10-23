#!/bin/bash
# =====================================================================
#  Weakdows OS - Linux ISO Image Packer Script
# =====================================================================

echo "========================================================="
echo "       Weakdows OS - Image Packer (Linux/Unix)           "
echo "========================================================="

echo "[*] Preparing root filesystem and compressing W-Reg cache..."
sleep 0.4

# محاكاة إنشاء وضغط حزم النظام
echo "[-] Compressing editions (XP, Weak7, Weak10, Weak11)..."
sleep 0.5

echo "[-] Integrating bootloader configurations and XForce modules..."
sleep 0.5

OUTPUT_ISO="Weakdows_OS_Universal.iso"
echo "[SUCCESS] Image packed successfully into $OUTPUT_ISO!"
