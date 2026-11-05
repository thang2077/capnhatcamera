[app]
title = Camera AI Phone
package.name = cameraaiphone
package.domain = org.test
source.dir = .
source.filename = main_phone.py
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.archs = arm64-v8a
android.ndk = 25b
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
