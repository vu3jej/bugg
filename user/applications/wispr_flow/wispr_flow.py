"""Wispr Flow dictation actions."""

from talon import Context, Module, actions
from talon.mac import applescript

mod = Module()
ctx = Context()

mod.tag('recording', desc='Recording is active')


@mod.action_class
class WisprFlowActions:
    """Actions used to control Wispr Flow dictation state."""

    def start_dictation() -> None:
        """Start Wispr Flow dictation with Talon speech recognition disabled."""
        ctx.tags = ['user.recording']
        actions.speech.disable()
        applescript.run(
            'do shell script "open --background wispr-flow://start-hands-free"'
        )

    def stop_dictation() -> None:
        """Stop Wispr Flow dictation and re-enable Talon speech recognition."""
        applescript.run(
            'do shell script "open --background wispr-flow://stop-hands-free"'
        )
        actions.speech.enable()
        ctx.tags = []

    def cancel_dictation() -> None:
        """Cancel dictation using Escape, then re-enable speech and clear context."""
        actions.key('escape')
        actions.speech.enable()
        ctx.tags = []
