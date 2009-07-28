from zope.component import adapts
from zope.interface import implements, Interface
from zope.app.traversing.interfaces import ITraverser
from zope.traversing.interfaces import ITraversable
from zope.publisher.interfaces.http import IHTTPRequest

_marker = object()


class ViewletNamespace(object):
    implements(ITraversable)
    adapts(Interface, IHTTPRequest)
   
    def __init__(self, context, request=None):
        self.context = context
        self.request = request
       
    def traverse(self, name, more):
        # Broken
        viewletmanager = getMultiAdapter((self.context, self.request), IViewletManager, name=u"plone.portaltop")
        viewlet = getMultiAdapter((self.context, self.request, self, viewletmanager), Interface, name=name)
        return viewlet.render()