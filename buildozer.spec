[app]
title = مطابقة الأسماء والأقسام
package.name = matchnames
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas,xlsx
version = 0.1
requirements = python3,kivy,pandas,openpyxl,rapidfuzz,shutil
orientation = portrait
osx.kivy_version = 2.1.0
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = armeabi-v7a
android.gradle_dependencies = 'com.android.support:appcompat-v7:28.0.0'

[buildozer]
log_level = 2
warn_on_root = 1