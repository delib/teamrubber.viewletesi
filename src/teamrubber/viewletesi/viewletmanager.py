from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.viewletmanager.manager import OrderedViewletManager
from zope.component import getAdapters
from zope.viewlet.interfaces import IViewlet

class ESIOrderedViewletManager(OrderedViewletManager):
    template = ViewPageTemplateFile("viewletmanager.pt")

    def render(self):
        template = ESIOrderedViewletManager.template.__of__(self.context)
        return template(viewlets=self.viewlets)

    def update(self):
        """See zope.contentprovider.interfaces.IContentProvider"""
        # Lifted from zope.viewlet to force setting of __name__
        
        self.__updated = True

        # Find all content providers for the region
        viewlets = getAdapters((self.context, self.request, self.__parent__, self),IViewlet)

        viewlets = self.filter(viewlets)
        viewlets = self.sort(viewlets)

        # Force the viewlets to have __name__ set
        for name,viewlet in viewlets:
            if not viewlet.__name__:
                viewlet.__name__ = name

        # Just use the viewlets from now on
        self.viewlets = [viewlet for name, viewlet in viewlets]

        # Update all viewlets
        [viewlet.update() for viewlet in self.viewlets]


    def getViewletIdentifier(self,viewlet):
        return  "%s:%s" % (self.__name__,viewlet.__name__)


    def getESIPath(self,viewlet):
        identifier = self.getViewletIdentifier(viewlet)
        url = "%s/++viewlet++%s" % (self.context.absolute_url(),identifier)
        return url


    def isESI(self, viewlet):
        identifier = self.getViewletIdentifier(viewlet)
        try:
            registry = self.context.portal_registry
        except:
            return False
        else:
            esi_enabled = registry.get('esi_viewlets_enabled',False)
            if esi_enabled:
                esi_viewlets = registry.get('esi_viewlets')
                if identifier in esi_viewlets:
                    return True
            return False
