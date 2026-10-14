from talon import Context, actions, ui

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
    apps_list = actions.apps.list()
    app_names = {app_name.casefold() for app_name in apps_list}

    return {
        alias: app_path
        for app_name, app_path in apps_list.items()
        for alias in app_aliases.get(app_name, ())
        if alias.casefold() not in app_names
    } | apps_list


@ctx.dynamic_list('apps.running')
def running(phrase: list[str]) -> dict[str, ui.App]:
    """Add aliases for running app names."""
    apps_running = actions.apps.running()
    app_names = {app_name.casefold() for app_name in apps_running}

    return {
        alias: app
        for app_name, app in apps_running.items()
        for alias in app_aliases.get(app_name, ())
        if alias.casefold() not in app_names
    } | apps_running
