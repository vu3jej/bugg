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

    def open_new_agent_thread() -> None:
        """Open a new agent thread."""
        actions.key('alt-cmd-shift-n')
        actions.sleep('100ms')
        actions.key('cmd-n')

    def close_agent_panel() -> None:
        """Close the agent panel."""
        actions.key('cmd-b')

    def allow_agent_prompt() -> None:
        """Allow the currently proposed LLM agent prompt."""
        actions.key('cmd-y')

    def deny_agent_prompt() -> None:
        """Deny the currently proposed LLM agent prompt."""
        actions.key('alt-cmd-z')
