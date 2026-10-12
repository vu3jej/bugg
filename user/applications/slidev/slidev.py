"""Talon app bindings for Slidev controls."""

from talon import Context, Module

mod = Module()
ctx = Context()

mod.tag('slidev_controls', desc='Enable Slidev presentation commands')


@mod.action_class
class SlidevActions:
    """Actions to enable/disable Slidev command bindings."""

    def enable_slidev_controls() -> None:
        """Enable Slidev controls."""
        ctx.tags = ['user.slidev_controls']

    def disable_slidev_controls() -> None:
        """Disable Slidev controls."""
        ctx.tags = []

    def toggle_slidev_controls() -> None:
        """Toggle Slidev controls."""
        if 'user.slidev_controls' in ctx.tags:
            ctx.tags = []
        else:
            ctx.tags = ['user.slidev_controls']
