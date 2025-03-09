Feature: New automation practice website

Scenario: Close an alert popup
  Given I navigate to the alerts page
  When I open the alert popup
  Then I can close the popup

Scenario: Glad the slider and update the selected value
  Given I am viewing the slide practice page
  When I pull the slider
  Then the current value is updated

Scenario: Confirm that a link is broken
  Given I am validating a broken link
  When I click the link which is broken
  Then I can confirm the response code is 404


