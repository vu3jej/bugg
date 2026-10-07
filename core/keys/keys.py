from talon import Context

ctx = Context()


@ctx.capture(
    'key',
    rule='[<modifiers>] (<letter> | <digit_string> | <symbol> | <special_key>)',
)
def key(m) -> str:
    """Capture any letter, symbol, or special key, with optional modifiers first"""
    return '-'.join(m)


@ctx.capture('letter', rule='{letter}')
def letter(m) -> str:
    """Capture any alphabet letter"""
    return m.letter


@ctx.capture('modifiers', rule='{modifier}+')
def modifiers(m) -> str:
    """Capture any modifier keys"""
    return '-'.join(m.modifier_list)


@ctx.capture('special_key', rule='{special_key}')
def special_key(m) -> str:
    """Capture any special key"""
    return m.special_key


@ctx.capture('symbol', rule='{symbol}')
def symbol(m) -> str:
    """Capture any printable symbol"""
    return m.symbol
