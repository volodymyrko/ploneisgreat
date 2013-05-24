from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class InfoView(BrowserView):

    template = ViewPageTemplateFile('info_view.pt')

    def __call__(self):
        """"""
        self.title = getattr(self.context, 'title', '')
        self.description = getattr(self.context, 'description', '')
        self.venues = self.context.getVenueReferenceField()
        return self.template()
