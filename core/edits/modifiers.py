from collections.abc import Callable
from contextlib import suppress
from dataclasses import dataclass
from typing import Literal

from talon import Module, actions, settings

mod = Module()


@dataclass
class NavigationStep:
    kind: Literal[
        'left', 'right', 'wordLeft', 'wordRight', 'word', 'lineUp', 'lineDown'
    ]
    count: int


@dataclass
class EditModifier:
    kind: str
    count: int = 1


repeatable_modifier_callback_map: dict[str, Callable] = {
    'wordLeft': actions.edit.word_left,
    'wordRight': actions.edit.word_right,
    'word': actions.edit.word_right,
    'left': actions.edit.left,
    'right': actions.edit.right,
    'lineUp': actions.edit.up,
    'lineDown': actions.edit.down,
}


modifier_callback_map: dict[str, Callable] = {
    'document': actions.edit.select_all,
    'paragraph': actions.edit.select_paragraph,
    'word': actions.edit.extend_word_right,
    'wordLeft': actions.edit.extend_word_left,
    'wordRight': actions.edit.extend_word_right,
    'left': actions.edit.extend_left,
    'right': actions.edit.extend_right,
    'lineUp': actions.edit.extend_line_up,
    'lineDown': actions.edit.extend_line_down,
    'line': actions.edit.select_line,
    'lineStart': actions.edit.extend_line_start,
    'lineEnd': actions.edit.extend_line_end,
    'fileStart': actions.edit.extend_file_start,
    'fileEnd': actions.edit.extend_file_end,
    'selection': actions.edit.skip,
}


@mod.capture(rule='[<user.positive_small_integer>] {user.edit_repeatable_modifier}')
def navigation_step(m) -> NavigationStep:
    count = 1
    modifier = m.edit_repeatable_modifier

    with suppress(AttributeError):
        count = m.positive_small_integer

    return NavigationStep(kind=modifier, count=count)


@mod.capture(
    rule='{user.edit_modifier}|[<user.positive_small_integer>] {user.edit_repeatable_modifier}'
)
def edit_modifier(m) -> EditModifier:
    count = 1

    with suppress(AttributeError):
        count = m.positive_small_integer

    with suppress(AttributeError):
        kind = m.edit_modifier

    with suppress(AttributeError):
        kind = m.edit_repeatable_modifier

    return EditModifier(kind=kind, count=count)


throttled_navigation_steps = ['wordLeft', 'wordRight', 'word']


def _repeat(navigation_step_fn: Callable, count: int, throttle: bool) -> None:
    delay = settings.get('user.edit_word_selection_delay')

    for _ in range(count):
        navigation_step_fn()

        if throttle:
            actions.sleep(delay)


@mod.action_class
class Actions:
    def apply_edit_modifier(modifier: EditModifier) -> None:
        """Executes the callback function of the modifier for the specified count"""
        count = modifier.count
        callback = actions.user.get_edit_modifier_callback(modifier)

        for index in range(count):
            callback()

    def get_edit_modifier_callback(modifier: EditModifier):
        """Returns the callback function associated with the modifier"""
        try:
            return modifier_callback_map[modifier.kind]
        except KeyError:
            raise ValueError('Unknown edit modifier')

    def execute_navigation_steps(steps: list[NavigationStep]) -> None:
        """Applies a sequence of cursor movements"""
        throttle = False

        for step in steps:
            if step in throttled_navigation_steps:
                throttle = True

            navigation_step_fn = repeatable_modifier_callback_map[step.kind]

            _repeat(navigation_step_fn, step.count, throttle)
