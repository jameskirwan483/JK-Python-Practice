from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pathlib import Path
import pytest
import time
import uuid
import random
import os
from selenium.webdriver.chrome.options import Options

featureFileDir = 'myfeatures'
featureFile = 'automationExercise.feature'  # Ensure the correct extension
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

# Fixture to initialize and close WebDriver
@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@scenario(str(FEATURE_FILE), 'Register User on Automation Exercise Website')
def test_registraton():
    pass


@given('I have opened the automation practice website')
def automation_practice(driver):
    driver.get('https://www.automationexercise.com/login')

    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")


@when('I use the registration functionality')
def registration(driver):
    unique_id = uuid.uuid4().hex[:8]
    email = f"user_{unique_id}@testmail.com"
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys("jkirwan")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button').click()
    time.sleep(2)
    driver.find_element(By.ID, 'id_gender2').click()
    driver.find_element(By.ID, 'password').send_keys('Password123')
    driver.find_element(By.ID, 'id_gender1').click()
    driver.find_element(By.ID, 'password').send_keys('Password123')
    dropdown = driver.find_element(By.ID, 'days')
    select = Select(dropdown)
    select.select_by_index(10)
    dropdown = driver.find_element(By.ID, 'months')
    select = Select(dropdown)
    select.select_by_index(10)
    dropdown = driver.find_element(By.ID, 'years')
    select = Select(dropdown)
    select.select_by_index(30)
    time.sleep(2)
    driver.find_element(By.ID, 'first_name').send_keys('test')
    driver.find_element(By.ID, 'last_name').send_keys('test')
    driver.find_element(By.ID, 'address1').send_keys('test')
    driver.find_element(By.ID, 'state').send_keys('test')
    driver.find_element(By.ID, 'city').send_keys('test')
    driver.find_element(By.ID, 'zipcode').send_keys('test')
    driver.find_element(By.ID, 'mobile_number').send_keys('123456789')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button').click()

@then('I have registered as a website user')
def registered_user(driver):
    expected_url = "https://www.automationexercise.com/account_created"
    assert driver.current_url == expected_url, f"Expected '{expected_url}', but got '{driver.current_url}'"

@scenario(str(FEATURE_FILE), 'Log into Automation Exercise with existing credentials')
def test_login():
    pass

@given('I want to log into the automation exercise website')
def automation_practice(driver):
    driver.get('https://www.automationexercise.com/login')

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when('I enter my login credentials')
def login_credentials(driver):
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys('jameskirwan483@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys('K9g5zn2X!')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()

@then('I have logged into the website')
def logged_in(driver):
    logout_element = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    assert "Logout" in logout_element.text, "Logout link text is missing or incorrect"

@scenario(str(FEATURE_FILE), 'Log into Automation Exercise with incorrect credentials')
def test_login_incorrect():
    pass

@given('I want to log into the automation exercise website')
def automation_practice(driver):
    driver.get('https://www.automationexercise.com/login')

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when('I enter incorrect login credentials')
def login_credentials(driver):
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys('jameskirwan483@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys('password')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()

@then('I am unable to log into the website')
def cant_login(driver):
    element = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/p')
    expected_text = "Your email or password is incorrect!"
    assert expected_text in element.text, f"Expected '{expected_text}', but found '{element.text}'"

@scenario(str(FEATURE_FILE), 'Open Automation Exercise website and search for a product')
def test_search_random_product():
    pass

@given('I have opened the all products page')
def open_all_products(driver):
    driver.get("https://automationexercise.com/products")
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when('I select a product')
def select_product(driver):
    driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a').click()

@then('an indvidual product is displayed')
def individual_product_selected(driver):
    expected_title = "Automation Exercise - Product Details"
    actual_title = driver.title
    assert actual_title == expected_title, f"Expected '{expected_title}', but found '{actual_title}'"

@scenario(str(FEATURE_FILE), 'Open Automation Exercise website and search for a product')
def test_search_random_product():
    pass

@given('I have opened the automation practice website')
def automation_practice(driver):
    driver.get('https://www.automationexercise.com/login')

    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when('I open the cart page')
def cart_page(driver):
    driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a')

@then('I can verify the subscription link')
def verify_link(driver):
    expected_text = "SUBSCRIPTION"
    element = driver.find_element(By.XPATH, '//*[@id="footer"]/div[1]/div/div/div[2]/div/h2')
    assert expected_text in element.text, f"Expected '{expected_text}', but found '{element.text}'"

@scenario(str(FEATURE_FILE), 'Add a product to the cart on the Automation Practice Website')
def test_product_basket_():
    pass

@given('I have navigated to a specific product page')
def automation_practice(driver):
    driver.get('https://automationexercise.com/product_details/1')

    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when('I click the add to basket button')
def add_to_basket(driver):
    driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button").click()

@then('the product has been added to my basket')
def added_to_basket(driver):
    time.sleep(2)
    expected_text = "Added!"
    element = driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[1]/h4')
    assert expected_text in element.text, f"Expected '{expected_text}', but found '{element.text}'"

@scenario(str(FEATURE_FILE), 'Verify increased product quantity in cart')
def test_increase_basket_quantity():
    pass

@given('I have added a specific product to my basket')
def automation_practice(driver):
    driver.get('https://automationexercise.com/product_details/2')
    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when("I increase quantity of the product")
def increase_quantity(driver):
    quantity_element = driver.find_element(By.ID, 'quantity')
    quantity_element.clear()
    quantity_element.send_keys("5")
    driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]/a/u').click()

@then("I can see the total number of products")
def total_number_products(driver):
    time.sleep(2)
    quantity_element = driver.find_element(By.XPATH, '//*[@id="product-2"]/td[4]/button')
    assert "5" in quantity_element.text, f"Expected '5', but found '{quantity_element.text}'"

@scenario(str(FEATURE_FILE), 'Write a review on a product and confirm its submission')
def test_write_review():
    pass

@given('I am viewing the product which will be reviewed')
def review_product(driver):
    driver.get('https://automationexercise.com/product_details/2')
    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()
    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when('I write a review and click the submit button')
def write_review(driver):
    driver.find_element(By.ID, 'name').send_keys('test name')
    driver.find_element(By.ID, 'email').send_keys('test@test.com')
    driver.find_element(By.ID, 'review').send_keys('test review message')
    driver.find_element(By.ID, 'button-review').click()

@then('the review has been submitted')
def review_submitted(driver):
    quantity_element = driver.find_element(By.ID, 'review-section')
    assert "Thank you for your review" in quantity_element.text, f"Expected '5', but found '{quantity_element.text}'"

@scenario(str(FEATURE_FILE), 'Remove a product from basket which was previously added')
def test_remove_basket():
    pass

@given('I have added a product to the basket')
def automation_practice(driver):
    driver.get('https://automationexercise.com/product_details/2')
    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

    driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]/a/u').click()

