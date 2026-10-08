# Mouse grid targets
tag: labels.grid_active
-

choose <labels.target>:
    labels.select(labels.target)

<labels.target>:
    labels.select(labels.target)

double click [at] <labels.target>:
    labels.mouse_move(labels.target)
    mouse_click()
    mouse_click()
    labels.hide()

<modifiers> double click [at] <labels.target>:
    key("{modifiers}:down")
    labels.mouse_move(labels.target)
    mouse_click()
    mouse_click()
    labels.hide()
    key("{modifiers}:up")

drag [from] <labels.target> to <labels.target>:
    labels.mouse_move(labels.target_1)
    sleep(200ms)
    mouse_drag()
    sleep(200ms)
    labels.mouse_move(labels.target_2)
    sleep(200ms)
    mouse_release()
    labels.hide()

drop [at] <labels.target> | release mouse [at] <labels.target> | release hold [at] <labels.target> | end drag [at] <labels.target>:
    labels.mouse_move(labels.target)
    sleep(200ms)
    mouse_release()
    labels.hide()

long press [at] <labels.target>:
    labels.mouse_move(labels.target)
    mouse_drag()
    sleep(1)
    mouse_release()
    labels.hide()

move mouse to <labels.target> | move cursor to <labels.target>:
    labels.mouse_move(labels.target)
    labels.hide()

click and hold [at] <labels.target> | press and hold <labels.target>:
    labels.mouse_move(labels.target)
    mouse_drag()
    labels.hide()

<modifiers> click and hold [at] <labels.target>:
    key("{modifiers}:down")
    labels.mouse_move(labels.target)
    mouse_drag()
    labels.hide()
    key("{modifiers}:up")

show menu for <labels.target>:
    labels.mouse_move(labels.target)
    mouse_click(1)
    labels.hide()

click [at] <labels.target> | press <labels.target> | tap <labels.target>:
    labels.mouse_move(labels.target)
    mouse_click()
    labels.hide()

<modifiers> click [at] <labels.target>:
    key("{modifiers}:down")
    labels.mouse_move(labels.target)
    mouse_click()
    labels.hide()
    key("{modifiers}:up")

start drag [at] <labels.target>:
    labels.mouse_move(labels.target)
    sleep(200ms)
    mouse_drag()

triple click [at] <labels.target>:
    labels.mouse_move(labels.target)
    mouse_click()
    mouse_click()
    mouse_click()
    labels.hide()

<modifiers> triple click [at] <labels.target>:
    key("{modifiers}:down")
    labels.mouse_move(labels.target)
    mouse_click()
    mouse_click()
    mouse_click()
    labels.hide()
    key("{modifiers}:up")
