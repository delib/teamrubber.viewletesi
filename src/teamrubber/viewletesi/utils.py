from zope.publisher.interfaces.browser import IBrowserView
from zope.interface import implements

class FakeView(object):
    """ A lightweight fake view for getting viewlets/viewlet managers """
    implements(IBrowserView)