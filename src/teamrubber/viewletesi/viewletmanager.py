from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.viewletmanager.manager import OrderedViewletManager

class ESIOrderedViewletManager(OrderedViewletManager):
    template = ViewPageTemplateFile("viewletmanager.pt")

    def render(self):
        template = ESIOrderedViewletManager.template.__of__(self.context)
        return template(viewlets=self.viewlets)

    def isESI(self, viewlet):
        identifier = "%s:%s" % (self.__name__,viewlet.__name__)
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
        