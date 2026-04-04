from talon import Context, Module, actions

mod = Module()
ctx = Context()

# mod.apps.intellij = 'os:mac and app.bundle:com.jetbrains.pycharm'

mod.apps.intellij = """
os:mac
and app.bundle:com.jetbrains.pycharm
"""

ctx.matches = 'app:intellij'


@ctx.action_class('edit')
class EditActions:
    def indent_more():
        actions.key('tab')

    def indent_less():
        actions.key('shift-tab')

    def jump_line(n):
        actions.key('cmd-l')
        actions.sleep('100ms')
        actions.insert(n)
        actions.key('enter')

    def line_clone():
        actions.key('cmd-d')

    def selection_clone():
        actions.key('cmd-d')

    #
    # def complete():
    #     actions.key('ctrl-space')


@ctx.action_class('code')
class CodeActions:
    def toggle_comment():
        actions.key('cmd-/')

    def complete():
        actions.key('ctrl-space')
