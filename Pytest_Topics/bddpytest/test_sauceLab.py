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

@scenario(str(FEATURE_FILE), 'Login to Sauce Labs with incorrect credentials')
def test_failed_login():
    pass

@given('I am viewing the Sauce Demo homepage')
def sauce_homepage(driver):
    driver.get('https://www.saucedemo.com/')

@when('I attempt to login with incorrect credentials')
def sauce_incorrect_credentials(driver):
    login_username = driver.find_element(By.ID,'user-name')
    login_username.send_keys('Incorrect login')
    login_password = driver.find_element(By.ID,'password')
    login_password.send_keys('Incorrect password')
    login_button = driver.find_element(By.ID,'login-button')
    login_button.click()

@then('I am unable to login to Sauce Demo')
def sauce_incorrect_login(driver):
    error_message = driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]')
    assert "Epic sadface: Username and password do not match any user in this service" in error_message.text, f"Expected 'Cart is empty!', but found '{error_message.text}'"