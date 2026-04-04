from talon import Context, actions, clip

ctx = Context()

ctx.matches = 'os: mac'


@ctx.action_class('edit')
class Actions:
    def copy():
        actions.key('cmd-c')

    def cut():
        actions.key('cmd-x')

    def delete():
        actions.key('backspace')

    def delete_line():
        actions.edit.select_line()
        actions.edit.delete()

    def delete_word():
        actions.edit.select_word()
        actions.edit.delete()

    def down():
        actions.key('down')

    def up():
        actions.key('up')

    def left():
        actions.key('left')

    def right():
        actions.key('right')

    def extend_file_start():
        actions.key('shift-cmd-up')

    def extend_file_end():
        actions.key('shift-cmd-down')

    # def extend_line_left():
    #     actions.key('shift-cmd-left')
    #
    # def extend_line_right():
    #     actions.key('shift-cmd-right')
    def extend_line_start():
        actions.key('shift-cmd-left')

    def extend_line_end():
        actions.key('shift-cmd-right')

    def extend_line_up():
        actions.key('shift-up')

    def extend_line_down():
        actions.key('shift-down')

    def extend_up():
        actions.key('shift-up')

    def extend_down():
        actions.key('shift-down')

    def extend_right():
        actions.key('shift-right')

    def extend_left():
        actions.key('shift-left')

    def extend_word_left():
        actions.key('shift-alt-left')

    def extend_word_right():
        actions.key('shift-alt-right')

    def word_left():
        actions.key('alt-left')

    def word_right():
        actions.key('alt-right')

    def undo():
        actions.key('cmd-z')

    def redo():
        actions.key('shift-cmd-z')

    def save():
        actions.key('cmd-s')

    def file_start():
        actions.key('cmd-up')

    def file_end():
        actions.key('cmd-down')

    def line_start():
        actions.key('cmd-left')

    def line_end():
        actions.key('cmd-right')

    def line_insert_up():
        actions.key('cmd-left enter up')

    def line_up():
        actions.key('up cmd-left')

    def line_down():
        actions.key('down cmd-left')

    def page_up():
        actions.key('pageup')

    def page_down():
        actions.key('pagedown')

    def extend_page_up():
        actions.key('shift-cmd-pageup')

    def extend_page_down():
        actions.key('shift-cmd-pagedown')

    def find(text: str = None):
        if text is not None:
            clip.set_text(text, mode='find')
        actions.key('cmd-f')

    def find_next():
        actions.key('cmd-g')

    def find_previous():
        actions.key('shift-cmd-g')

    def select_all():
        actions.key('cmd-a')

    def select_line(n: int = None):
        if n is not None:
            actions.edit.jump_line(n)
        actions.key('cmd-right shift-cmd-left')

    def select_none():
        actions.key('right')

    def paste():
        actions.key('cmd-v')

    def paste_match_style():
        actions.key('alt-shift-cmd-v')

    def print():
        actions.key('cmd-p')

    def zoom_in():
        actions.key('cmd-=')

    def zoom_out():
        actions.key('cmd--')

    def zoom_reset():
        actions.key('cmd-0')
