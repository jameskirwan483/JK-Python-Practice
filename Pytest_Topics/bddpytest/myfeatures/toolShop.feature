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

  Scenario: Purchase a product
    Given I have added a product to my basket
    When I proceed to checkout
    Then I can order the product

  Scenario: Update language on homepage
    Given I am on the tool shop homepage
    When I update the page language
    Then the language is now french

  Scenario: Search for the powertools using dropdown
    Given I am on the tool shop homepage
    When I use the categories dropdown
    Then I have filtered by powertools

  Scenario: Apply a filter and select a random product
    Given I apply a filter for wrenches
    When I select a random wrench
    Then the wrench is displayed

  Scenario: Loop through each available pagination option
    Given I am on the tool shop homepage
    When I navigate through each page individually
    Then I am taken to the final page