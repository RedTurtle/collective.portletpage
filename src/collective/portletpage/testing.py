# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.portletpage


class CollectivePortletpageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.portletpage)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.portletpage:default')


COLLECTIVE_PORTLETPAGE_FIXTURE = CollectivePortletpageLayer()


COLLECTIVE_PORTLETPAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PORTLETPAGE_FIXTURE,),
    name='CollectivePortletpageLayer:IntegrationTesting'
)


COLLECTIVE_PORTLETPAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PORTLETPAGE_FIXTURE,),
    name='CollectivePortletpageLayer:FunctionalTesting'
)


COLLECTIVE_PORTLETPAGE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_PORTLETPAGE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectivePortletpageLayer:AcceptanceTesting'
)
