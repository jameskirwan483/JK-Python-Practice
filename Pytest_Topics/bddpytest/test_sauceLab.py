from selenium.webdriver.common.by import By
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
featureFile = 'sauceDemo.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

USERNAME_INPUT_FIELD = (By.ID, 'user-name')
PASSWORD_INPUT_FIELD = (By.ID, 'password')
LOGIN_BUTTON = (By.ID, 'login-button')
ERROR_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
BURGER_MENU = (By.ID,'react-burger-menu-btn')
LOGOUT_BUTTON = (By.XPATH, '//*[@id="logout_sidebar_link"]')

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




