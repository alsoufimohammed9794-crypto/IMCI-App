[app]
title = IMCI Yemen
package.name = imciyemen
package.domain = dr.mohamed
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

# إعدادات الأندرويد لضمان الاستقرار
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
