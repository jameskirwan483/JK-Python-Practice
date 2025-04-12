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

Scenario: Verify Test Cases Page
  Given I have opened the automation practice website
  When I click the test cases button
  Then I have navigated to the test cases page

Scenario: Complete Automation Exercise Contact Form
  Given I have opened the automation contact form
  When I populate the forms details
  Then I can send the form to automation exercise

Scenario: Open Automation Exercise website and search for a product
  Given I have opened the all products page
  When I select a product
  Then an indvidual product is displayed

Scenario: Verify subscription on the cart page
  Given I have oepened the automaton practice website
  When I open the cart page
  Then I can verify the subscription link



