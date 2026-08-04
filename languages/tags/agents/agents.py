"""Agents language tag actions."""

from talon import Module

mod = Module()

mod.tag('agents', desc='Controls for agent panel actions in any IDE or editor')


@mod.action_class
class Actions:
    """Agent panel action hooks."""

    def open_agent_panel() -> None:
        """Open the agent panel."""

    def open_new_agent_thread() -> None:
        """Open a new agent thread."""

    def close_agent_panel() -> None:
        """Close the agent panel."""

    def allow_agent_prompt() -> None:
        """Allow the currently proposed LLM agent prompt."""

    def deny_agent_prompt() -> None:
        """Deny the currently proposed LLM agent prompt."""
