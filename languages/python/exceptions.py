from talon import Context, Module

mod = Module()
mod.list('exception_class', desc='Exception classes')


ctx = Context()
ctx.matches = 'code.language: python'


ctx.lists['user.exception_class'] = {
    'generic exception': 'Exception',
    'value': 'ValueError',
    'attribute': 'AttributeError',
    'buffer': 'BufferError',
    'end of file': 'EOFError',
    'import': 'ImportError',
    'module not found': 'ModuleNotFoundError',
    'lookup': 'LookupError',
    'index': 'IndexError',
    'key': 'KeyError',
    'memory': 'MemoryError',
    'name': 'NameError',
    'unbound local': 'UnboundLocalError',
    'system': 'SystemError',
    'type': 'TypeError',
    'unicode': 'UnicodeError',
    'unicode decode': 'UnicodeDecodeError',
    'unicode encode': 'UnicodeEncodeError',
    'unicode translate': 'UnicodeTranslateError',
}
