from Products.Five.browser import BrowserView


class ESIViewlet(BrowserView):

    def setViewlet(self, viewlet):
        self.viewlet = viewlet

    def __call__(self):
        self.viewlet.update()
        return self.viewlet.render()
