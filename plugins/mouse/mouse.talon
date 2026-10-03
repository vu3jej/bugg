gaze calibrate:
  tracking.calibrate()

gaze control:
  tracking.control_toggle()

gaze zoom:
  tracking.control_zoom_toggle()

gaze debug:
  tracking.control_debug_toggle()

# Mouse
click and hold mouse | press and hold mouse:
    mouse_drag()
<modifiers> click and hold mouse:
    key("{modifiers}:down")
    mouse_drag()
    key("{modifiers}:up")
release mouse | release hold:
    mouse_release()
single click [mouse] | click mouse | press mouse | mouse click:
    mouse_click()
<modifiers> [mouse] click:
    key("{modifiers}:down")
    mouse_click()
    key("{modifiers}:up")
double click [mouse] | mouse double click:
    mouse_click()
    mouse_click()
<modifiers> [mouse] double click:
    key("{modifiers}:down")
    mouse_click()
    mouse_click()
    key("{modifiers}:up")
triple click [mouse] | mouse triple click:
    mouse_click()
    mouse_click()
    mouse_click()
<modifiers> [mouse] triple click:
    key("{modifiers}:down")
    mouse_click()
    mouse_click()
    mouse_click()
    key("{modifiers}:up")
long press:
    mouse_drag()
    sleep(1s)
    mouse_release()

move [the] cursor down [by] <number> pixels | move [the] mouse down [by] <number> pixels | move [the] cursor down [by] one pixel | move [the] mouse down [by] one pixel | move [the] cursor down [by] a pixel | move [the] mouse down [by] a pixel:
    number = number or 1
    x = mouse_x()
    y = mouse_y()
    mouse_move(x, y + number)
move [the] cursor [to the] left <number> pixels | move [the] mouse [to the] left [by] <number> pixels | move [the] cursor [to the] left [by] one pixel | move [the] mouse [to the] left [by] one pixel | move [the] cursor [to the] left [by] a pixel | move [the] mouse [to the] left [by] a pixel:
    number = number or 1
    y = mouse_y()
    x = mouse_x()
    mouse_move(x - number, y)
move [the] cursor [to the] right [by] <number> pixels | move [the] mouse [to the] right [by] <number> pixels | move [the] cursor [to the] right [by] one pixel | move [the] mouse [to the] right [by] one pixel | move [the] cursor [to the] right [by] a pixel | move [the] mouse [to the] right [by] a pixel:
    number = number or 1
    x = mouse_x()
    y = mouse_y()
    mouse_move(x + number, y)
move [the] cursor up [by] <number> pixels | move [the] mouse up [by] <number> pixels | move [the] cursor up [by] one pixel | move [the] mouse up [by] one pixel | move [the] cursor up [by] a pixel | move [the] mouse up [by] a pixel:
    number = number or 1
    x = mouse_x()
    y = mouse_y()
    mouse_move(x, y - number)

scroll [the] mouse down [<number_small> times]:
    number_small = number_small or 1
    mouse_scroll(120)
    repeat(number_small - 1)
scroll [the] mouse up [<number_small> times]:
    number_small = number_small or 1
    mouse_scroll(-120)
    repeat(number_small - 1)
scroll [the] mouse right [<number_small> times]:
    number_small = number_small or 1
    mouse_scroll(0, 120)
    repeat(number_small - 1)
scroll [the] mouse left [<number_small> times]:
    number_small = number_small or 1
    mouse_scroll(0, -120)
    repeat(number_small - 1)
