from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pytest
import random
import string
import time
import unittest

featureFileDir = 'myfeatures'
featureFile = 'toolShop.feature'  # Ensure the correct extension
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


def generate_random_string(length):
    letters = string.ascii_letters + string.digits  # Include letters and digits
    return ''.join(random.choice(letters) for i in range(length))

# Fixture to initialize and close WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@scenario(str(FEATURE_FILE), 'Login to Toolshop Website')
def test_login():
    pass

@given('I navigate to the toolshop website')
def click_search_field(driver):
    driver.get("https://practicesoftwaretesting.com/auth/login")

@when('I enter my login details')
def enter_login_details(driver):
    email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_field.send_keys("jameskirwan483@gmail.com")
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("K9g5zn2X!!!")
    login_button = driver.find_element(By.XPATH, '/html/body/app-root/div/app-login/div/div/div/form/div[3]/input')
    login_button.click()

@then('I can log into the toolshop website')
def verify_login(driver):
    WebDriverWait(driver, 10).until(EC.url_to_be("https://practicesoftwaretesting.com/account"))
    actual_url = driver.current_url
    expected_url = "https://practicesoftwaretesting.com/account"
    assert actual_url == expected_url, f"Expected {expected_url}, but got {actual_url}"
    cookies = driver.get_cookies()
    for cookie in cookies:
        print(f"Name: {cookie['name']} - Value: {cookie['value']}")
    return cookies  # Return cookies for use in other steps

@scenario(str(FEATURE_FILE), 'Update users phone number on Toolshop Website')
def test_update_phone():
    pass

@pytest.fixture
def login_and_get_cookies(driver):
    driver.get("https://practicesoftwaretesting.com/auth/login")
    email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_field.send_keys("jameskirwan483@gmail.com")
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("K9g5zn2X!!!")
    login_button = driver.find_element(By.XPATH, '/html/body/app-root/div/app-login/div/div/div/form/div[3]/input')
    login_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://practicesoftwaretesting.com/account"))
    cookies = driver.get_cookies()
    return cookies

@given('I viewing the users profile')
def user_profile(driver, login_and_get_cookies):
    cookies = login_and_get_cookies
    driver.get("https://practicesoftwaretesting.com/auth/login")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://practicesoftwaretesting.com/account")

@when('I enter a new value into the phone number field')
def new_number(driver):
    profile = driver.find_element(By.XPATH, '/html/body/app-root/div/app-overview/div/a[2]')
    profile.click()
    phone = driver.find_element(By.XPATH, '//*[@id="phone"]')
    phone.send_keys("123")
    update_button = driver.find_element(By.XPATH, '/html/body/app-root/div/app-profile/div[1]/form[1]/div[3]/div/button')
    update_button.click()

@then('the phone number is updated')
def update_confirmation(driver):
    actual_url = driver.current_url
    expected_url = "https://practicesoftwaretesting.com/account/profile"
    assert actual_url == expected_url

@scenario(str(FEATURE_FILE), 'Add a product as a favourite')
def test_fav_add(driver):
    pass

@given('I have navigated to a product page')
def logged_in(driver, login_and_get_cookies):
    cookies = login_and_get_cookies
    driver.get("https://practicesoftwaretesting.com/auth/login")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://practicesoftwaretesting.com/product/01JMAVCCD4CV2PE93YXHJ5TC5V")

@when('I click the favourites link')
def click_fav(driver):
    fav_link = driver.find_element(By.XPATH, '//*[@id="btn-add-to-favorites"]')
    fav_link.click()

@then('the product has been added as a favourite')
def fav_added(driver):
    driver.get("https://practicesoftwaretesting.com/account/favorites")
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-favorites/div/div/div/div[2]"))
    )
    partial_text = "Combination Pliers"
    assert partial_text in element.text

@scenario(str(FEATURE_FILE), 'Send a message to tool shop via contact form')
def test_contact(driver):
    pass

@given('I am viewing the contact form')
def logged_in(driver, login_and_get_cookies):
    cookies = login_and_get_cookies
    driver.get("https://practicesoftwaretesting.com/auth/login")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://practicesoftwaretesting.com/contact")

@when('I populate the form details')
def form_details(driver):
    subject = driver.find_element(By.XPATH, '//*[@id="subject"]')
    subject.click()
    dropdown = driver.find_element(By.XPATH, '//*[@id="subject"]/option[2]')
    dropdown.click()
    message = driver.find_element(By.XPATH, '//*[@id="message"]')
    random_message = generate_random_string(50)
    message.send_keys(random_message)
    file_input = driver.find_element(By.XPATH, '//*[@id="attachment"]')
    file_path = "C:/Users/racha_g15xclc/Documents/test.txt"
    file_input.send_keys(file_path)
    send_button = driver.find_element(By.XPATH, '/html/body/app-root/div/app-contact/div/div/div/form/div/div[2]/div[4]/input')
    send_button.click()

@then('I can send the form to tool shop')
def send_form(driver):
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-contact/div/div/div/div'))
    )
    partial_text = "We will contact you shortly."
    assert partial_text in element.text

@scenario(str(FEATURE_FILE), 'Purchase a product')
def test_purchase(driver):
    pass

@given('I have added a product to my basket')
def logged_in(driver, login_and_get_cookies):
    cookies = login_and_get_cookies
    driver.get("https://practicesoftwaretesting.com/auth/login")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://practicesoftwaretesting.com/product/01JMJJJGBZH9PNT074R9CGY92K")

@when('I proceed to checkout')
def checking_out(driver):
    add_to_basket = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-add-to-cart"]'))
    )
    add_to_basket.click()
    time.sleep(10)

    shopping_cart = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[5]/a')
    shopping_cart.click()
    time.sleep(2)

    proceed_to_checkout_button = driver.find_element(By.XPATH,'/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[1]/app-cart/div/div/button')
    proceed_to_checkout_button.click()
    time.sleep(2)

    sign_in_button_checkout = driver.find_element(By.XPATH,'/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[2]/app-login/div/div/div/div/button')
    sign_in_button_checkout.click()
    time.sleep(2)

    billing_address_button = driver.find_element(By.XPATH, '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[3]/app-address/div/div/div/div/button')
    billing_address_button.click()
    time.sleep(2)

    # Select payment method
    payment_dropdown = driver.find_element(By.XPATH, '//*[@id="payment-method"]')
    payment_dropdown.click()
    cash_on_delivery = driver.find_element(By.XPATH, '//*[@id="payment-method"]/option[3]')
    cash_on_delivery.click()
    time.sleep(2)
    confirm_button = driver.find_element(By.XPATH, '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-completion-step/app-payment/div/div/div/div/button')
    confirm_button.click()


@then("I can order the product")
def assert_payment_successful(driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-completion-step/app-payment/div/div/div/form/div[2]/div')) )
    element_text = element.text
    expected_text = "payment was successful"
    assert expected_text in element_text.lower(), f"Expected text '{expected_text}' not found in element text '{element_text}'"