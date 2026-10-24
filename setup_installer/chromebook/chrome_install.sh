#!/bin/bash

# ==============================================================================
# WeakdowsOS / ChromeOS Universal Installer Tool
# ==============================================================================

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=====================================================${NC}"
echo -e "${BLUE}       ChromeOS / WeakdowsOS Package Installer       ${NC}"
echo -e "${BLUE}=====================================================${NC}"

# 1. التحقق من صلاحيات Root
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}[!] يرجى تشغيل السكربت بصلاحيات الجذر (sudo ./chrome_install.sh)${NC}"
  exit 1
fi

# 2. البحث عن صورة النظام أو حزمة الـ ISO
IMAGE_PATH=""
for img in "../../chromeos.iso" "./chromeos.iso" "../../chromeos.bin" "./chromeos.img"; do
    if [ -f "$img" ]; then
        IMAGE_PATH="$img"
        break
    fi
done

if [ -z "$IMAGE_PATH" ]; then
    echo -e "${RED}[!] خطأ: لم يتم العثور على ملف صورة النظام (chromeos.iso / chromeos.bin / chromeos.img)!${NC}"
    echo -e "${YELLOW}يرجى وضع ملف صورة نظام كروم في مجلد المشروع.${NC}"
    exit 1
fi

echo -e "${GREEN}[✔] تم العثور على حزمة النظام: $IMAGE_PATH${NC}"

# 3. اختيار طريقة التثبيت
echo -e "\n${YELLOW}اختر طريقة التثبيت:${NC}"
echo "1) استخراج حزمة النظام إلى دليل /opt/chromeos (تثبيت مجلد)"
echo "2) كتابة/حرق صورة النظام على قرص تخزين أو USB (Full Disk Install)"
read -p "أدخل الخيار (1 أو 2): " CHOICE

case $CHOICE in
  1)
    INSTALL_DIR="/opt/chromeos"
    echo -e "${YELLOW}[*] جاري تجهيز الدليل $INSTALL_DIR...${NC}"
    mkdir -p "$INSTALL_DIR"
    
    echo -e "${YELLOW}[*] جاري فك واستخراج حزمة ChromeOS...${NC}"
    if command -v 7z &> /dev/null; then
        7z x "$IMAGE_PATH" -o"$INSTALL_DIR" -y > /dev/null
    elif command -v bsdtar &> /dev/null; then
        bsdtar -xf "$IMAGE_PATH" -C "$INSTALL_DIR"
    else
        echo -e "${RED}[!] يلزم توفر أداة 7z أو bsdtar لاستخراج الحزمة.${NC}"
        exit 1
    fi
    echo -e "${GREEN}[✔] تم استخراج وتثبيت نظام كروم بنجاح في: $INSTALL_DIR${NC}"
    ;;

  2)
    echo -e "\n${RED}تنبيه: هذه العملية ستقوم بمسح البيانات على القرص المستهدف!${NC}"
    lsblk -d -n -o NAME,SIZE,MODEL
    read -p "أدخل اسم القرص المستهدف (مثال: sdb أو nvme0n1): " TARGET_DISK
    
    if [ -b "/dev/$TARGET_DISK" ]; then
        echo -e "${YELLOW}[*] جاري كتابة حزمة النظام على /dev/$TARGET_DISK ...${NC}"
        dd if="$IMAGE_PATH" of="/dev/$TARGET_DISK" bs=4M status=progress conv=fsync
        echo -e "${GREEN}[✔] تم حرق وتثبيت نظام كروم على القرص /dev/$TARGET_DISK بنجاح!${NC}"
    else
        echo -e "${RED}[!] القرص /dev/$TARGET_DISK غير موجود!${NC}"
        exit 1
    fi
    ;;

  *)
    echo -e "${RED}[!] خيار غير صحيح. إلغاء العملية.${NC}"
    exit 1
    ;;
esac

echo -e "${GREEN}=====================================================${NC}"
echo -e "${GREEN}[✔] اكتملت عملية إعداد وتثبيت نظام كروم بنجاح!${NC}"
echo -e "${GREEN}=====================================================${NC}"
