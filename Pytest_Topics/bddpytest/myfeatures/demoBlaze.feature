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

Scenario: Add a product to your basket on Demo Blaze website
  Given I navigate to the Demo Blaze website
  When I click the add to cart button
  Then the product is now in my basket

Scenario: Log into Demo Blaze website with existing email
  Given I press the login button on the Demo Blaze website
  When I enter previously used login details
  Then I have logged into my account

Scenario: Purchase a product from the Demo Blaze website
  Given I have added a product to my cart
  When I populate he place order details
  Then I can purchase the product







