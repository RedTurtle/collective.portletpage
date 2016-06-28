# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from collective.portletpage import MessageFactory as _
from plone.app.portlets.interfaces import IColumn
from plone.portlets.interfaces import IPortletManager
from zope import schema
from zope.interface import Interface



class ICollectivePortletpageLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPortletPageColumn(IPortletManager, IColumn):
    """Marker interface describing columns on a portlet page
    """

class IPortletPage(Interface):
    """ A portlet page"""


