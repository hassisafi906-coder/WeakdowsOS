# =====================================================================
#  Weakdows OS - Central CMake Build Configuration
# =====================================================================

cmake_minimum_required(VERSION 3.15)
project(WeakdowsOS VERSION 1.0.0 LANGUAGES C CXX)

# تعيين معيار C++
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# إضافة المجلدات والكونات الأساسية للنظام
add_subdirectory(core/xforce)
add_subdirectory(core/bypass)
add_subdirectory(apps/weak_store)

# رسالة تأكيد إعداد البناء
message(STATUS "[Weakdows CMake] Central build configuration loaded successfully.")
