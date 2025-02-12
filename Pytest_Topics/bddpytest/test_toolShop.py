from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pathlib import Path
import pytest
import time

featureFileDir = 'myfeatures'
featureFile = 'toolShop.feature'  # Ensure the correct extension
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

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