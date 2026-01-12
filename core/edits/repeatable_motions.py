from collections.abc import Callable
from contextlib import suppress
from dataclasses import dataclass
from typing import Literal

from talon import Module, actions, settings

mod = Module()


@dataclass
class RepeatableMotion:
    kind: Literal[
        'left', 'right', 'wordLeft', 'wordRight', 'word', 'lineUp', 'lineDown'
    ]
    count: int


repeatable_motions: dict[str, tuple[Callable, bool]] = {
    'wordLeft': (actions.edit.word_left, True),
    'wordRight': (actions.edit.word_right, True),
    'word': (actions.edit.word_right, True),
    'left': (actions.edit.left, False),
    'right': (actions.edit.right, False),
    'lineUp': (actions.edit.up, False),
    'lineDown': (actions.edit.down, False),
}


@mod.capture(rule='[number_between_1_and_100] {user.edit_repeatable_motion}')
def repeatable_motion(m) -> RepeatableMotion:
    count = 1
    motion_type = m.edit_repeatable_motion

    with suppress(AttributeError):
        count = m.number_between_1_and_100

    return RepeatableMotion(kind=motion_type, count=count)


@mod.action_class
class Actions:
    def execute_motions(motions: list[RepeatableMotion]):
        """Execute motions"""
        for motion in motions:
            action, throttle = repeatable_motions[motion.kind]
            repeat_motion(action, motion.count, throttle)


def repeat_motion(action: Callable, count, throttle):
    delay = settings.get('user.edit_word_selection_delay')
    delay_ms = f'{delay}ms'

    for index in range(count):
        action()

        if throttle:
            actions.sleep(delay_ms)
