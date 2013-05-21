from zope.interface import Interface
from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('info')


class IInfoForm(Interface):

    info_title = TextLine(
        title=_(u'Title'),
        description=_(u'Please enter title.'),
        required=True)
    info_desc= TextLine(
        title=_(u'Desc'),
        description=_(u'Please enter desc.'),
        required=False)



from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from z3c.form import form, field

class InfoForm(form.Form):

    fields = field.Fields(IInfoForm)
    ignoreContext = True

    def updateWidgets(self):
        super(InfoForm, self).updateWidgets()

    @button.buttonAndHandler(u'Save')
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            return False

#        if data['hello_world_name'] is not None:
#            hello_name = data['hello_world_name']
#        else:
#            hello_name = 'World'

#        IStatusMessage(self.request).addStatusMessage(
#            "Title %s" % title,
#            'info')
        redirect_url = "%s/@@info_form" % self.context.absolute_url()
        self.request.response.redirect(redirect_url)

    @button.buttonAndHandler(u'Cancel')
    def handleCancel(self, action):
#        IStatusMessage(self.request).addStatusMessage(
#            "Hello No One",
#            'info')
        redirect_url = "%s/@@info_form" % self.context.absolute_url()
        self.request.response.redirect(redirect_url)

from plone.z3cform.layout import wrap_form
InfoFormView = wrap_form(InfoForm)
