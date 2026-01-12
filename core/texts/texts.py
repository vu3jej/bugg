from talon import Module

mod = Module()


@mod.capture(rule='<phrase>')
def text(m) -> str:
    """Returns spoken words as a string"""
    return str(m)
