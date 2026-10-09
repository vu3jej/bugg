# Text deletion
delete that | delete this | delete [the] selection:
    edit.delete()

delete all:
    edit.delete_all()
delete [this] character:
    edit.delete_right()
delete [this] line:
    edit.delete_line()
delete [this] paragraph:
    edit.delete_paragraph()
delete [this] sentence:
    edit.delete_sentence()
delete [this] word:
    edit.delete_word()
delete [the] next character | delete forward:
    edit.delete_right()
delete [the] next <number> characters:
    edit.delete_right()
    repeat(number-1)
delete [the] next line:
    edit.line_down()
    edit.delete_line()
delete [the] next <number> lines:
    edit.line_down()
    edit.delete_line()
    repeat(number-1)
delete [the] next paragraph:
    edit.paragraph_next()
    edit.delete_paragraph()
delete [the] next <number> paragraphs:
    edit.paragraph_next()
    edit.delete_paragraph()
    repeat(number-1)
delete [the] next sentence:
    edit.sentence_next()
    edit.delete_sentence()
delete [the] next <number> sentences:
    edit.sentence_next()
    edit.delete_sentence()
    repeat(number-1)
delete [the] next word:
    edit.word_right()
    edit.delete_word()
delete [the] next <number> words:
    edit.word_right()
    edit.delete_word()
    repeat(number-1)
delete [the] previous character | backspace [one]:
    edit.delete_left()
delete [the] previous <number> characters | backspace <number>:
    edit.delete_left()
    repeat(number-1)
delete [the] previous line:
    edit.line_start()
    edit.extend_line_up()
    edit.delete()
delete [the] previous <number> lines:
    edit.line_start()
    edit.extend_line_up()
    repeat(number-1)
    edit.delete()
delete [the] previous paragraph:
    edit.paragraph_start()
    edit.extend_paragraph_previous()
    edit.delete()
delete [the] previous <number> paragraphs:
    edit.paragraph_start()
    edit.extend_paragraph_previous()
    repeat(number-1)
    edit.delete()
delete [the] previous sentence:
    edit.sentence_start()
    edit.extend_sentence_previous()
    edit.delete()
delete [the] previous <number> sentences:
    edit.sentence_start()
    edit.extend_sentence_previous()
    repeat(number-1)
    edit.delete()
delete [the] previous word:
    edit.word_left()
    edit.delete_word()
delete [the] previous <number> words:
    edit.extend_word_left()
    repeat(number-1)
    edit.delete()

delete <edit.target>:
    edit.target_delete(edit.target)
