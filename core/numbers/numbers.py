"""Implement Talon's documented built-in numeric captures."""

from collections.abc import Iterable
from dataclasses import dataclass
from decimal import Decimal

from talon import Context

ctx = Context()


@dataclass(frozen=True)
class NumberGrouping:
    digit: list[str]
    number_small: list[str]
    number_meta: list[str]
    number_scale: list[str]


def parse_number(values: Iterable[str], grouping: NumberGrouping) -> int:
    """Combine numeric values in spoken order using their capture lists."""
    tokens = [value for value in values if value not in grouping.number_meta]

    scales = [
        (int(Decimal(value)), index)
        for index, value in enumerate(tokens)
        if value in grouping.number_scale
    ]

    if scales:
        scale, index = max(scales)

        if index > 0:
            # "two hundred": index is 1, so parse "two" as coefficient 2.
            coefficient = parse_number(tokens[:index], grouping)
        else:
            # "hundred" or "a hundred" (after filtering metadata): index is 0.
            # An absent prefix implies 1; parsing an empty prefix would give 0.
            coefficient = 1

        return coefficient * scale + parse_number(tokens[index + 1 :], grouping)

    number = previous = 0

    for token in tokens:
        value = int(token)

        # "forty two" may be one entry ("forty two" -> "42" in number_small),
        # or two: "forty" -> "40" in number_small, then "two" -> "2" in digit.
        # Add the split entries to get 42 rather than concatenate them into 402.
        if 20 <= previous <= 90 and previous % 10 == 0 and 0 < value < 10:
            number += value
        else:
            # Concatenate number chunks rather than sum them: "twenty twenty" -> 2020.
            # At the second token:
            # number = 20, token = "20", value = 20, len(token) = 2
            # 20 * 10 ** 2 + 20 = 2020
            number = number * 10 ** len(token) + value

        previous = value

    return number


@ctx.capture('digit_string', rule='{digit}+')
def digit_string(m) -> str:
    """Capture a series of digits, as a string."""
    return ''.join(m.digit_list)


@ctx.capture('digits', rule='<digit_string>')
def digits(m) -> int:
    """Capture a series of digits as a single integer."""
    return int(m.digit_string)


@ctx.capture(
    'number_string',
    rule='({digit} | {number_small} | {number_meta} | {number_scale})+',
)
def number_string(m) -> str:
    """Capture a naturally-spoken positive integer of any size, as a string."""
    grouping = NumberGrouping(
        digit=m.digit_list,
        number_small=m.number_small_list,
        number_meta=m.number_meta_list,
        number_scale=m.number_scale_list,
    )

    return str(parse_number(m, grouping))


@ctx.capture('number', rule='<number_string>')
def number(m) -> int:
    """Capture a naturally-spoken positive integer of any size."""
    return int(m.number_string)


@ctx.capture('number_signed', rule='[{number_sign}] <number>')
def number_signed(m) -> int:
    """Capture a naturally-spoken integer of any size."""
    return -m.number if hasattr(m, 'number_sign') else m.number


@ctx.capture('number_small', rule='{digit} | {number_small}')
def number_small(m) -> int:
    """Capture a naturally-spoken integer under 100."""
    return int(m[0])
