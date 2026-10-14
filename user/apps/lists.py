from talon import Context, actions

ctx = Context()
ctx.matches = 'os: mac'

app_aliases: dict[str, tuple[str, ...]] = {
    'Amazon Kindle': ('kindle',),
    'Brave Browser': ('brave',),
    'DBeaver': ('beaver',),
    'Google Chrome': ('chrome',),
    'iTerm': ('shell', 'eye term', 'eye term two'),
    'iTerm2': ('shell', 'eye term', 'eye term two'),
    'TextEdit': ('editor',),
    'Wispr Flow': ('flow',),
    'Zed': ('said',),
    'zoom.us': ('zoom',),
}


@ctx.dynamic_list('apps.list')
def launchable(phrase: list[str]) -> dict[str, str]:
    """Add aliases for launchable app names."""
    apps = actions.apps.list()

    return {
        alias: app_path
        for app_name, app_path in apps.items()
        for alias in app_aliases.get(app_name, ())
    } | apps


@ctx.dynamic_list('apps.running')
def running(phrase: list[str]) -> dict[str, str]:
    """Add aliases for running app names."""
    apps = {app_name: app_name for app_name in actions.apps.running()}

    return {
        alias: app_name for app_name in apps for alias in app_aliases.get(app_name, ())
    } | apps
