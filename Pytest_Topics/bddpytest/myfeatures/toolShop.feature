Feature: Practice tests for Toolshop Website

  Scenario: Login to Toolshop Website
    Given I navigate to the toolshop website
    When I enter my login details
    Then I can log into the toolshop website

  Scenario: Update users phone number on Toolshop Website
    Given I viewing the users profile
    When I enter a new value into the phone number field
    Then the phone number is updated

  Scenario: Add a product as a favourite
    Given I have navigated to a product page
    When I click the favourites link
    Then the product has been added as a favourite

  Scenario: Send a message to tool shop via contact form
    Given I am viewing the contact form
    When I populate the form details
    Then I can send the form to tool shop


