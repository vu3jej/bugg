from talon import Context

ctx = Context()


ctx.lists['user.code_formatter'] = {
    'all caps': 'allCaps',
    'camel': 'camelCase',
    'snake': 'snakeCase',
    'kebab': 'kebabCase',
    'constant': 'screamingSnakeCase',
    'hammer': 'pascalCase',
    'smash': 'unseparated',
    'dunder': 'doubleUnderscoreSeparated',
    'dotted': 'dotSeparated',
    'packed': 'doubleColonSeparated',
    'conga': 'slashSeparated',
    'slasher': 'leadingSlashSeparated',
    'string': 'singleQuoted',
    'dub string': 'doubleQuoted',
}
