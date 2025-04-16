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

