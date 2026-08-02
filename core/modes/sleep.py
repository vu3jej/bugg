"""Disable Talon speech by default when Talon starts."""

from talon import actions, app


def disable() -> None:
    """Disable speech recognition when Talon emits the ready event."""
    actions.speech.disable()


app.register('ready', disable)
