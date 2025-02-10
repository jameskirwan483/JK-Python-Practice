Feature: Practice tests for Parabank website

  Scenario: Open website and navigate to the Locations page
    Given I want to search for Parabank locations
    When I click the locations link
    Then I am taken to the locations page

  Scenario: Open website and navigate to the Products page
    Given I want to search for Parabank products
    When I click the products link
    Then I am taken to the Products page

  Scenario: Send an email to Parabank via customer care
    Given I navigate to the Parabank contact page
    When I complete the form customer care form
    Then It is sent to the customer care team

  Scenario: Register for the Parabank website
    Given I navigate to the Parabank registration page
    When I complete the registration form
    Then I can register for the Parabank website

  Scenario: Log out of website
    Given I am logged into the website
    When I click the logout link
    Then I am successfully logged out

  Scenario: Applying for a loan
    Given I am logged into the website
    When I populate the loan request details
    Then my loan request has been processed

  Scenario: Transfer funds to pay a bill
    Given I am logged into Robobank website
    When I select the transfer funds link
    Then I can transfer funds between accounts

  Scenario: Open a Savings Account
    Given I have logged into Robobank website
    When I select the new account option
    Then I can open a savings account

  Scenario: Pay my bill
    Given I have logged into Robobank website
    When I fill out the online form
    Then I can pay the bill online

  Scenario: Update my profile
    Given I have logged into Robobank website
    When I fill out the update profile section
    Then my profile is successfully updated


