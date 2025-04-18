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

Scenario: Add a product to the cart on the Automation Practice Website
  Given I have navigated to a specific product page
  When I click the add to basket button
  Then the product has been added to my basket

Scenario: Verify increased product quantity in cart
  Given I have added a specific product to my basket
  When I increase quantity of the product
  Then I can see the total number of products

Scenario: Write a review on a product and confirm its submission
  Given I am viewing the product which will be reviewed
  When I write a review and click the submit button
  Then the review has been submitted

Scenario: Remove a product from basket which was previously added
  Given I have added a product to the basket
  When I press the cross button
  Then the product is removed from the basket

Scenario: Add a product to the basket from recommended products
  Given I have opened the automation practice website
  When I add a recommended product to the basket
  Then it is visible within the cart