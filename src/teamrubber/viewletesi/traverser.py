from zope.component import adapts
from zope.interface import implements, Interface
from zope.traversing.interfaces import ITraversable
from zope.publisher.interfaces.http import IHTTPRequest
from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IViewletManager
from zope.viewlet.interfaces import IViewlet
from utils import FakeView
from AccessControl.SecurityManagement import newSecurityManager
from Products.CMFCore.utils import getToolByName

_marker = object()

class ViewletNamespace(object):
    implements(ITraversable)
    adapts(Interface, IHTTPRequest)
   
    def __init__(self, context, request=None):
        self.context = context
        self.request = request
       
    def traverse(self, name, more):
        manager_name, viewlet_name = name.split(':')
        view = FakeView()
        manager = getMultiAdapter((self.context, self.request, view), IViewletManager, name=manager_name)
        viewlet = getMultiAdapter((self.context, self.request, view, manager), IViewlet, name=viewlet_name)
        super_user = getToolByName(self.context,'portal_url').getWrappedOwner()
        authenticated_user = self.request.get('AUTHENTICATED_USER')
        newSecurityManager(self.request,super_user)
        view = self.context.restrictedTraverse('viewlet_renderer')
        view.setViewlet(viewlet)
        newSecurityManager(self.request,authenticated_user)
        return view
        