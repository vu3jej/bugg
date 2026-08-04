import operator
from collections.abc import Iterator
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
    'octillion',
    'nonillion',
    'decillion',
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
    zip(
        [
            'single',
            'double',
            'triple',
            'quadruple',
            'quintuple',
            'sextuple',
            'septuple',
            'octuple',
            'nonuple',
            'decuple',
        ],
        count(1),
    )
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


number_rule = (
    '('
    + '|'.join(
        chain(digits, tens, teens, scales, repeaters, homophones, words_to_ignore)
    )
    + ')+'
)


class Numericizer:
    def __init__(
        self,
        homophones_dct: dict[str, str] = homophones,
        ignore_words: list[str] = words_to_ignore,
        numbers_dct: dict[str, int] = named_numbers,
        digits: list[str] = digits,
        repeaters_dct: dict[str, int] = repeaters,
        scales: list[str] = scales,
    ) -> None:
        self.homophones_dct = homophones_dct
        self.ignore_words = ignore_words
        self.numbers_dct = numbers_dct
        self.digits = digits
        self.repeaters_dct = repeaters_dct
        self.scales = scales
        self.digit_word_list = digits + list(repeaters_dct.keys())

    def normalize_tokens(self, spoken_words: list[str]) -> Iterator[str]:
        for word in spoken_words:
            token = self.homophones_dct.get(word, word)
            if token not in self.ignore_words:
                yield token

    def _to_digits(self, tokens: list[str]) -> Iterator[int]:
        iterator = iter(tokens)

        for token in iterator:
            if token in self.repeaters_dct:
                times = self.repeaters_dct[token]

                try:
                    following_token = next(iterator)
                except StopIteration:
                    return

                if following_token in self.digits:
                    value = self.numbers_dct[following_token]
                    yield from repeat(value, times)
                else:
                    return

            elif token in self.digits:
                yield self.numbers_dct[token]

    def _from_number_vocalization(self, tokens: list[str]) -> int:
        total = 0
        subtotal = 0

        for token in tokens:
            if token not in self.numbers_dct:
                continue

            value = self.numbers_dct[token]

            if token == 'hundred':
                if subtotal != 0:
                    subtotal = subtotal * value
                else:
                    subtotal += value

            elif token in self.scales:
                if subtotal != 0:
                    total += subtotal * value
                else:
                    total += value

                subtotal = 0

            else:
                subtotal += value

        return total + subtotal

    def _from_digit_vocalization(self, tokens: list[str]) -> str:
        gen = self._to_digits(tokens)

        return ''.join(str(value) for value in gen)

    def numericize(self, spoken_words: list[str]) -> str | None:
        tokens = list(self.normalize_tokens(spoken_words))

        if all(t in self.digit_word_list for t in tokens):
            if number_as_str := self._from_digit_vocalization(tokens):
                return number_as_str
        else:
            if number := self._from_number_vocalization(tokens):
                return str(number)

        return None


POSITIVE_SMALL_INTEGER_MIN = 0
POSITIVE_SMALL_INTEGER_MAX = 32767


@mod.capture(rule=number_rule)
def utterance_to_arabic(m) -> str:
    spoken_words = list(m)
    parsed_value = Numericizer().numericize(spoken_words)

    if parsed_value is None:
        raise ValueError('Could not parse spoken words into a number.')

    return parsed_value


@mod.capture(rule='<user.utterance_to_arabic>')
def positive_small_integer(m) -> int:
    spoken_number = m.utterance_to_arabic

    value = int(spoken_number)

    if not (POSITIVE_SMALL_INTEGER_MIN <= value <= POSITIVE_SMALL_INTEGER_MAX):
        raise ValueError(
            f'Number {value} is not within the range 0..32767 for positive small integers.'
        )

    return value
