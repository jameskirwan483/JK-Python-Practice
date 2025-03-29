from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import pytest
import time

featureFileDir = 'myfeatures'
featureFile = 'demoBlaze.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@scenario(str(FEATURE_FILE), 'Send a message to Demo Blaze using the contact feature')
def test_contact():
    pass

@given('I navigate to the Demo Blaze website')
def demo_blaze_website(driver):
    driver.get('https://www.demoblaze.com/index.html#')

@when('I use the contact option')
def contact_option(driver):
    driver.find_element(By.XPATH,'//*[@id="navbarExample"]/ul/li[2]/a').click()
    driver.find_element(By.ID,'recipient-email').send_keys("test@test.com")
    driver.find_element(By.ID,'recipient-name').send_keys("test")
    driver.find_element(By.ID,'message-text').send_keys("message")
    driver.find_element(By.XPATH,'//*[@id="exampleModal"]/div/div/div[3]/button[2]').click()

@then('the message is successfully sent')
def message_sent(driver):
    alert = driver.switch_to.alert
    expected_text = "Thanks for the message!!"
    assert alert.text == expected_text, f"Unexpected alert text: {alert.text}"
    print("Assertion passed: The alert contains the expected text.")

@scenario(str(FEATURE_FILE), 'Attempt to sign-up to Demo Blaze with email already used')
def test_contact():
    pass

@given('I navigate to the Demo Blaze website')
def demo_blaze_website(driver):
    driver.get('https://www.demoblaze.com/index.html#')

@when('I sign up with an email already used')
def email_signup(driver):
    driver.find_element(By.ID,'signin2').click()
    driver.find_element(By.ID,'sign-username').send_keys("test")
    driver.find_element(By.ID,'sign-password').send_keys("test")
    driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[2]').click()

@then('the sign-up is unsuccessful')
def unsuccessful_signup (driver):
    time.sleep(2)
    alert = driver.switch_to.alert
    expected_text = "This user already exist."
    assert alert.text == expected_text, f"Unexpected alert text: {alert.text}"
    print("Assertion passed: The alert contains the expected text.")