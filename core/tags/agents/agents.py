"""Agents language tag actions."""

from talon import Context, Module

mod = Module()

mod.tag('agents', desc='Controls for agent panel actions in any IDE or editor')
mod.list('agent_reply_prompt', desc='Reply prompts to send to the agent')

ctx = Context()
ctx.matches = 'tag: user.agents'

ctx.lists['user.agent_reply_prompt'] = {
    'go ahead': 'go ahead',
    'go for it': 'go for it',
    'please continue': 'please continue',
    'make the change': 'make the change',
    'use that approach': 'use that approach',
    'that works': 'that works',
    'approved': 'approved',
    'confirm': 'confirm',
    'you may proceed': 'you may proceed',
}


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

    def confirm_agent_response(message: str) -> None:
        """Send a confirmation message to the agent."""
