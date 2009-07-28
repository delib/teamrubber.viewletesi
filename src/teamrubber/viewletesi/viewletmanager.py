from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.viewletmanager.manager import OrderedViewletManager

class ESIOrderedViewletManager(OrderedViewletManager):
    template = ViewPageTemplateFile("viewletmanager.pt")
    
    def isESI(self, viewlet):
        return True
    