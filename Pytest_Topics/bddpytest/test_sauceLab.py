from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pytest
import time
from selenium.webdriver.chrome.options import Options

featureFileDir = 'myfeatures'
featureFile = 'sauceDemo.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-blink-features=PasswordManagerDetection")
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerEnabled")
    options.add_argument("--incognito")  # Optional: avoids stored passwords
    options.add_argument("--user-data-dir=/tmp/test-profile")
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    yield driver
    driver.quit()

USERNAME_INPUT_FIELD = (By.ID, 'user-name')
PASSWORD_INPUT_FIELD = (By.ID, 'password')
LOGIN_BUTTON = (By.ID, 'login-button')
ERROR_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
BURGER_MENU = (By.ID,'react-burger-menu-btn')
LOGOUT_BUTTON = (By.XPATH, '//*[@id="logout_sidebar_link"]')
ABOUT_BUTTON = (By.XPATH, '//*[@id="about_sidebar_link"]')
ADD_PRODUCT= (By.ID, 'add-to-cart-sauce-labs-backpack')
VIEW_BASKET = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
VIEW_CHECKOUT = (By.ID, 'checkout')
FIRST_NAME_FIELD = (By.ID, 'first-name')
LAST_NAME_FIELD = (By.ID, 'last-name')
POSTCODE_FIELD = (By.ID, 'postal-code')
CONTINUE_BUTTON = (By.ID, 'continue')
FINISH_BUTTON = (By.ID, 'finish')
REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-backpack')


@scenario(str(FEATURE_FILE), 'Login to Sauce Labs with incorrect credentials')
def test_failed_login():
    pass

@given('I am viewing the Sauce Demo homepage')
def sauce_homepage(driver):
    driver.get('https://www.saucedemo.com/')

@when('I attempt to login with incorrect credentials')
def sauce_incorrect_credentials(driver):
    perform_login(driver, 'Incorrect login', 'Incorrect password')

@then('I am unable to login to Sauce Demo')
def sauce_incorrect_login(driver):
    error_message = driver.find_element(*ERROR_MESSAGE)
    expected_error = "Epic sadface"
    assert expected_error in error_message.text, f"Expected error message: '{expected_error}', but got: '{error_message.text}'"

def perform_login(driver, username, password):
    driver.find_element(*USERNAME_INPUT_FIELD).send_keys(username)
    driver.find_element(*PASSWORD_INPUT_FIELD).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()

@scenario(str(FEATURE_FILE), 'Login to Sauce Labs with correct credentials')
def test_successful_login():
    pass

@when('I attempt to login with correct credentials')
def sauce_incorrect_credentials(driver):
    perform_login(driver, 'standard_user', 'secret_sauce')

@then('I can login to Sauce Demo')
def sauce_successful_login(driver):
    expected_url = 'https://www.saucedemo.com/inventory.html'
    actual_url = driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, but got: {actual_url}"

@scenario(str(FEATURE_FILE), 'Attempt to login to Sauce Labs with locked out credentials')
def test_locked_out_login():
    pass

@when('I attempt to login with locked out credentials')
def locked_out_credentials(driver):
    perform_login(driver, 'locked_out_user', 'locked_out_password')

@scenario(str(FEATURE_FILE), 'Log out of Sauce Labs after logging in')
def test_successful_logout():
    pass

@given('I have logged into the Sauce Labs website')
def website_login(driver):
    driver.get('https://www.saucedemo.com/')
    perform_login(driver, 'standard_user', 'secret_sauce')

@when('I use the log out function')
def log_out(driver):
    perform_logout(driver)

@then('I have logged out of my Sauce Labs account')
def logged_out(driver):
    expected_url = 'https://www.saucedemo.com/'
    actual_url = driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, but got: {actual_url}"

def perform_logout(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BURGER_MENU)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

@scenario(str(FEATURE_FILE), 'Navigate to the About Me page of Sauce Labs')
def test_about_me():
    pass

@when('I press the About link')
def about_link(driver):
    about_section(driver)

@then('I am taken to the About Me page')
def about_me_page(driver):
    expected_url = 'https://saucelabs.com/'
    actual_url = driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, but got: {actual_url}"

