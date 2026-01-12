from talon import Module, actions

mod = Module()


mod.list('delimiter_pair', desc='Delimiter pairs')


delimiter_pairs = {
    'curlyBrackets': ['{', '}'],
    'angleBrackets': ['<', '>'],
    'parentheses': ['(', ')'],
    'squareBrackets': ['[', ']'],
    'doubleQuotes': ['"', '"'],
    'singleQuotes': ["'", "'"],
    'backtickQuotes': ['`', '`'],
    'whitespace': [' ', ' '],
    'escapedParentheses': ['\\(', '\\)'],
    'escapedSquareBrackets': ['\\[', '\\]'],
    'escapedDoubleQuotes': ['\\"', '\\"'],
    'escapedSingleQuotes': ["\\'", "\\'"],
}


simple_action_callback_map = {
    'select': actions.skip,
    'before': actions.edit.left,
    'after': actions.edit.right,
    'copyToClipboard': actions.edit.copy,
    'cutToClipboard': actions.edit.cut,
    'pasteFromClipboard': actions.edit.paste,
    'delete': actions.edit.delete,
    'insertLineAbove': actions.edit.insert_line_up,
    'insertLineBelow': actions.edit.insert_line_down,
    'insertCopyAfter': actions.edit.selection_clone,
}


@mod.capture(rule='{user.delimiter_pair}')
def delimiter_pair(m) -> list[str]:
    key = m.delimiter_pair
    return delimiter_pairs[key]


@mod.action_class
class Actions:
    def insert_delimiter_pair(pair: list[str]) -> None:
        """Insert a delimiter pair"""
        left, right = pair
        actions.insert(f'{left}{right}')

    def surround_string(key: str, s: str) -> str:
        """Returns a string wrapped with delimiter pair"""
        left, right = delimiter_pairs[key]
        return f'{left}{s}{right}'
