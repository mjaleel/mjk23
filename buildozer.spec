[app]
# اسم التطبيق
title = App2

# اسم البايثون الأساسي
package.name = app2
package.domain = org.example

# مجلد ملفات المصدر (الكود)
source.dir = .

# ملف البايثون الرئيسي
source.main = app2.py

# إصدار البايثون المطلوب
requirements = python3,kivy,pandas,openpyxl,rapidfuzz,cryptography,pyperclip

# نسخة SDK أندرويد
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# نوع الحزمة
android.arch = armeabi-v7a

# وضع العرض
fullscreen = 0

# أي إعدادات أخرى حسب الحاجة
