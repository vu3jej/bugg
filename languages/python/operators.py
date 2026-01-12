from talon import Context

ctx = Context()
ctx.matches = 'code.language: python'


ctx.lists['user.comparison_operator'] = {
    'equality': '==',
    'not equal': '!=',
    'less': '<',
    'less or equal': '<=',
    'greater': '>',
    'greater or equal': '>=',
}


ctx.lists['user.arithmetic_operator'] = {
    'addition': '+',
    'subtraction': '-',
    'multiplication': '*',
    'exponentiation': '**',
    'division': '/',
    'integer division': '//',
    'modulo': '%',
}


ctx.lists['user.bitwise_operator'] = {
    'bitwise and': '&',
    'bitwise or': '|',
    'bitwise exclusive or': '^',
    'bitwise inversion': '~',
    'left shift': '<<',
    'right shift': '>>',
}

ctx.lists['user.other_op'] = {
    'dot': '.',
    'at': '@',
}


ctx.lists['user.enclosing_delimiter'] = {
    'left parenthesis': '(',
    'right parenthesis': ')',
    'left square bracket': '[',
    'right square bracket': ']',
    'left brace': '{',
    'right brace': '}',
}


ctx.lists['user.other_delimiter'] = {
    'comma': ',',
    'colon': ':',
    'exclamation': '!',
    'semicolon': ';',
    'equal': '=',
    'right arrow': '->',
}


ctx.lists['user.assignment_operator'] = {
    'addition assignment': '+=',
    'subtraction assignment': '-=',
    'multiplication assignment': '*=',
    'exponentiation assignment': '**=',
    'division assignment': '/=',
    'integer division assignment': '//=',
    'remainder assignment': '%=',
    'bitwise and assignment': '&=',
    'bitwise or assignment': '|=',
    'bitwise exclusive or assignment': '^=',
    'left shift assignment': '<<=',
    'right shift assignment': '>>=',
    'matrix multiplication assignment': '@=',
    'the walrus operator': ':=',
}
