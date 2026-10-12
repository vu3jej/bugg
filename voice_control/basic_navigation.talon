# Basic navigation
next app | next application:
    app.next()
previous app | previous application:
    app.previous()
show app windows | show application windows:
    app.windows_show()

close [this] window:
    app.window_close()

find the text <phrase>:
    text = "{phrase}"
    edit.find(text)
find next:
    edit.find_next()

toggle [the] desktop:
    app.desktop_toggle()

close menu | cancel menu:
    key(escape)

[open] mission control:
    app.desktop_show_windows()

go to previous field | previous field:
    key(shift-tab)
go to next field | next field | tab key:
    key(tab)

minimize [this] window:
    app.window_minimize()

[make] new item | new window:
    app.window_open()

open [a] document:
    edit.open()

quit {apps.running}:
    apps.focus(apps.running)
    app.quit()
quit [this] application:
    app.quit()

repeat [that] [again] <number_small> times | repeat [that] [again] <number_small> | repeat that [one time]:
    core.repeat_command(number_small or 1)
save [this] document:
    edit.save()

open {apps.list} | launch {apps.list}:
    apps.launch(apps.list)

switch to {apps.running} | focus {apps.running}:
    apps.focus(apps.running)

stop listening [to me] | go to sleep:
    speech.disable()

enter full screen:
    app.window_fullscreen(true)
exit full screen:
    app.window_fullscreen(false)
zoom window | maximize window:
    app.window_maximize()

scroll [page] down:
    edit.page_down()
scroll [page] up:
    edit.page_up()
scroll to [the] bottom | scroll to [the] end:
    edit.file_end()
scroll to [the] top | scroll to [the] beginning:
    edit.file_start()
