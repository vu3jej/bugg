from talon import Context, Module

mod = Module()
ctx = Context()

# mod.list('edit_repeatable_motion', desc='Repeatable cursor motions')
mod.list('edit_repeatable_modifier', desc='Edit repeatable modifiers')
mod.list('edit_modifier', desc='Edit action modifiers')
mod.list('edit_action', desc='Edit actions')


# ctx.lists['user.edit_repeatable_motion'] = {
ctx.lists['user.edit_repeatable_modifier'] = {
    'left': 'left',
    'right': 'right',
    'word': 'word',
    'word left': 'wordLeft',
    'word right': 'wordRight',
    'line up': 'lineUp',
    'line down': 'lineDown',
}

ctx.lists['user.edit_modifier'] = {
    'all': 'document',
    'paragraph': 'paragraph',
    'line': 'line',
    'line start': 'lineStart',
    'line end': 'lineEnd',
    'file start': 'fileStart',
    'file end': 'fileEnd',
    'way left': 'lineStart',
    'way right': 'lineEnd',
    'way up': 'fileStart',
    'way down': 'fileEnd',
}


ctx.lists['user.edit_action'] = {
    'select': 'select',
    'go before': 'before',
    'go after': 'after',
    'cut': 'cutToClipboard',
    'copy': 'copyToClipboard',
    'paste': 'pasteFromClipboard',
    'paste to': 'pasteFromClipboard',
    'remove': 'delete',
    'clear': 'delete',
}


ctx.lists['user.delimiter_pair'] = {
    'curly': 'curlyBrackets',
    'diamond': 'angleBrackets',
    'round': 'parentheses',
    'box': 'squareBrackets',
    'quad': 'doubleQuotes',
    'twin': 'singleQuotes',
    'skis': 'backtickQuotes',
    'void': 'whitespace',
    'escaped round': 'escapedParentheses',
    'escaped box': 'escapedSquareBrackets',
    'escaped quad': 'escapedDoubleQuotes',
    'escaped twin': 'escapedSingleQuotes',
}
