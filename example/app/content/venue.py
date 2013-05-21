"""Definition of the Venue content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from example.app.interfaces import IVenue
from example.app.config import PROJECTNAME

VenueSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.FloatField(
        name='latitude',
        required=True,
        widget=atapi.DecimalWidget(
            label='latitude',
            description='Please enter latitude.',
            visible= {'view': 'visible', 'edit': 'visible'},
        ),
    ),
    atapi.FloatField(
        name='longitude',
        required=True,
        widget=atapi.DecimalWidget(
            label='longitude',
            description='Please enter longitude.',
            visible= {'view': 'visible', 'edit': 'visible'},
        ),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

VenueSchema['title'].storage = atapi.AnnotationStorage()
VenueSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(VenueSchema, moveDiscussion=False)


class Venue(base.ATCTContent):
    """Venue Description"""
    implements(IVenue)

    meta_type = "Venue"
    schema = VenueSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Venue, PROJECTNAME)
