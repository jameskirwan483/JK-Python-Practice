import time

from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pytest
from selenium.webdriver.chrome.options import Options

featureFileDir = 'myfeatures'
featureFile = '5elements.feature'
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

@scenario(str(FEATURE_FILE), 'Open the 5elements website and navigate to the Shipping page')
def test_shipping_page():
    pass

@given("I have opened the 5elements website")
def open_5elements(driver):
    driver.get("https://5elementslearning.dev/demosite/index.php")

@when("I click the Shipping & Returns link")
def click_shipping_link(driver):
    shipping_link = driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[5]/div[2]/a[1]')
    shipping_link.click()

@then("I am taken to the Shipping page")
def verify_shipping_url(driver):
    assert "5elementslearning.dev/demosite/shipping" in driver.current_url, "Expected URL part is not found."

@scenario(str(FEATURE_FILE), 'Open the 5elements website and navigate to the Privacy Notice page')
def test_privacy_page():
    pass

@when("I click the Privacy Notice link")
def click_privacy_link(driver):
    privacy_link = driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[5]/div[2]/a[2]')
    privacy_link.click()

@then("I am taken to the Privacy Notice page")
def verify_privacy_url(driver):
    conditions_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="bodyContent"]/h1'))
    )
    assert "Privacy Notice" in conditions_element.text, "Expected text not found in element."

    print("Assertion passed: The element contains Privacy Notice'.")

@scenario(str(FEATURE_FILE), 'Open the 5elements website and navigate to the Conditions of Use page')
def test_conditions_page():
    pass

@when("I click the Conditions of Use page")
def click_conditions(driver):
    conditions_link = driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[5]/div[2]/a[3]')
    conditions_link.click()

@then("I am taken to the Conditions of Use page")
def verify_conditions_url(driver):
    assert "5elementslearning.dev/demosite/conditions" in driver.current_url, "Expected URL part is not found."

@scenario(str(FEATURE_FILE), 'Open the 5elements website and navigate to the Contact Us page')
def test_contact_page():
    pass

@when("I click the Contact Us link")
def click_conditions(driver):
    contacts_link = driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[5]/div[2]/a[4]')
    contacts_link.click()

@then("I am taken to the Contact Us page")
def verify_contact_url(driver):
    assert "5elementslearning.dev/demosite/contact_us" in driver.current_url, "Expected URL part is not found."

@scenario(str(FEATURE_FILE), 'Send a message to store owner using contact field')
def test_contact_page():
    pass

@given("I am viewing the Contact Us page")
def open_contact(driver):
    driver.get("https://5elementslearning.dev/demosite/contact_us.php")

@when("I populate all the fields in the message box")
def populate_all_fields(driver):
    full_name_field = driver.find_element(By.NAME, 'name')
    full_name_field.send_keys("Test Name")
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys("test1@test.com")
    enquiry_field = driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[1]/table/tbody/tr[3]/td[2]/textarea')
    enquiry_field.send_keys("test")
    continue_button = driver.find_element(By.XPATH, '//*[@id="tdb4"]/span[2]')
    continue_button.click()

@then("my message is sent to the Store Owner")
def message_send(driver):
    confirmation_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="bodyContent"]/div/div[1]'))
    )
    assert "Your enquiry has been successfully sent to the Store Owner." in confirmation_element.text, \
        "Expected confirmation message not found."

    print("Assertion passed: The confirmation message is displayed correctly.")

@scenario(str(FEATURE_FILE), 'Confirm that only 1 message can be sent every 15 minutes')
def test_contact_limit():
    pass

@when("I submit a message within 15 minutes")
def message_submit(driver):
    time.sleep(1)
    full_name_field = driver.find_element(By.NAME, 'name')
    full_name_field.send_keys("Test Name")
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys("test1@test.com")
    enquiry_field = driver.find_element(By.XPATH,'//*[@id="bodyContent"]/form/div/div[1]/table/tbody/tr[3]/td[2]/textarea')
    enquiry_field.send_keys("test")
    continue_button = driver.find_element(By.XPATH, '//*[@id="tdb4"]/span[2]')
    continue_button.click()

@then("an error message is displayed")
def error_message(driver):
    error_message = driver.find_element(By.XPATH, '//*[@id="bodyContent"]/table/tbody/tr/td')
    assert " Error: An enquiry has already been sent. Please try again in 15 minutes." in error_message.text, \
        "Expected confirmation message not found."
