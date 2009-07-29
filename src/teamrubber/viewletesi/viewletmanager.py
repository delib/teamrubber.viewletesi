from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.viewletmanager.manager import OrderedViewletManager

class ESIOrderedViewletManager(OrderedViewletManager):
    template = ViewPageTemplateFile("viewletmanager.pt")

    def render(self):
        template = ESIOrderedViewletManager.template.__of__(self.context)
        return template(viewlets=self.viewlets)

    def isESI(self, viewlet):
        identifier = viewlet.__class__.__module__ + viewlet.__class__.__name__
        return True
        try:
            registry = self.context.portal_registry
        except:
            return False
        else:
            pass # XXX TODO
    