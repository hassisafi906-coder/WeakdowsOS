// =====================================================================
//  Weakdows OS - Smart System Detector & Interactive Audio Engine
// =====================================================================

document.addEventListener("DOMContentLoaded", () => {
    
    // --- 1. نظام التعرف الذكي على نظام التشغيل وتوجيه التحميل ---
    const autoDetectBtn = document.getElementById("auto-detect-btn");
    const detectionBox = document.getElementById("detection-result");
    const detectionText = document.getElementById("detection-text");
    const quickDownloadBtn = document.getElementById("quick-download-btn");

    if (autoDetectBtn) {
        autoDetectBtn.addEventListener("click", () => {
            const userAgent = navigator.userAgent || navigator.vendor || window.opera;
            let recommended = "Weak11 (النسخة الكمومية الفائقة)";
            let editionCode = "weak11";

            // فحص مبدئي لبيئة المستخدم
            if (/Windows NT 5.1|Windows NT 5.2/i.test(userAgent)) {
                recommended = "WeakXP (الخفة المطلقة لجهازك القديم)";
                editionCode = "xp";
            } else if (/Windows NT 6.1/i.test(userAgent)) {
                recommended = "Weak7 (زجاج Aero المائي الأنيق)";
                editionCode = "weak7";
            } else if (/Windows NT 10.0/i.test(userAgent)) {
                recommended = "Weak10 (السايبربانك العصري السريع)";
                editionCode = "weak10";
            } else if (/Macintosh|MacIntel|MacPPC|Mac68K/i.test(userAgent)) {
                recommended = "Weak11 (مع حزمة التثبيت المتوافقة مع أجهزة ماك)";
                editionCode = "weak11";
            }

            // إظهار النتيجة في صندوق التحليل
            detectionBox.classList.remove("hidden");
            detectionText.innerHTML = `✨ بناءً على جهازك الحالي، نوصي بتحميل: <strong style="color: var(--accent-cyan);">${recommended}</strong>`;

            console.log(`[SmartDetector] Recommended edition mapped: ${editionCode}`);
        });
    }

    // زر التحميل السريع من شريط الملاحة
    if (quickDownloadBtn) {
        quickDownloadBtn.addEventListener("click", () => {
            alert("[Weakdows ISO Builder]\nجاري توجيهك إلى مركز التثبيت المباشر وحزم الـ ISO الخفيفة...");
        });
    }

    // --- 2. أزرار تحميل النسخ الفردية (بطاقات الإصدارات) ---
    const editionDownloadButtons = document.querySelectorAll(".btn-card-download");
    editionDownloadButtons.forEach(button => {
        button.addEventListener("click", (e) => {
            const edition = e.target.getAttribute("data-edition").toUpperCase();
            alert(`[Weakdows Downloader]\nجاري تحضير حزمة التثبيت الخاصة بإصدار: [ ${edition} ]...\nسيتم بدء التحميل فوراً.`);
        });
    });

    // --- 3. محرك المعاينة الصوتية التفاعلي ---
    const soundButtons = document.querySelectorAll(".btn-sound");
    const audioStatusText = document.getElementById("audio-status");
    const editionSelect = document.getElementById("audio-edition-select");
    const profileSelect = document.getElementById("audio-profile-select");

    soundButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const eventName = btn.getAttribute("data-event");
            const currentEdition = editionSelect.value.toUpperCase();
            const currentProfile = profileSelect.value.toUpperCase();

            // محاكاة تشغيل الصوت وإظهار التنبيه التفاعلي
            audioStatusText.innerHTML = `🎵 جاري تشغيل صوت [ <span style="color: var(--accent-cyan);">${eventName}</span> ] لـ <strong style="color: #d8b4fe;">${currentEdition}</strong> (النمط: ${currentProfile})`;

            // تأثير نبضي مرئي خفيف على نص الحالة
            audioStatusText.style.transform = "scale(1.02)";
            setTimeout(() => {
                audioStatusText.style.transform = "scale(1)";
            }, 200);

            console.log(`[AudioEngine] Playing -> Edition: ${currentEdition} | Profile: ${currentProfile} | Event: ${eventName}`);
        });
    });

});
