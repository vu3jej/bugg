from itertools import chain

from talon import Module

mod = Module()


mod.list('letter_key', desc='Phonetic alphabets')
mod.list('number_key', desc='Number keys')
mod.list('navigation_key', desc='Navigation keys')
mod.list('modifier_key', desc='Modifier keys')
mod.list('whitespace_key', desc='Whitespace keys')
mod.list('function_key', desc='Function keys')
mod.list('symbol_key', desc='Symbol keys')


@mod.capture(rule='{user.letter_key}')
def letter_key(m) -> str:
    """Returns a single alphabet key"""
    return m.letter_key


@mod.capture(rule='{user.number_key}')
def number_key(m) -> str:
    """Returns a single number key"""
    return m.number_key


@mod.capture(rule='{user.navigation_key}')
def navigation_key(m) -> str:
    """Returns a single navigation key"""
    return m.navigation_key


@mod.capture(rule='{user.whitespace_key}')
def whitespace_key(m) -> str:
    """Returns a single whitespace key"""
    return m.whitespace_key


@mod.capture(rule='{user.function_key}')
def function_key(m) -> str:
    """Returns a single function key"""
    return m.function_key


@mod.capture(rule='{user.symbol_key}')
def symbol_key(m) -> str:
    """Returns a single symbol key"""
    return m.symbol_key


@mod.capture(
    rule='(<user.letter_key>|<user.number_key>|<user.function_key>|<user.navigation_key>|<user.whitespace_key>|<user.symbol_key>)'
)
def nonmodifier_key(m) -> str:
    """Returns a single non-modifier key"""
    return str(m)


@mod.capture(rule='{user.letter_key}+')
def letter_keys(m) -> str:
    """Returns one or more letters"""
    return ''.join(m.letter_key_list)


@mod.capture(rule='{user.modifier_key}+ <user.nonmodifier_key>')
def shortcut(m) -> str:
    """Returns a keyboard shortcut"""
    return '-'.join(chain(m.modifier_key_list, (m.nonmodifier_key,)))
