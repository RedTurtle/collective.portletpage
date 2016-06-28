# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.portletpage.testing import COLLECTIVE_PORTLETPAGE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.portletpage is properly installed."""

    layer = COLLECTIVE_PORTLETPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.portletpage is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.portletpage'))

    def test_browserlayer(self):
        """Test that ICollectivePortletpageLayer is registered."""
        from collective.portletpage.interfaces import (
            ICollectivePortletpageLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectivePortletpageLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_PORTLETPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.portletpage'])

    def test_product_uninstalled(self):
        """Test if collective.portletpage is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.portletpage'))

    def test_browserlayer_removed(self):
        """Test that ICollectivePortletpageLayer is removed."""
        from collective.portletpage.interfaces import ICollectivePortletpageLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectivePortletpageLayer, utils.registered_layers())