def about_section(driver):
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BURGER_MENU)).click()
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ABOUT_BUTTON)).click()

@scenario(str(FEATURE_FILE), 'Purchase a product from the Sauce Labs website')
def test_purchase_product():
    pass

@given('I have added a Sauce Labs product to my basket')
def added_to_basket(driver):
    driver.get("https://www.saucedemo.com/")
    perform_login(driver, 'standard_user', 'secret_sauce')

@when('I complete the payment process')
def payment_process(driver):
    firstname = "John"
    lastname = "Doe"
    postcode = "12345"
    complete_payment(driver, firstname, lastname, postcode)

@then('I have purchased the product')
def about_me_page(driver):
    expected_url = 'https://www.saucedemo.com/checkout-complete.html'
    actual_url = driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, but got: {actual_url}"

def complete_payment(driver, firstname, lastname, postcode):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ADD_PRODUCT)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VIEW_BASKET)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VIEW_CHECKOUT)).click()
    driver.find_element(*FIRST_NAME_FIELD).send_keys(firstname)
    driver.find_element(*LAST_NAME_FIELD).send_keys(lastname)
    driver.find_element(*POSTCODE_FIELD).send_keys(postcode)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CONTINUE_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(FINISH_BUTTON)).click()

@scenario(str(FEATURE_FILE), 'Add a product to my basket before removing it')
def test_empty_basket():
    pass

@given('I have visited Sauce Labs and add product to my basket')
def basket_add(driver):
    driver.get("https://www.saucedemo.com/")
    perform_login(driver, 'standard_user', 'secret_sauce')
    adding_product(driver)

@when('I press the remove button')
def press_remove_button(driver):
    remove_from_basket(driver)

@then('my basket is now empty')
def empty_basket(driver):
    assert not driver.find_elements(By.ID, "REMOVE_BUTTON"), "REMOVE_BUTTON is unexpectedly visible"

def adding_product(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ADD_PRODUCT)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VIEW_BASKET)).click()

def remove_from_basket(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REMOVE_BUTTON)).click()

@scenario(str(FEATURE_FILE), 'Open Sauce Labs Twitter feed')
def test_twitter():
    pass

@when('I select the twitter icon')
def open_twitter(driver ):
    twitter_icon = driver.find_element(By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[1]/a')
    twitter_icon.click()

@then('I am taken to the twitter page')
def verify_new_window_url(driver):  # ignoring context
    original_window = driver.current_window_handle

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    new_window = [w for w in driver.window_handles if w != original_window][0]
    driver.switch_to.window(new_window)

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://x.com/saucelabs")
    )

    assert driver.current_url == "https://x.com/saucelabs", "Incorrect URL opened."
    print("New browser window opened with the correct URL.")

@scenario(str(FEATURE_FILE), 'Open Sauce Labs Facebook feed')
def test_facebook():
    pass

@when('I select the facebook icon')
def open_facebook(driver ):
    facebook_icon = driver.find_element(By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[2]/a')
    facebook_icon.click()

@then('I am taken to the facebook page')
def verify_facebook_window(driver):
    original_window = driver.current_window_handle

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    new_window = [w for w in driver.window_handles if w != original_window][0]
    driver.switch_to.window(new_window)

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.facebook.com/saucelabs")
    )

    assert driver.current_url == "https://www.facebook.com/saucelabs", "Incorrect URL opened."
    print("New browser window opened with the correct URL.")

@scenario(str(FEATURE_FILE), 'Open Sauce Labs Linkedin page')
def test_linkedin():
    pass

@when('I select the Linkedin icon')
def open_linkedin(driver ):
    linkedin_icon = driver.find_element(By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[3]/a')
    linkedin_icon.click()

@then('I am taken to the Linkedin page')
def verify_linkedin_window(driver):
    original_window = driver.current_window_handle

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    new_window = [w for w in driver.window_handles if w != original_window][0]
    driver.switch_to.window(new_window)

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.linkedin.com/company/sauce-labs/")
    )

    assert driver.current_url == "https://www.linkedin.com/company/sauce-labs/", "Incorrect URL opened."
    print("New browser window opened with the correct URL.")