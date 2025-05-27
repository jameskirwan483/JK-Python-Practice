Feature: 5 elements learning website - Information Links

Scenario: Open the 5elements website and navigate to the Shipping page
  Given I have opened the 5elements website
  When I click the Shipping & Returns link
  Then I am taken to the Shipping page

Scenario: Open the 5elements website and navigate to the Privacy Notice page
  Given I have opened the 5elements website
  When I click the Privacy Notice link
  Then I am taken to the Privacy Notice page

Scenario: Open the 5elements website and navigate to the Conditions of Use page
  Given I have opened the 5elements website
  When I click the Conditions of Use page
  Then I am taken to the Conditions of Use page

Scenario: Open the 5elements website and navigate to the Contact Us page
  Given I have opened the 5elements website
  When I click the Contact Us link
  Then I am taken to the Contact Us page

Scenario: Send a message to store owner using contact field
  Given I am viewing the Contact Us page
  When I populate all the fields in the message box
  Then my message is sent to the Store Owner

Scenario: Confirm that