@when('I press the cross button')
def remove_from_basket(driver):
    driver.find_element(By.XPATH,'//*[@id="product-2"]/td[6]/a').click()

@then('the product is removed from the basket')
def product_removed(driver):
    time.sleep(2)
    product_removed = driver.find_element(By.XPATH,'//*[@id="empty_cart"]/p')
    assert "Cart is empty!" in product_removed.text, f"Expected '5', but found '{product_removed.text}'"

@scenario(str(FEATURE_FILE), 'Add a product to the basket from recommended products')
def test_remove_basket():
    pass

@given('I have opened the automation practice website')
def automation_practice(driver):
    driver.get('https://www.automationexercise.com/')

    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when("I add a recommended product to the basket")
def recommended_product(driver):
    driver.find_element(By.XPATH, '//*[@id="recommended-item-carousel"]/div/div[2]/div[2]/div/div/div/a/i').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a').click()

@then("it is visible within the cart")
def product_visible(driver):
    time.sleep(2)
    product_basket = driver.find_element(By.XPATH, '//*[@id="product-5"]/td[4]/button')
    assert "1" in product_basket.text, f"Expected '1', but found '{product_basket.text}'"

@scenario(str(FEATURE_FILE), 'Log into account and purchase product')
def test_login_purchase():
    pass

@given('I have logged into my account')
def logged_in(driver):
    driver.get('https://automationexercise.com/login')
    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys('jameskirwan483@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys('K9g5zn2X!')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()

@when('I add a product to my basket')
def product_basket(driver):
    driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]/a/u').click()
    driver.find_element(By.XPATH,'//*[@id="do_action"]/div[1]/div/div/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="cart_items"]/div/div[7]/a').click()
    driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[1]/div/input').send_keys('test user')
    driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[2]/div/input').send_keys('11223344')
    driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[3]/div[1]/input').send_keys('112')
    driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[3]/div[1]/input').send_keys('112')
    driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[3]/div[2]/input').send_keys('11')
    driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[3]/div[3]/input').send_keys('11')

    #click button
    driver.find_element(By.XPATH,'//*[@id="submit"]').click()

@then('I can complete my purchase')
def product_ordered(driver):
    time.sleep(2)
    product_ordered = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/p')
    assert "Congratulations! Your order has been confirmed!" in product_ordered.text, f"Expected 'Congratulations! Your order has been confirmed!', but found '{product_ordered.text}'"

