from typing import Literal

from talon import Module, actions

mod = Module()

TextDirection = Literal["left", "right", "both"]


@mod.capture(rule="(left | right | both)")
def text_direction_input(m) -> TextDirection:
    return str(m)


@mod.action_class
class TextActions:
    def pad_text(text: str, direction: TextDirection, by: str = " ") -> None:
        """"""
        match direction:
            case "left":
                modified_text = by + text
            case "right":
                modified_text = text + by
            case "both":
                modified_text = by + text + by
            case _:
                modified_text = text

        actions.insert(modified_text)
