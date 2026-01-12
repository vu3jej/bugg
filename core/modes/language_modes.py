from types import SimpleNamespace

from talon import Context, Module, app

mod = Module()
mod.tag('language_override', desc='Name of programming language mode')

ctx = Context()

ctx_language_override = Context()
ctx_language_override.matches = 'tag: user.language_override'


overrides = SimpleNamespace(language=None)
language_extensions = {'python': '.py'}


@ctx_language_override.action('code.language')
def get_overridden_language_mode():
    return overrides.language


@mod.action_class
class Actions:
    def set_language_mode(language: str):
        """"""
        overrides.language = language

        ctx.tags = []
        ctx.tags = ['user.language_override']

    def unset_language_mode():
        """"""

        overrides.language = None
        ctx.tags = []

    def show_overridden_language_mode():
        """"""
        if overrides.language is None:
            app.notify('No override (auto mode)')
        else:
            app.notify(f'[LANGUAGE MODE OVERRIDE] {overrides.language}')
