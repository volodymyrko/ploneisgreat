from zope.interface import Interface
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from example.app import appMessageFactory as _

from zope.i18nmessageid import MessageFactory
__ = MessageFactory("plone")

def test(*args):
    points = ''
    p_template = """
    var point = new google.maps.LatLng{point};
    var marker = new google.maps.Marker({{
              position: point,
              map: map,
              title: '{point_title}',
            }});
    """

    obj = args[0]
    venues = obj.venues
    if not len(venues):
        point1 = (venues[0].latitude, venues[0].longitude)

        for p in venues:
            points += p_template.format(point=(p.latitude, p.longitude),
                point_title=p.title)
    else:
        return ''

    return """
    <style type="text/css">
    #map-canvas {{
            height: 300px;
            width: 300px;
            text-align: center;
            margin-right: auto;
            margin-left: auto
          }}
    </style>
      
    <script type="text/javascript"
        src='https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false'>
    </script>

    <script type="text/javascript">
          function initialize(){{
            var point = new google.maps.LatLng{point1};
            var mapOptions = {{
              center: point,
              zoom: 12,
              mapTypeId: google.maps.MapTypeId.ROADMAP
            }};

            var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

            {point_list}

            }}
            google.maps.event.addDomListener(window, 'load', initialize)
          </script>


    <dl class="portlet portletInfoPortlet" i18n:domain="example.app">

    <dt class="portletHeader">
        <span class="portletTopLeft"></span>
        <span>
           Google Map
        </span>
        <span class="portletTopRight"></span>
    </dt>

    <div id="map-canvas"></div>
    """.format(point1=point1, point_list=points)
    




class IInfoPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    # TODO: Add any zope.schema fields here to capture portlet configuration
    # information. Alternatively, if there are no settings, leave this as an
    # empty interface - see also notes around the add form and edit form
    # below.

    # some_field = schema.TextLine(title=_(u"Some field"),
    #                              description=_(u"A field to use"),
    #                              required=True)


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IInfoPortlet)

    # TODO: Set default values for the configurable parameters here

    # some_field = u""

    # TODO: Add keyword parameters for configurable parameters here
    # def __init__(self, some_field=u''):
    #    self.some_field = some_field

    def __init__(self):
        pass

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return __(u"Info portlet")


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = test
    #ViewPageTemplateFile('infoportlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        context = args[0]
        self.venues = context.getVenueReferenceField()
        #import pdb; pdb.set_trace()


# NOTE: If this portlet does not have any configurable parameters, you can
# inherit from NullAddForm and remove the form_fields variable.

class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IInfoPortlet)

    def create(self, data):
        return Assignment(**data)


# NOTE: IF this portlet does not have any configurable parameters, you can
# remove this class definition and delete the editview attribute from the
# <plone:portlet /> registration in configure.zcml

class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IInfoPortlet)
