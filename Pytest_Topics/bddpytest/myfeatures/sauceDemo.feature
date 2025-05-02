Feature: Sauce Demo Regression Tests

Scenario: Login to Sauce Labs with incorrect credentials
    Given I am viewing the Sauce Demo homepage
    When I attempt to login with incorrect credentials
    Then I am unable to login to Sauce Demo

Scenario: Login to Sauce Labs with correct credentials
    Given I am viewing the Sauce Demo homepage
    When I attempt to login with correct credentials
    Then I can login to Sauce Demo

Scenario: Attempt to login to Sauce Labs with locked out credentials
    Given I am viewing the Sauce Demo homepage
    When I attempt to login with locked out credentials
    Then I am unable to login to Sauce Demo

Scenario: Log out of Sauce Labs after logging in
    Given I have logged into the Sauce Labs website
    When I use the log out function
    Then I have logged out of my Sauce Labs account

Scenario: Navigate to the About Me page of Sauce Labs
    Given I have logged into the Sauce Labs website
    When I press the About link
    Then I am taken to the About Me page

