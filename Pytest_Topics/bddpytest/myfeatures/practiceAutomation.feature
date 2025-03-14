Feature: New automation practice website

Scenario: Close an alert popup
  Given I navigate to the alerts page
  When I open the alert popup
  Then I can close the popup

Scenario: Confirm a close popup
  Given I navigate to the alerts page
  When I open the confirm popup
  Then I close the alert popup


Scenario: Glad the slider and update the selected value
  Given I am viewing the slide practice page
  When I pull the slider
  Then the current value is updated

Scenario: Confirm that a link is broken
  Given I am validating a broken link
  When I click the link which is broken
  Then I can confirm the response code is 404

Scenario: Confirm that a file can be uploaded
  Given I want to upload a file
  When I use the upload functionality
  Then the file is successfully uploaded

Scenario: Close the on-screen pop up
  Given I am viewing a page with a pop-up add
  When I press the close button
  Then the pop-up add has disappeared

Scenario: Select a date using the calendar
  Given I open the calendar page
  When I select a date
  Then the date is entered into the field

Scenario: Complete the form fields and submit
  Given I am on the form completion page
  When I complete the mandatory fields
  Then I can submit the form


Scenario: Search for data within a table
  Given I am viewing a page showing a table
  When I am search for the results within a table
  Then the correct results are displayed


