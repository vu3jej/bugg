"""Wispr Flow dictation actions."""

from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.tag('wispr_flow_active', desc='Dictation overlay is active')

hotkey = 'alt-shift-h'


@mod.action_class
class WisprFlowActions:
    """Actions used to control Wispr Flow dictation state."""

    def start_dictation() -> None:
        """Disable speech recognition and mark Wispr Flow as active."""
        ctx.tags = ['user.wispr_flow_active']
        actions.speech.disable()
        actions.key(hotkey)

    def stop_dictation() -> None:
        """Enable speech recognition and clear Wispr Flow active tag."""
        actions.key(hotkey)
        actions.speech.enable()
        ctx.tags = []

    def cancel_dictation() -> None:
        """Cancel dictation using Escape, then re-enable speech and clear context."""
        actions.key('escape')
        actions.speech.enable()
        ctx.tags = []

    def enable_speech_if_not_wispr_flow() -> None:
        """Enable speech only when Wispr Flow mode is not active."""
        if 'user.wispr_flow_active' in ctx.tags:
            return
        actions.speech.enable()
