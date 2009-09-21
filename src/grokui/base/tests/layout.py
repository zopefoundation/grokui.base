"""
Building admin pages using `AdminView`
======================================

:doctest:
:layer: grokui.base.tests.test_grokuibase.FunctionalLayer

We create a browser to watch our views:

    >>> from zope.testbrowser.testing import Browser
    >>> browser = Browser()
    >>> browser.addHeader('Authorization', 'Basic mgr:mgrpw')
    >>> browser.handleErrors = False

To create a view that automatically comes with the GrokUI layout, we
can derive from `grokui.base.AdminView`.

Instances of `AdminView` are in fact `megrok.layout.Page` instances
that render the content provided by a template or `render` method
into a given layout.

When we render PlainAdminView, we will get a complete Grok UI page
with the contents delivered by the `render()` method inserted:

    >>> browser.open('http://localhost/++grokui++/caveview')
    >>> print browser.contents
    <html xmlns="http://www.w3.org/1999/xhtml">
    ...
     <title>Grok Administration Interface</title>
    ...
    <BLANKLINE>
        <div id="grokui-content">Hello from CaveAdminView</div>
    <BLANKLINE>
    ...
    </html>

We also provided a ``title`` with our page. Therefore we will get an
entry in the navigation bar:

    >>> print browser.contents
    <html xmlns="http://www.w3.org/1999/xhtml">
    ...
    <ul id="grokui-menu-entries">
      <li>
        <a href="http://localhost/caveview"
           title="cave management">cave management</a>
      </li>
    </ul>
    ...
    </html>
    
"""
import grok
from grokui.base import AdminView

class CaveAdminView(AdminView):
    """An admin page to administer caves.
    """
    grok.name('caveview')
    # This title will appear in the navigation bar:
    grok.title('cave management')
    def render(self):
        """This will go into a standard Grok UI page.
        """
        return u'Hello from CaveAdminView'