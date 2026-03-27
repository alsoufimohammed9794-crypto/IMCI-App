[app]
title = IMCI Yemen
package.name = imciyemen
package.domain = dr.mohamed
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,cython==0.29.33

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

# إعدادات الأندرويد الصحيحة لتجاوز الخطأ الأخير
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
