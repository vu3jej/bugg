"""Agents language tag actions."""

from talon import Module

mod = Module()

mod.tag('agents', desc='Controls for agent panel actions in any IDE or editor')


@mod.action_class
class Actions:
    """Agent panel action hooks."""

    def open_agent_panel() -> None:
        """Open the agent panel."""

    def close_agent_panel() -> None:
        """Close the agent panel."""
