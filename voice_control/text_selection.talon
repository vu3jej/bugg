# Text selection
select [this] character:
    edit.select_none()
    edit.extend_right()
select [this] line:
    edit.select_line()
select [this] paragraph:
    edit.select_paragraph()
select [this] sentence:
    edit.select_sentence()
select [this] word:
    edit.select_word()
select all [[the] text] | select [entire] document:
    edit.select_all()
select [the] next character:
    edit.extend_right()
select [the] next <number> characters:
    edit.extend_right()
    repeat(number-1)
select [the] next line:
    edit.extend_line_down()
select [the] next <number> lines:
    edit.extend_line_down()
    repeat(number-1)
select [the] next paragraph:
    edit.extend_paragraph_next()
select [the] next <number> paragraphs:
    edit.extend_paragraph_next()
    repeat(number-1)
select [the] next sentence:
    edit.extend_sentence_next()
select [the] next <number> sentences:
    edit.extend_sentence_next()
    repeat(number-1)
select [the] next word:
    edit.extend_word_right()
select [the] next <number> words:
    edit.extend_word_right()
    repeat(number-1)
select [the] previous character:
    edit.select_none()
    edit.extend_left()
select [the] previous <number> characters:
    edit.select_none()
    edit.extend_left()
    repeat(number - 1)
select [the] previous line:
    edit.line_start()
    edit.extend_line_up()
select [the] previous <number> lines:
    edit.line_start()
    edit.extend_line_up()
    repeat(number-1)
select [the] previous paragraph:
    edit.paragraph_start()
    edit.extend_paragraph_previous()
select [the] previous <number> paragraphs:
    edit.paragraph_start()
    edit.extend_paragraph_previous()
    repeat(number-1)
select [the] previous sentence:
    edit.sentence_start()
    edit.extend_sentence_previous()
select [the] previous <number> sentences:
    edit.sentence_start()
    edit.extend_sentence_previous()
    repeat(number-1)
select [the] previous word:
    edit.word_left()
    edit.select_word()
select [the] previous <number> words:
    edit.word_left()
    edit.select_word()
    edit.right()
    edit.extend_word_left()
    repeat(number-1)
select that:
    dictate.select_last()
deselect that | deselect this | unselect that | unselect this:
    edit.select_none()

extend [the] selection back [by] <number> characters | extend [the] selection backward [by] <number> characters | extend [the] selection back [by] one character | extend [the] selection backward [by] one character:
    number = number or 1
    edit.extend_left()
    repeat(number-1)
extend [the] selection back [by] <number> lines | extend [the] selection backward [by] <number> lines | extend [the] selection back [by] one line | extend [the] selection backward [by] one line:
    number = number or 1
    edit.extend_line_up()
    repeat(number-1)
extend [the] selection back [by] <number> paragraphs | extend [the] selection backward [by] <number> paragraphs | extend [the] selection back [by] one paragraph | extend [the] selection backward [by] one paragraph:
    number = number or 1
    edit.extend_paragraph_previous()
    repeat(number-1)
extend [the] selection back [by] <number> sentences | extend [the] selection backward [by] <number> sentences | extend [the] selection back [by] one sentence | extend [the] selection backward [by] one sentence:
    number = number or 1
    edit.extend_sentence_previous()
    repeat(number-1)
extend [the] selection back [by] <number> words | extend [the] selection backward [by] <number> words | extend [the] selection back [by] one word | extend [the] selection backward [by] one word:
    number = number or 1
    edit.extend_word_left()
    repeat(number-1)
extend [the] selection [forward] [by] <number> characters | extend [the] selection [forward] [by] one character:
    number = number or 1
    edit.extend_right()
    repeat(number-1)
extend [the] selection [forward] [by] <number> lines | extend [the] selection [forward] [by] one line:
    number = number or 1
    edit.extend_line_down()
    repeat(number-1)
extend [the] selection [forward] [by] <number> paragraphs | extend [the] selection [forward] [by] one paragraph:
    number = number or 1
    edit.extend_paragraph_next()
    repeat(number-1)
extend [the] selection [forward] [by] <number> sentences | extend [the] selection [forward] [by] one sentence:
    number = number or 1
    edit.extend_sentence_next()
    repeat(number-1)
extend [the] selection [forward] [by] <number> words | extend [the] selection [forward] [by] one word:
    number = number or 1
    edit.extend_word_right()
    repeat(number-1)
extend [the] selection to [the] beginning | select to [the] beginning:
    edit.extend_file_start()
extend [the] selection to [the] end | select to [the] end:
    edit.extend_file_end()

select [from] [the word] <edit.target>:
    edit.target_select(edit.target)
