[app]
title = Chess Assistant AI
package.name = chessassistantai
package.domain = org.sultan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,opencv-python,numpy,python-chess
android.permissions = SYSTEM_ALERT_WINDOW, FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.private_storage = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
