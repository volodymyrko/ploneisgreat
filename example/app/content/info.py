"""Definition of the Info content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from example.app.interfaces import IInfo
from example.app.config import PROJECTNAME

InfoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.StringField(
        name='info_title',
        required=True,
        widget=atapi.StringWidget(
            label='Title',
            description='Please enter title.',
            visible= {'view': 'visible', 'edit': 'visible'},
        ),
    ),
    atapi.StringField(
        name='info_desc',
        required=True,
        widget=atapi.StringWidget(
            label='Desc',
            description='Please enter desc.',
            visible= {'view': 'visible', 'edit': 'visible'},
        ),
    ),
    atapi.ReferenceField('VenueReferenceField',
        relationship = 'venuerelationship',
        multiValued = 'True',
        allowed_types = ('Venue',),
        widget = atapi.ReferenceWidget(
            label='Reference Venue',
            description='Choose reference venue',
            visible= {'view': 'visible', 'edit': 'visible'},
            ),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

InfoSchema['title'].storage = atapi.AnnotationStorage()
InfoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(InfoSchema, moveDiscussion=False)


class Info(base.ATCTContent):
    """Info desc"""
    implements(IInfo)

    meta_type = "Info"
    schema = InfoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Info, PROJECTNAME)
