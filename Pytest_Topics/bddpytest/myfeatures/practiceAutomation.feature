@regression_tests
Feature: New automation practice website

@popup_test
Scenario: Close an alert popup
  Given I navigate to the alerts page
  When I open the alert popup
  Then I can close the popup1

@popup_test
Scenario: Confirm a close popup
  Given I navigate to the alerts page
  When I open the confirm popup
  Then I close the alert popup

@popup_test
Scenario: Cancel an alert popup
  Given I navigate to the alerts page
  When I open the confirm popup but cancel it
  Then the pop-up has been closed

@popup_test
  Scenario: Enter text into popup prompt
  Given I navigate to the alerts page
  When I open the popup prompt before entering text
  Then the popup prompt has been closed

@popup_test
  Scenario: Cancel a popup prompt without entering text
  Given I navigate to the alerts page
  When I open the popup prompt but cancel the popup
  Then the popup prompt has been cancelled

@UI_test
Scenario: Glad the slider and update the selected value
  Given I am viewing the slide practice page
  When I pull the slider
  Then the current value is updated

@UI_test
Scenario: Confirm that a link is broken
  Given I am validating a broken link
  When I click the link which is broken
  Then I can confirm the response code is 404

@UI_test
Scenario: Confirm that a file can be uploaded
  Given I want to upload a file
  When I use the upload functionality
  Then the file is successfully uploaded

@UI_test
Scenario: Close the on-screen pop up
  Given I am viewing a page with a pop-up add
  When I press the close button
  Then the pop-up add has disappeared

@UI_test
Scenario: Select a date using the calendar
  Given I open the calendar page
  When I select a date
  Then the date is entered into the field

@UI_test
Scenario: Complete the form fields and submit
  Given I am on the form completion page
  When I complete the mandatory fields
  Then I can submit the form

@UI_test
Scenario: Search for data within a table
  Given I am viewing a page showing a table
  When I am search for the results within a table
  Then the correct results are displayed


