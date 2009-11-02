from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.viewletmanager.manager import OrderedViewletManager

class ESIOrderedViewletManager(OrderedViewletManager):
    template = ViewPageTemplateFile("viewletmanager.pt")

    def render(self):
        template = ESIOrderedViewletManager.template.__of__(self.context)
        return template(viewlets=self.viewlets)

    def getViewletIdentifier(self,viewlet):
        if not viewlet.__name__ and hasattr(viewlet,'addTags'):
            return "%s:opsuite.tagging.viewlet" % (self.__name__)
            
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
        