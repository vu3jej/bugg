from talon import actions

modifier_callback_map = {
    'document': actions.edit.select_all,
    'paragraph': actions.edit.select_paragraph,
    'word': actions.edit.extend_word_right,
    'wordLeft': actions.edit.extend_word_left,
    'wordRight': actions.edit.extend_word_right,
    'left': actions.edit.extend_left,
    'right': actions.edit.extend_right,
    'lineUp': actions.edit.extend_line_up,
    'lineDown': actions.edit.extend_line_down,
    'line': actions.edit.select_line,
    'lineStart': actions.edit.extend_line_start,
    'lineEnd': actions.edit.extend_line_end,
    'fileStart': actions.edit.extend_file_start,
    'fileEnd': actions.edit.extend_file_end,
    'selection': actions.edit.skip,
}
