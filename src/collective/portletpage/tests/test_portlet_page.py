# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from collective.portletpage.testing import COLLECTIVE_PORTLETPAGE_INTEGRATION_TESTING  # noqa
from collective.portletpage.interfaces import IPortletPage

import unittest2 as unittest


class Portlet_PageIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_PORTLETPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Portlet_Page')
        schema = fti.lookupSchema()
        self.assertEqual(IPortletPage, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Portlet_Page')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Portlet_Page')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IPortletPage.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Portlet_Page', 'Portlet_Page')
        self.assertTrue(
            IPortletPage.providedBy(self.portal['Portlet_Page'])
        )