@scenario(str(FEATURE_FILE), 'Validate address in checkout')
def test_valid_address():
    pass

@given("I have logged into my account with a product in the basket")
def basket_added(driver):
    driver.get('https://automationexercise.com/login')
    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")
        #login
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys('jameskirwan483@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys('K9g5zn2X!')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()
        #add product to basket
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a').click()
    time.sleep(2)
        #go to cart
    driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]/a/u').click()

@when("I navigate to the checkout page")
def navigate_checkout(driver):
    driver.find_element(By.XPATH,'//*[@id="do_action"]/div[1]/div/div/a').click()

@then("the correct delivery address is displayed")
def delivery_address(driver):
    address = driver.find_element(By.XPATH,'//*[@id="cart_items"]/div/div[3]/div/div[1]')
    assert "11 Southfield" in address.text, f"Expected '11 Southfield', but found '{address.text}'"

@scenario(str(FEATURE_FILE), 'Filter automation practice products by mens jeans')
def test_validate_filter():
    pass

@given("I am viewing the automation practice homepage")
def homepage(driver):
    driver.get('https://www.automationexercise.com/')

    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when("I apply a filter for mens jeans")
def apply_filter(driver):
    filter = driver.find_element(By.XPATH,'//*[@id="accordian"]/div[2]/div[1]/h4/a/span')
    filter.click()

    subfilter = driver.find_element(By.XPATH,'//*[@id="Men"]/div/ul/li[2]/a')
    subfilter.click()

@then("the mens jeans products are displayed")
def jeans_displayed(driver):
    assert driver.title == "Automation Exercise - Jeans Products", f"Page title mismatch! Found: {driver.title}"

@scenario(str(FEATURE_FILE), 'Subscribe to automation practice website')
def test_validate_filter():
    pass

@given("I want to subscribe to automation practice")
def subscribe(driver):
    driver.get('https://www.automationexercise.com/')

    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()
    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when("I enter my email address")
def enter_email(driver):
    email_subscription = driver.find_element(By.ID,'susbscribe_email')
    email_subscription.send_keys("test@test.com")

    subscribe_button = driver.find_element(By.ID,'subscribe')
    subscribe_button.click()

@then("I am subscribed for updates")
def subscribed(driver):
    subscribed = driver.find_element(By.ID, 'success-subscribe')
    assert "You have been successfully subscribed!" in subscribed.text, f"Expected '11 Southfield', but found '{subscribed.text}'"

@scenario(str(FEATURE_FILE), 'Complete a purchase before downloading an invoice')
def test_download_invoice():
    pass

@given("I have logged into my account before adding a product to my basket")
def logged_product(driver):
    driver.get("https://www.automationexercise.com/login")
    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()
    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

    login = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]')
    login.send_keys("jameskirwan483@gmail.com")
    login.click()

    password = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]')
    password.send_keys("K9g5zn2X!")
    password.click()

    add_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a')
    add_button.click()

    time.sleep(2)

    view_cart = driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]/a/u')
    view_cart.click()

    time.sleep(2)

    checkout_button = driver.find_element(By.XPATH, '//*[@id="do_action"]/div[1]/div/div/a')
    checkout_button.click()

    time.sleep(2)

    place_order = driver.find_element(By.XPATH, '//*[@id="cart_items"]/div/div[7]/a')
    place_order.click()

@when("the purchase is complete")
def purchase_product(driver):

    payment_card = driver.fnd_element(By.XPATH,'//*[@id="payment-form"]/div[1]/div/input')
    payment_card.send_keys("Test Name")

    payment_number = driver.find_element(By.XPATH,'//*[@id="payment-form"]/div[2]/div/input')
    payment_number.send_keys("1234 1234 1234 1234")

    cvc = driver.find_element(By.XPATH,'//*[@id="payment-form"]/div[3]/div[1]/input')
    cvc.send_keys("123")

    expiry_date_month = driver.find_element(By.XPATH,'//*[@id="payment-form"]/div[3]/div[2]/input')
    expiry_date_month.send_keys("12")

    expiry_date_day = driver.find_element(By.XPATH,'//*[@id="payment-form"]/div[3]/div[3]/input')
    expiry_date_day.send_keys("12")

    pay_button = driver.find_element(By.ID,'Submit')
    pay_button.click()

@then("I can download the invoice ")
def download_invoice(driver):
    invoice_button = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/a')
    invoice_button.click()

    if wait_for_invoice(download_dir, partial_name="invoice"):
        print("✅ Invoice downloaded successfully.")
    else:
        raise AssertionError("❌ Invoice was not downloaded.")
