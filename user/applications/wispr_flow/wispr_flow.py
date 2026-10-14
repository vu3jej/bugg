"""Wispr Flow dictation actions."""

from talon import Context, Module, actions, app

# Context matching restricts action dispatch, not Python imports.
if app.platform == 'mac':
    from talon.mac import applescript

mod = Module()
ctx = Context()
ctx.matches = 'os: mac'

mod.tag('recording', desc='Recording is active')


@mod.action_class
class WisprFlowActions:
    """Actions used to control Wispr Flow dictation state."""

    def start_dictation() -> None:
        """Start Wispr Flow dictation with Talon speech recognition disabled."""

    def stop_dictation() -> None:
        """Stop Wispr Flow dictation and re-enable Talon speech recognition."""

    def cancel_dictation() -> None:
        """Cancel dictation using Escape, then re-enable speech and clear context."""


@ctx.action_class('user')
class WisprFlowMacActions:
    """Implement Wispr Flow dictation actions on macOS."""

    def start_dictation() -> None:
        ctx.tags = ['user.recording']
        actions.speech.disable()
        applescript.run(
            'do shell script "open --background wispr-flow://start-hands-free"'
        )

    def stop_dictation() -> None:
        applescript.run(
            'do shell script "open --background wispr-flow://stop-hands-free"'
        )
        actions.speech.enable()
        ctx.tags = []

    def cancel_dictation() -> None:
        actions.key('escape')
        actions.speech.enable()
        ctx.tags = []
