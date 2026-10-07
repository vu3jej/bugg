# Basic navigation (macOS)
os: mac
-
next window:
    key(cmd-`)
previous window:
    key(cmd-shift-`)

hide {apps.running}:
    apps.focus(apps.running)
    sleep(0.5)
    app.hide()
hide [this] application:
    app.hide()

toggle [the] dock:
    key(alt-cmd-d)

next space:
    key(ctrl-right)
previous space:
    key(ctrl-left)

search spotlight for <phrase>:
    key(cmd-space)
    sleep(100ms)
    auto_insert(phrase)
    apps.focus("Spotlight")

open siri | show siri | launch siri | switch to siri:
    apps.launch("/System/Library/CoreServices/Siri.app")
