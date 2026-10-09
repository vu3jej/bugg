# Dictation
-
type <phrase> | literal <phrase> | say <phrase>:
    dictate.phrase(phrase)

insert [today's] date:
    date = time.now()
    s = time.format(date, "%b %d, %Y")
    auto_insert(s)

space key:
    key(space)

press [the] [combo] <key> key [[repeated] <number_small> [times]]:
    number_small = number_small or 1
    key(key)
    repeat(number_small - 1)

enter that:
    key(enter)

spell {letter}+:
    for l in letter_list: insert(l)

command mode:
    mode.disable("dictation")
    mode.enable("command")
dictation mode:
    mode.enable("dictation")

select last dictation: dictate.select_last()
correct last dictation: correct.last()
