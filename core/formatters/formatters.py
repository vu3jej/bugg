import re
from collections import deque
from functools import partial

from talon import Module, actions, app

mod = Module()


mod.list('code_formatter', desc='Identifier formatters')


def stitcher(sep: str):
    return partial(str.join, sep)


class SpecialCaseFormatter:
    """pun intended"""

    def to_camel(self, tokens: list[str]) -> str:
        tokens = deque(tokens)
        first = tokens.popleft()
        return first + ''.join(t.capitalize() for t in tokens)

    def to_pascal(self, tokens: list[str]) -> str:
        return ''.join(t.capitalize() for t in tokens)

    def to_screaming_snake(self, tokens: list[str]) -> str:
        return '_'.join(t.upper() for t in tokens)

    def to_slasher(self, tokens: list[str]) -> str:
        return '/' + '/'.join(t for t in tokens)


formatter = SpecialCaseFormatter()


formatter_map = {
    'camelCase': formatter.to_camel,
    'snakeCase': stitcher('_'),
    'kebabCase': stitcher('-'),
    'screamingSnakeCase': formatter.to_screaming_snake,
    'pascalCase': formatter.to_pascal,
    'unseparated': stitcher(''),
    'doubleUnderscoreSeparated': stitcher('__'),
    'dotSeparated': stitcher('.'),
    'doubleColonSeparated': stitcher('::'),
    'slashSeparated': stitcher('/'),
    'leadingSlashSeparated': formatter.to_slasher,
    'singleQuoted': partial(actions.user.surround_string, 'singleQuotes'),
    'doubleQuoted': partial(actions.user.surround_string, 'doubleQuotes'),
    'allCaps': partial(str.upper),
}


string_formatters = ['singleQuoted', 'doubleQuoted', 'allCaps']


@mod.capture(rule='{user.code_formatter}+')
def code_formatters(m) -> list[str]:
    """Returns a list of code formatters"""
    return m.code_formatter_list


@mod.capture(rule='<user.code_formatters> <user.text>')
def format_identifier(m) -> str:
    """Formats identifier and returns a string"""
    return format_phrase(m.text, m.code_formatters)


def string_to_tokens(string):
    return re.findall(r'[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|[0-9]+', string)


def format_phrase(text, formatters: list[str]) -> str:
    for formatter_name in reversed(formatters):
        formatter = formatter_map[formatter_name]

        if formatter_name in string_formatters:
            arg = text
        else:
            arg = string_to_tokens(text)

        text = formatter(arg)

    return text


@mod.action_class
class Actions:
    def get_formatted_text(text: str, formatters: list[str] | str) -> str:
        """Get formatted text"""
        if isinstance(formatters, str):
            formatters = [formatters]
        return format_phrase(text, formatters)

    def insert_formatted_text(text: str, formatters: list[str] | str) -> None:
        """Insert formatted text"""
        # if isinstance(formatters, str):
        #     formatters = [formatters]
        formatted_text = actions.user.get_formatted_text(text, formatters)
        actions.insert(formatted_text)

    def reformat_selection(formatters: list[str]) -> None:
        """Reformats current selection with the given formatters"""
        selection = actions.edit.selected_text()
        if not selection:
            app.notify('No selection')
            return

        actions.edit.delete()
        reformatted_text = actions.user.get_formatted_text(selection, formatters)
        actions.insert(reformatted_text)
