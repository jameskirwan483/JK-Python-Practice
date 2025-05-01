Feature: Sauce Demo Regression Tests

Scenario: Login to Sauce Labs with incorrect credentials
    Given I am viewing the Sauce Demo homepage
    When I attempt to login with incorrect credentials
    Then I am unable to login to Sauce Demo

Scenario: Login to Sauce Labs with correct credentials
    Given I am viewing the Sauce Demo homepage
    When I attempt to login with correct credentials
    Then I can login to Sauce Demo