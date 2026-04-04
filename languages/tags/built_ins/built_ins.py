from talon import Module

mod = Module()

mod.tag('built_ins', desc='Tag for enabling the built-in functions')
# mod.list('built_in', desc='Built-in functions')
mod.list('built_in_func', desc='Built-in functions')
mod.list('string_method', desc='String methods')

#
# @mod.capture(rule='{user.built_in}')
# def built_in(m) -> str:
#     return f'{m.built_in}()'


@mod.capture(rule='{user.built_in_func}')
def built_in(m) -> str:
    return f'{m.built_in_func}()'
