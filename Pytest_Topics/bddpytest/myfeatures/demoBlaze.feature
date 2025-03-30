Feature: Practice tests for Demoblaze website

Scenario: Send a message to Demo Blaze using the contact feature
  Given I navigate to the Demo Blaze website
  When I use the contact option
  Then the message is successfully sent

Scenario: Attempt to sign-up to Demo Blaze with email already used
  Given I navigate to the Demo Blaze website
  When I sign up with an email already used
  Then the sign-up is unsuccessful

Scenario: Attempt to sign-up to Demo Blaze with a new email address
  Given I navigate to the Demo Blaze website
  When I sign up with a new email address
  Then the sign-up is successful




