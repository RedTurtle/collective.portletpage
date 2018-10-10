from plone.dexterity.content import Item
from collective.portletpage.interfaces import IPortletPage
from zope.interface import implements

class PortletPage(Item):
    implements(IPortletPage)

    portal_type = 'Portlet Page'
    meta_type = 'PortletPage'
