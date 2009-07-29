from Products.Five.browser import BrowserView


class ESIViewlet(BrowserView):

    def setViewlet(self,viewlet):
        self.viewlet = viewlet

    def __call__(self):
        self.viewlet.update()
        import pdb
        pdb.set_trace()
        return self.viewlet.render()
