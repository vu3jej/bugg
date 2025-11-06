from talon import Context

ctx = Context()
ctx.matches = "code.language: python"


ctx.lists["user.keyword"] = {
    "false": "False",
    "none": "None",
    "true": "True",
    "and": "and",
    "as": "as",
    "assert": "assert",
    "as sink": "async",
    "await": "await",
    "break": "break",
    "class": "class",
    "continue": "continue",
    "funk": "def",
    "delete": "del",
    "elf": "elif",
    "else": "else",
    "except": "except",
    "finally": "finally",
    "for": "for",
    "from": "from",
    "global": "global",
    "if": "if",
    "import": "import",
    "in": "in",
    "is": "is",
    "lambda": "lambda",
    "nonlocal": "nonlocal",
    "not": "not",
    "or": "or",
    "pass": "pass",
    "raise": "raise",
    "return": "return",
    "try": "try",
    "while": "while",
    "with": "with",
    "yield": "yield",
}
