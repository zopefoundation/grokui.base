# -*- coding: utf-8 -*-

import grok
from z3c.flashmessage.message import PersistentMessage
from z3c.flashmessage.sources import SessionMessageSource
from z3c.flashmessage.receiver import GlobalMessageReceiver
from z3c.flashmessage.interfaces import IMessageSource


class AdminMessageSource(grok.GlobalUtility):
    """Source for the administration messages
    """
    grok.name('admin')
    grok.implements(IMessageSource)

    message = None

    def send(self, message, type='admin'):
        self.message = PersistentMessage(message, type)

    def list(self, type=None):
        if self.message is None:
            return
        if type is None or self.message.type == type:
            yield self.message

    def delete(self, message):
        if message is self.message:
            self.message = None
        else:
            raise KeyError(message)


grok.global_utility(GlobalMessageReceiver)
grok.global_utility(SessionMessageSource, name='session')
