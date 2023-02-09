from fanstatic import Library
from fanstatic import Resource


library = Library('grokui.base', 'static')

grok_css = Resource(library, 'grok.css')

favicon = Resource(library, 'favicon.ico')
