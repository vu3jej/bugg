# Text editing
copy that | copy this | copy [the] selection:
    edit.copy()

cut that | cut this | cut [the] selection:
    edit.cut()

paste that | paste this | paste [[the] clipboard] here:
    edit.paste()

redo that | redo this:
    edit.redo()

undo that | undo this | scratch that:
    edit.undo()

capitalize that | capitalize this | capitalize [the] selection | cap that | cap this | cap [the] selection:
    text = edit.selected_text()
    start = string.slice(text, 0, 1)
    start = start or ""
    start = string.upper(start)
    rest = string.slice(text, 1)
    rest = rest or ""
    if text: insert("{start}{rest}")

correct that | correct this | correct [the] selection:
    correct.show()

bold that | bold this | bold [the] selection:
    edit.bold()
italicize that | italicize this | italicize [the] selection:
    edit.italic()
underline that | underline this | underline [the] selection:
    edit.underline()

lowercase that | lowercase this | lowercase [the] selection:
    text = edit.selected_text()
    if text: insert(string.lower(text))

put [curly] braces around that | put [curly] braces around [the] selection:
    text = edit.selected_text()
    paste("{{{text}}}")
put [double] curly quotes around that | put [double] curly quotes around [the] selection | curly quote that | put [double] smart quotes around that | put [double] smart quotes around [the] selection | smart quote that:
    text = edit.selected_text()
    paste('“{text}”')
put [double] quotes around that | put [double] quotes around [the] selection | quote that:
    text = edit.selected_text()
    paste('"{text}"')
put parentheses around that | put parentheses around [the] selection:
    text = edit.selected_text()
    paste("({text})")
put single curly quotes around that | put single curly quotes around [the] selection | put single smart quotes around that | put single smart quotes around [the] selection:
    text = edit.selected_text()
    paste("‘{text}’")
put single quotes around that | put single quotes around [the] selection:
    text = edit.selected_text()
    paste("'{text}'")
put [square] brackets around that | put [square] brackets around [the] selection:
    text = edit.selected_text()
    paste("[{text}]")

uppercase that | uppercase this | uppercase [the] selection:
    text = edit.selected_text()
    if text: insert(string.upper(text))

capitalize <edit.target>:
    edit.target_capitalize(edit.target)
lowercase <edit.target>:
    edit.target_lower(edit.target)
uppercase <edit.target>:
    edit.target_upper(edit.target)

replace <edit.target> with <phrase> | change <edit.target> to <phrase>:
    edit.target_replace(edit.target, "{phrase}")

correct [the word] <edit.target>:
    correct.target(edit.target)

bold <edit.target>:
    edit.target_bold(edit.target)

italicize <edit.target>:
    edit.target_italic(edit.target)

underline <edit.target>:
    edit.target_underline(edit.target)

insert <phrase> after <edit.target>:
    edit.target_insert_after(edit.target, " {phrase}")
insert <phrase> before <edit.target>:
    edit.target_insert_before(edit.target, "{phrase} ")

put [curly] braces around <edit.target>:
    edit.target_wrap(edit.target, "{", "}")
put [double] curly quotes around <edit.target> | put [double] smart quotes around <edit.target>:
    edit.target_wrap(edit.target, '“', "”")
put [double] quotes around <edit.target>:
    edit.target_wrap(edit.target, '"', '"')
put parentheses around <edit.target>:
    edit.target_wrap(edit.target, '(', ')')
put single curly quotes around <edit.target> | put single smart quotes around <edit.target>:
    edit.target_wrap(edit.target, "‘", "’")
put single quotes around <edit.target>:
    edit.target_wrap(edit.target, "'", "'")
put [square] brackets around <edit.target>:
    edit.target_wrap(edit.target, "[", "]")
