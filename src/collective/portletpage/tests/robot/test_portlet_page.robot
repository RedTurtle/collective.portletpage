# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.portletpage -t test_portlet_page.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.portletpage.testing.COLLECTIVE_PORTLETPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_portlet_page.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Portlet_Page
  Given a logged-in site administrator
    and an add portlet_page form
   When I type 'My Portlet_Page' into the title field
    and I submit the form
   Then a portlet_page with the title 'My Portlet_Page' has been created

Scenario: As a site administrator I can view a Portlet_Page
  Given a logged-in site administrator
    and a portlet_page 'My Portlet_Page'
   When I go to the portlet_page view
   Then I can see the portlet_page title 'My Portlet_Page'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add portlet_page form
  Go To  ${PLONE_URL}/++add++Portlet_Page

a portlet_page 'My Portlet_Page'
  Create content  type=Portlet_Page  id=my-portlet_page  title=My Portlet_Page


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the portlet_page view
  Go To  ${PLONE_URL}/my-portlet_page
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a portlet_page with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the portlet_page title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
