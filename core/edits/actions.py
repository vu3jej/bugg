from collections.abc import Callable
from dataclasses import dataclass
from typing import Union

from talon import Module, actions

mod = Module()


mod.list('delimiter_pair', desc='Delimiter pairs')


@dataclass
class EditSimpleAction:
    kind: str


@dataclass
class EditInsertAction:
    kind = 'insert'
    text: str


@dataclass
class EditWrapAction:
    kind = 'wrapWithPairedDelimiter'
    pair: list[str]


@dataclass
class EditFormatAction:
    kind = 'applyFormatter'
    formatters: list[str]


EditAction = Union[EditSimpleAction, EditInsertAction, EditWrapAction, EditFormatAction]


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


@mod.capture(rule='{user.edit_action}')
def edit_simple_action(m) -> EditSimpleAction:
    return EditSimpleAction(str(m))


@mod.capture(rule='<user.delimiter_pair> wrap')
def edit_wrap_action(m) -> EditWrapAction:
    return EditWrapAction(pair=m.delimiter_pair)


@mod.capture(rule='<user.formatters> format')
def edit_format_action(m) -> EditFormatAction:
    return EditFormatAction(formatters=m.formatters)


@mod.capture(
    rule='<user.edit_simple_action>|<user.edit_wrap_action>|<user.edit_format_action>'
)
def edit_action(m) -> EditAction:
    return m[0]


@mod.action_class
class Actions:
    def insert_delimiter_pair(pair: list[str]) -> None:
        """Insert a delimiter pair"""
        left, right = pair
        actions.insert(f'{left}{right}')

    def surround_string(key: str, string: str) -> str:
        """Returns a string wrapped with delimiter pair"""
        left, right = delimiter_pairs[key]
        return f'{left}{string}{right}'

    def surround_selection(pair: list[str]) -> None:
        """Wrap selection with the given delimiter pair"""
        left, right = pair
        selection = actions.edit.selected_text()
        actions.insert(f'{left}{selection}{right}')

    def apply_edit(edit_action: EditAction) -> None:
        """Executes the specified edit action"""
        match edit_action:
            case EditSimpleAction(kind=k):
                callback = actions.user.get_simple_edit_action_callback(k)
                if callback:
                    callback()

            case EditInsertAction(text=t):
                actions.insert(t)

            case EditWrapAction(pair=p):
                actions.user.surround_selection(p)

            case EditFormatAction(formatters=f):
                actions.user.reformat_selection(f)

            case _:
                raise ValueError('Unsupported action')

    def get_simple_edit_action_callback(identifier: str) -> Callable | None:
        """Returns the callback associated with the simple action identifier"""
        return simple_action_callback_map.get(identifier)
