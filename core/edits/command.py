from talon import Module, actions

mod = Module()

mod.setting(
    'edit_word_selection_delay',
    type=int,
    default=75,
    desc='Sleep required between word selections',
)


throttled_callback_map = {
    ('after', 'wordLeft'): 'move_by_word',
    ('after', 'wordRight'): 'move_by_word',
    ('before', 'wordLeft'): 'move_by_word',
    ('before', 'wordRight'): 'move_by_word',
    ('delete', 'word'): 'select_words',
    ('delete', 'wordLeft'): 'select_words',
    ('delete', 'wordRight'): 'select_words',
    ('delete', 'lineUp'): 'select_lines',
    ('delete', 'lineDown'): 'select_lines',
    ('cutToClipboard', 'word'): 'select_words',
    ('cutToClipboard', 'wordLeft'): 'select_words',
    ('cutToClipboard', 'wordRight'): 'select_words',
    ('cutToClipboard', 'lineUp'): 'select_lines',
    ('cutToClipboard', 'lineDown'): 'select_lines',
    ('copyToClipboard', 'word'): 'select_words',
    ('copyToClipboard', 'wordLeft'): 'select_words',
    ('copyToClipboard', 'wordRight'): 'select_words',
    ('copyToClipboard', 'lineUp'): 'select_lines',
    ('copyToClipboard', 'lineDown'): 'select_lines',
    # ,       : 'select_lines'
    ('select', 'lineUp'): 'select_lines',
    ('select', 'lineDown'): 'select_lines',
}


compound_callback_map = {
    ('select', 'wordLeft'): actions.edit.extend_word_left,
    ('select', 'wordRight'): actions.edit.extend_word_right,
    ('select', 'word'): actions.edit.extend_word_right,
    ('select', 'left'): actions.edit.extend_left,
    ('select', 'right'): actions.edit.extend_right,
    ('before', 'line'): actions.edit.line_start,
    ('before', 'lineUp'): actions.user.before_line_up,
    ('before', 'lineDown'): actions.user.before_line_down,
    ('before', 'paragraph'): actions.edit.paragraph_start,
    ('before', 'document'): actions.edit.file_start,
    ('before', 'fileStart'): actions.edit.file_start,
    ('before', 'selection'): actions.edit.left,
    ('before', 'wordLeft'): actions.edit.word_left,
    ('before', 'word'): actions.edit.word_left,
    ('after', 'line'): actions.edit.line_end,
    ('after', 'lineUp'): actions.user.after_line_up,
    ('after', 'lineDown'): actions.user.after_line_down,
    ('after', 'paragraph'): actions.edit.paragraph_end,
    ('after', 'document'): actions.edit.file_end,
    ('after', 'fileEnd'): actions.edit.file_end,
    ('after', 'selection'): actions.edit.right,
    ('after', 'wordRight'): actions.edit.word_right,
    ('after', 'wordLeft'): actions.edit.word_left,
    ('after', 'word'): actions.edit.word_right,
    ('delete', 'left'): actions.edit.delete,
    ('delete', 'right'): actions.edit.delete_right,
    ('delete', 'line'): actions.edit.delete_line,
    ('delete', 'paragraph'): actions.edit.delete_paragraph,
    ('delete', 'document'): actions.user.delete_all,
    ('delete', 'selection'): actions.edit.delete,
    ('cutToClipboard', 'line'): actions.user.cut_line,
    ('cutToClipboard', 'selection'): actions.edit.cut,
    ('copyToClipboard', 'selection'): actions.edit.copy,
}
