"""Talon app bindings for Zed."""

from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.apps.zed = """
os: mac
and app.bundle: dev.zed.Zed
"""

ctx.matches = 'app:zed'

ctx.tags = ['user.agents']


@ctx.action_class('user')
class UserActions:
    """User actions for the Zed app."""

    def open_agent_panel() -> None:
        """Open the agent panel."""
        actions.key('cmd-shift-/')

    def close_agent_panel() -> None:
        """Close the agent panel."""
        actions.key('cmd-b')
