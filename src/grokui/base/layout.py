import grok
import megrok.menu
from zope.traversing.browser.absoluteurl import absoluteURL

from grokui.base import GrokUILayer
from grokui.base import IGrokUIRealm
from grokui.base import IUIPanel
from grokui.base import MainMenu
from grokui.base import resource


grok.layer(GrokUILayer)


class GrokUILayout(grok.Layout):
    """The general layout for the administration
    """
    grok.context(IGrokUIRealm)
    title = "Grok User Interface"

    def update(self):
        resource.grok_css.need()
        resource.favicon.need()
        self.baseurl = absoluteURL(self.context, self.request) + '/'


class GrokUIView(grok.Page):
    """A grok ui view.
    """
    grok.baseclass()
    grok.context(IGrokUIRealm)
    grok.implements(IUIPanel)
    megrok.menu.menuitem(MainMenu)
