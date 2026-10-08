from talon import Module, actions

mod = Module()


mod.tag('keywords', desc='Tag to enable keywords')


mod.list('keyword', desc='Programming language keywords')


@mod.capture(rule='{user.keyword}')
def keyword(m) -> str:
    """Returns a single keyword"""
    return m.keyword


@mod.action_class
class Actions:
    def insert_keyword(keywords: list[str]) -> None:
        """Insert keywords"""
        actions.insert(' '.join(keywords))
