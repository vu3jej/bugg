from collections.abc import Callable
from inspect import signature
from operator import attrgetter

from talon import Module, actions, settings

from .actions import EditAction, EditSimpleAction
from .modifiers import EditModifier

mod = Module()
#
# mod.setting(
#     'edit_word_selection_delay',
#     type=int,
#     default=75,
#     desc='Sleep required between word selections',
# )

mod.setting(
    'edit_word_selection_delay',
    type=str,
    default='75ms',
    desc='Sleep required between word selections',
)
mod.setting(
    'edit_line_selection_delay',
    type=str,
    default='75ms',
    desc='Sleep required between line selections',
)


class DelayedAction:
    @staticmethod
    def select_words(action, modifier):
        direction = modifier.kind
        count = modifier.count
        # delay = settings.get('edit_word_selection_delay')
        delay = settings.get('user.edit_word_selection_delay')

        if direction == 'wordLeft':
            callback = actions.edit.extend_word_left
        else:
            callback = actions.edit.extend_word_right

        for _ in range(count):
            callback()
            actions.sleep(delay)

        actions.user.apply_edit(action)

    @staticmethod
    def move_by_word(action, modifier):
        direction = modifier.kind
        count = modifier.count
        # delay = settings.get('edit_word_selection_delay')
        delay = settings.get('user.edit_word_selection_delay')

        if direction == 'wordLeft':
            callback = actions.edit.word_left
        else:
            callback = actions.edit.word_right

        for _ in range(count):
            callback()
            actions.sleep(delay)

    @staticmethod
    def select_lines(action, modifier):
        direction = modifier.kind
        count = modifier.count
        # delay = settings.get('edit_line_selection_delay')
        delay = settings.get('user.edit_line_selection_delay')

        if direction == 'lineUp':
            step_vertical = actions.edit.extend_line_up
            snap_horizontal = actions.edit.extend_line_start
        else:
            step_vertical = actions.edit.extend_line_down
            snap_horizontal = actions.edit.extend_line_end

        for _ in range(count):
            step_vertical()
            actions.sleep(delay)

        snap_horizontal()
        actions.sleep(delay)

        actions.user.apply_edit(action)


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


@mod.action_class
class Actions:
    def resolve_edit_action(action_modifier_pair: tuple[str, str]) -> Callable | None:
        """Resolve the specialized handler for an edit action and modifier pair"""
        if name := throttled_callback_map.get(action_modifier_pair):
            # f = methodcaller(name)
            # return f(DelayedAction)
            #
            f = attrgetter(name)
            return f(DelayedAction)

        else:
            return compound_callback_map.get(action_modifier_pair)

    def dispatch_edit_command(
        action: EditAction | str, modifier: EditModifier | str
    ) -> None:
        """Executes an edit action against a specific text modifier"""
        if isinstance(action, str):
            action = EditSimpleAction(action)

        if isinstance(modifier, str):
            modifier = EditModifier(modifier)

        key = (action.kind, modifier.kind)

        if callback := actions.user.resolve_edit_action(key):
            if signature(callback).parameters.get('modifier'):
                callback(action, modifier)

            else:
                callback()
        else:
            actions.user.apply_edit_modifier(modifier)
            actions.user.apply_edit(action)
