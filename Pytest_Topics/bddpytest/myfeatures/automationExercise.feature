Feature: Practice Automation Exercises

Scenario: Register User on Automation Exercise Website
  Given I have opened the automation practice website
  When I use the registration functionality
  Then I have registered as a website user

Scenario: Log into Automation Exercise with existing credentials
  Given I want to log into the automation exercise website
  When I enter my login credentials
  Then I have logged into the website

Scenario: Log into Automation Exercise with incorrect credentials
  Given I want to log into the automation exercise website
  When I enter incorrect login credentials
  Then I am unable to log into the website


