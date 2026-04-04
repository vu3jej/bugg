import operator
from itertools import accumulate, chain, count, repeat

from talon import Context, Module

mod = Module()
ctx = Context()


digits: list[str] = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]


teens: list[str] = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]


tens: list[str] = [
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]


scales: list[str] = [
    'thousand',
    'million',
    'billion',
    'trillion',
    'quadrillion',
    'quintillion',
    'sextillion',
    'septillion',
]


named_numbers: dict[str, int] = dict(
    chain(
        zip(digits, count()),
        zip(teens, count(10)),
        zip(tens, count(10, 10)),
        [('hundred', 100)],
        zip(scales, accumulate(repeat(1000), operator.mul)),
    )
)


repeaters: dict[str, int] = dict(
    zip(['single', 'double', 'triple', 'quadruple', 'quintuple'], count(1))
)


homophones: dict[str, str] = {
    'oh': 'zero',
    'naught': 'zero',
    'won': 'one',
    'to': 'two',
    'too': 'two',
    'ate': 'eight',
}


words_to_ignore: list[str] = ['and']


digit_word_list = digits + list(repeaters.keys())


number_rule = (
    '('
    + '|'.join(
        chain(digits, tens, teens, scales, repeaters, homophones, words_to_ignore)
    )
    + ')+'
)


def normalize_tokens(spoken_words, homophones, ignored_words):
    for word in spoken_words:
        token = homophones.get(word, word)
        if token not in ignored_words:
            yield token


def to_digits(tokens, number_map, digits, repeaters):
    iterator = iter(tokens)

    for token in iterator:
        if token in repeaters:
            times = repeaters[token]

            try:
                following_token = next(iterator)
            except StopIteration:
                return

            if following_token in digits:
                value = number_map[following_token]
                yield from repeat(value, times)
            else:
                return
        elif token in digits:
            yield number_map[token]


def numericize(spoken_words):
    def from_number_vocalization(tokens, number_map):
        total = 0
        subtotal = 0

        for token in tokens:
            if token not in number_map:
                continue

            value = number_map[token]

            if token == 'hundred':
                if subtotal != 0:
                    subtotal = subtotal * value
                else:
                    subtotal += value

            elif token in scales:
                if subtotal != 0:
                    total += subtotal * value
                else:
                    total += value

                subtotal = 0

            else:
                subtotal += value

        return total + subtotal

    def from_digit_vocalization(tokens, number_map, digits, repeaters) -> str:
        gen = to_digits(tokens, number_map, digits, repeaters)
        return ''.join(str(value) for value in gen)

    tokens = normalize_tokens(spoken_words, homophones, words_to_ignore)
    if all(t in digit_word_list for t in tokens):
        if number_as_str := from_digit_vocalization(
            tokens, named_numbers, digits, repeaters
        ):
            return number_as_str
    else:
        if number := from_number_vocalization(tokens, named_numbers):
            return str(number)


@mod.capture(rule=number_rule)
def number_as_string(m) -> str:
    return numericize(list(m))


@ctx.capture('number', rule='<user.number_as_string>')
def number(m) -> int:
    return int(m.number_as_string)


# @ctx.capture('number_between_1_and_100', rule='<user.number_as_string>')


@mod.capture(rule='<user.number_as_string>')
def times(m) -> int:
    num = int(m.number_as_string)

    if 0 < num < 100:
        return num
    else:
        raise ValueError('The number must be between 1 and 99.')
