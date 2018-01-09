# -*- coding: utf-8 -*-

from collective.portletpage.interfaces import IPortletPage
from zope.interface import implements
from plone.dexterity.content import Item

class PortletPage(Item):
    """A page with some body text and a list of portlets.
    """
    implements(IPortletPage)
    meta_type = 'PortletPage'
    portal_type = 'Portlet Page'