[app]
# اسم التطبيق الظاهر
title = App2

# اسم الحزمة (package name) - يفضل أن يكون بدون مسافات وحروف صغيرة
package.name = app2

# نطاق الحزمة (عادة تستخدم دومينك معكوسًا أو org.example)
package.domain = org.example

# مجلد المصدر (الدليل الرئيسي للكود)
source.dir = .

# الملف الرئيسي الذي يبدأ التطبيق منه
source.main = app2.py

# إصدار التطبيق (ضروري)
version = 1.0.0

# المتطلبات - حزم بايثون اللازمة (حسب كودك)
requirements = python3,kivy,pandas,openpyxl,rapidfuzz,cryptography,pyperclip

# إعدادات أندرويد
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = armeabi-v7a

# خيارات الواجهة
fullscreen = 0
orientation = portrait

# خيارات أخرى
android.permissions = INTERNET

# تخطي التفعيل حسب طلبك، لذا لا توجد إعدادات تفعيل
