from talon import Context, Module, actions, clip, settings

mod = Module()
ctx = Context()


@ctx.action_class('edit')
class EditActions:
    def selected_text() -> str:
        timeout = settings.get('user.selected_text_timeout')

        with clip.capture(timeout=timeout) as c:
            actions.edit.copy()

        try:
            return c.text()
        except clip.NoChange:
            return ''

    def line_insert_down():
        actions.edit.line_end()
        actions.key('enter')

    def selection_clone():
        actions.edit.copy()
        actions.edit.select_none()
        actions.edit.paste()

    def line_clone():
        actions.edit.line_start()
        actions.edit.extend_line_end()
        actions.edit.copy()
        actions.edit.right()
        actions.key('enter')
        actions.edit.paste()

    def select_word():
        actions.edit.right()
        actions.edit.word_left()
        actions.edit.extend_word_right()


@mod.action_class
class Actions:
    def paste(text: str) -> None:
        """Pastes text and preserves clipboard"""
        with clip.revert():
            clip.set_text(text)
            actions.edit.paste()
            actions.sleep('150ms')

    def delete_right() -> None:
        """Delete character to the right"""
        actions.key('delete')

    def delete_all() -> None:
        """Delete all text in the current document"""
        actions.edit.select_all()
        actions.edit.delete()

    def words_left(n: int) -> None:
        """Move left by the given number of words"""
        for _ in range(n):
            actions.edit.word_left()

    def words_right(n: int) -> None:
        """Move right by the given number of words"""
        for _ in range(n):
            actions.edit.word_right()

    def cut_word_left() -> None:
        """Cuts the word to the left"""
        actions.edit.extend_word_left()
        actions.edit.cut()

    def cut_word_right() -> None:
        """Cuts the word to the right"""
        actions.edit.extend_word_right()
        actions.edit.cut()

    def copy_word_left() -> None:
        """Copies the word to the left"""
        actions.edit.extend_word_left()
        actions.edit.copy()

    def copy_word_right() -> None:
        """Copies the word to the right"""
        actions.edit.extend_word_right()
        actions.edit.copy()

    def select_line_start() -> None:
        """Select to the beginning of the current line"""
        if actions.edit.selected_text():
            actions.edit.left()

        actions.edit.extend_line_start()

    def select_line_end() -> None:
        """Select to the end of the current line"""
        if actions.edit.selected_text():
            actions.edit.right()

        actions.edit.extend_line_end()

    def line_middle() -> None:
        """Calculate the midpoint of the line and repositions the cursor"""
        actions.edit.select_line()
        text = actions.edit.selected_text()
        midpoint = len(text) // 2

        actions.edit.left()

        for _ in range(midpoint):
            actions.edit.right()

    def cut_line() -> None:
        """Cut the current line"""
        actions.edit.select_line()
        actions.edit.cut()

    def line_tail_break(symbol: str) -> None:
        """Appends the given symbol to the end of the line and creates a new line below"""
        actions.edit.line_end()
        actions.key(symbol)
        actions.edit.line_insert_down()

    def before_line_up() -> None:
        """Move to the start of the previous line"""
        actions.edit.up()
        actions.edit.line_start()

    def after_line_up() -> None:
        """Move to the end of the previous line"""
        actions.edit.up()
        actions.edit.line_end()

    def before_line_down() -> None:
        """Move to the start of the next line"""
        actions.edit.down()
        actions.edit.line_start()

    def after_line_down() -> None:
        """Move to the end of the next line"""
        actions.edit.down()
        actions.edit.line_end()
