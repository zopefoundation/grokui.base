# -*- coding: utf-8 -*-

import unittest
import doctest
import grokui.base
from zope.fanstatic.testing import ZopeFanstaticBrowserLayer


def test_suite():
    suite = unittest.TestSuite()
    readme = doctest.DocFileSuite(
        '../README.txt',
        optionflags=(
            doctest.ELLIPSIS
            | doctest.NORMALIZE_WHITESPACE
            | doctest.REPORT_NDIFF
            | doctest.IGNORE_EXCEPTION_DETAIL
        ))
    readme.layer = ZopeFanstaticBrowserLayer(grokui.base)
    suite.addTest(readme)
    return suite
