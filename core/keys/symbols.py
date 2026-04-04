from dataclasses import dataclass

from talon import Context

ctx = Context()


@dataclass
class Symbol:
    character: str
    # shared_phrases: list[str] = field(default_factory=list)
    # command_phrases: list[str] = field(default_factory=list)
    commands: list[str]


currencies = [
    Symbol('$', ['dollar sign']),
    # Symbol('¢', ['cent sign']),
    Symbol('£', ['pound sign', 'pound sterling sign']),
    Symbol('¥', ['yen sign']),
    Symbol('₦', ['naira sign']),
    Symbol('₩', ['won sign']),
    Symbol('€', ['euro sign']),
    Symbol('₹', ['indian rupee sign']),
    # Symbol('turkish lira sign', ['₺']),
    Symbol('₺', ['turkish lira sign']),
    Symbol('₽', ['ruble sign']),
    Symbol('₿', ['bitcoin sign']),
]


symbols = [
    Symbol(':', ['colon']),
    Symbol(',', ['comma', 'coma']),
    Symbol(';', ['semicolon']),
    Symbol('-', ['hyphen', 'minus sign']),
    Symbol('–', ['dash']),
    Symbol('.', ['period', 'point', 'dot', 'full stop']),
    # Symbol('...', ['ellipsis']),
    Symbol('!', ['exclamation mark']),
    Symbol('?', ['question mark']),
    Symbol('[', ['open square bracket', 'left square bracket']),
    Symbol(']', ['close square bracket', 'right square bracket']),
    Symbol('(', ['open parenthesis', 'left parenthesis']),
    Symbol(')', ['close parenthesis', 'right parenthesis']),
    Symbol('{', ['open curly bracket', 'left curly bracket']),
    Symbol('}', ['close curly bracket', 'right curly bracket']),
    Symbol('<', ['open angle bracket', 'less than sign']),
    Symbol('>', ['close angle bracket', 'greater than sign']),
    Symbol('&', ['ampersand']),
    Symbol('*', ['asterisk']),
    Symbol('@', ['at sign']),
    Symbol('\\', ['backslash']),
    Symbol('/', ['forward slash']),
    Symbol('^', ['caret']),
    Symbol('・', ['centre dot']),
    Symbol('●', ['large centre dot']),
    Symbol('°', ['degree sign']),
    Symbol('#', ['hashtag sign']),
    Symbol('%', ['per cent sign']),
    Symbol('_', ['underscore']),
    Symbol('|', ['vertical bar', 'pipe']),
    Symbol('=', ['equal sign']),
    Symbol('~', ['tilde']),
    Symbol('`', ['back tick', 'back quote', 'grave', 'grave accent']),
    Symbol('+', ['plus sign']),
    Symbol('x', ['multiplication sign']),
    Symbol("'", ['apostrophe', 'single quote']),
    Symbol('"', ['double quote', 'dub quote']),
]


symbols.extend(currencies)

symbol_map = {}


for symbol in symbols:
    for cmd in symbol.commands:
        symbol_map[cmd] = symbol.character


ctx.lists['user.symbol_key'] = symbol_map
