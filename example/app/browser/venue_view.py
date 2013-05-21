from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class VenueView(BrowserView):

    template = ViewPageTemplateFile('venue_view.pt')

    def __call__(self):
        """"""
        self.latitude = getattr(self.context, 'latitude', '')
        self.longitude = getattr(self.context, 'longitude', '')
        self.point_title = getattr(self.context, 'title', '')
        return self.template()
