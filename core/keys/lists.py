from talon import Context, Module

mod = Module()

ctx = Context()


ctx.lists['user.letter_key'] = {
    'air': 'a',
    'bat': 'b',
    'cap': 'c',
    'drum': 'd',
    'each': 'e',
    'fine': 'f',
    'gust': 'g',
    'harp': 'h',
    'sit': 'i',
    'jury': 'j',
    'crunch': 'k',
    'look': 'l',
    'made': 'm',
    'near': 'n',
    'odd': 'o',
    'pit': 'p',
    'quench': 'q',
    'red': 'r',
    'sun': 's',
    'trap': 't',
    'urge': 'u',
    'vest': 'v',
    'whale': 'w',
    'plex': 'x',
    'yank': 'y',
    'zip': 'z',
}


ctx.lists['user.number_key'] = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


ctx.lists['user.navigation_key'] = {
    'left': 'left',
    'right': 'right',
    'down': 'down',
    'up': 'up',
    'home': 'home',
    'end': 'end',
    'page up': 'pageup',
    'page down': 'pagedown',
}
