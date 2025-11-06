from collections.abc import Callable
from typing import Literal, Protocol


class Formatter(Protocol):
    def format(self, text: str) -> str: ...


class SimpleFormatter:
    def __init__(self, formatter_func: Callable[[str], str]):
        self.formatter_func = formatter_func

    def format(self, text: str) -> str:
        return self.formatter_func(text)


def create_formatter(
    kind: Literal["simple", "identifier"], formatter_fn: Callable[[str], str] | None
) -> Formatter:
    match kind:
        case "simple":
            return SimpleFormatter(formatter_fn)


class Lower:
    def __call__(self, text: str) -> str:
        return text.lower()


class Upper:
    def __call__(self, text: str) -> str:
        return text.upper()


class Capitalize:
    def __call__(self, text: str) -> str:
        return text.capitalize()


formatters = {
    "ALL_CAPS": create_formatter("simple", Upper()),
    "ALL_LOWERCASE": create_formatter("simple", Lower()),
}
