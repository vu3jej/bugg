from talon import Module

mod = Module()


mod.tag('operators', desc='Tag to enable operators')


mod.list('operator', desc='Programming language operators')


@mod.capture
def operator() -> str:
    """Returns a single operator"""
