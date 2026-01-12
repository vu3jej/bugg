from talon import Context, Module

mod = Module()
ctx = Context()
ctx.matches = 'code.language: python'


mod.list('assignment_operator', desc='does what it says on the tin')
mod.list('bitwise_operator', desc='does what it says on the tin')
mod.list('comparison_operator', desc='does what it says on the tin')
mod.list('arithmetic_operator', desc='does what it says on the tin')
mod.list('other_op', desc='does what it says on the tin')
mod.list('enclosing_delimiter', desc='does what it says on the tin')
mod.list('other_delimiter', desc='does what it says on the tin')


ctx.tags = ['user.keywords', 'user.operators']


@ctx.capture(
    rule='{user.assignment_operator}|{user.bitwise_operator}|{user.comparison_operator}|{user.arithmetic_operator}|{user.other_op}|{user.enclosing_delimiter}|{user.other_delimiter}'
)
def operator(m):
    return str(m)
