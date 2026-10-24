#!/bin/bash

# ==============================================================================
# WeakdowsOS - Universal Linux/Unix Package Installer
# ==============================================================================

# الألوان لتنسيق مخرجات الطرفية
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=====================================================${NC}"
echo -e "${BLUE}     WeakdowsOS - Universal Linux/Unix Installer     ${NC}"
echo -e "${BLUE}=====================================================${NC}"

# 1. التحقق من صلاحيات Root / Sudo
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}[!] يرجى تشغيل السكربت بصلاحيات الجذر (sudo ./weak_install.sh)${NC}"
  exit 1
fi

# 2. تحديد المسارات الأساسية
INSTALL_DIR="/opt/weakdows_os"
DESKTOP_ENTRY="/usr/share/applications/weakdows_os.desktop"
ISO_NAME="Weakdows_OS_v26H2.iso"

# البحث عن ملف الـ ISO في مجلدات المشروع
ISO_PATH=""
if [ -f "../../$ISO_NAME" ]; then
    ISO_PATH="../../$ISO_NAME"
elif [ -f "./$ISO_NAME" ]; then
    ISO_PATH="./$ISO_NAME"
elif [ -f "../$ISO_NAME" ]; then
    ISO_PATH="../$ISO_NAME"
else
    echo -e "${RED}[!] خطأ: لم يتم العثور على ملف $ISO_NAME في مسارات المشروع!${NC}"
    echo -e "${YELLOW}تأكد من وجود ملف الآيزو في مجلد المشروع الرئيسي.${NC}"
    exit 1
fi

echo -e "${GREEN}[✔] تم العثور على حزمة النظام: $ISO_PATH${NC}"

# 3. إنشاء دليل التثبيت المستقل
echo -e "${YELLOW}[*] جاري تجهيز مجلد التثبيت في $INSTALL_DIR...${NC}"
mkdir -p "$INSTALL_DIR"

# 4. استخراج حزمة النظام باستخدام الأدوات المتاحة في التوزيعة
echo -e "${YELLOW}[*] جاري استخراج وتثبيت حزمة WeakdowsOS...${NC}"

if command -v 7z &> /dev/null; then
    7z x "$ISO_PATH" -o"$INSTALL_DIR" -y > /dev/null
    echo -e "${GREEN}[✔] تم استخراج الحزمة بنجاح باستخدام 7z.${NC}"
elif command -v bsdtar &> /dev/null; then
    bsdtar -xf "$ISO_PATH" -C "$INSTALL_DIR"
    echo -e "${GREEN}[✔] تم استخراج الحزمة بنجاح باستخدام bsdtar.${NC}"
elif command -v xorriso &> /dev/null; then
    xorriso -osirrax on -indev "$ISO_PATH" -extract / "$INSTALL_DIR" &> /dev/null
    echo -e "${GREEN}[✔] تم استخراج الحزمة بنجاح باستخدام xorriso.${NC}"
else
    echo -e "${RED}[!] خطأ: لم يتم العثور على أداة استخراج (7z أو bsdtar أو xorriso).${NC}"
    echo -e "${YELLOW}يرجى تثبيت p7zip أو bsdtar عبر مدير الحزم الخاص بتوزيعتك.${NC}"
    exit 1
fi

# 5. ضبط الصلاحيات للملفات المستخرجة
chmod -R 755 "$INSTALL_DIR"

# 6. إنشاء اختصار في قائمة تطبيقات لينكس (Desktop Entry)
echo -e "${YELLOW}[*] جاري إضافة اختصار WeakdowsOS إلى قائمة التطبيقات...${NC}"
cat <<EOF > "$DESKTOP_ENTRY"
[Desktop Entry]
Type=Application
Name=WeakdowsOS
Comment=Weakdows OS Deployment Package
Exec=xdg-open $INSTALL_DIR
Icon=system-run
Terminal=false
Categories=System;
EOF

chmod +x "$DESKTOP_ENTRY"

echo -e "${GREEN}=====================================================${NC}"
echo -e "${GREEN}[✔] اكتمل تثبيت WeakdowsOS بنجاح على النظام!${NC}"
echo -e "${GREEN}[✔] مسار التثبيت: $INSTALL_DIR${NC}"
echo -e "${GREEN}[✔] يمكنك الآن الوصول للنظام من قائمة التطبيقات.${NC}"
echo -e "${GREEN}=====================================================${NC}"
