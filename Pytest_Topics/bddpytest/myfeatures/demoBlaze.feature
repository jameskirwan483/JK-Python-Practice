Feature: Practice tests for Demoblaze website

Scenario: Send a message to Demo Blaze using the contact feature
  Given I navigate to the Demo Blaze website
  When I use the contact option
  Then the message is successfully sent

