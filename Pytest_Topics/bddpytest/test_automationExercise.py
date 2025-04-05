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
featureFile = 'automationExercise.feature'  # Ensure the correct extension
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

# Fixture to initialize and close WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@scenario(str(FEATURE_FILE), 'Register User on Automation Exercise Website ')
def test_registraton():
    pass

@given('I have opened the automation practice website')
def automation_practice(driver):
    driver.get('https://www.automationexercise.com/login')

@when('I use the registration functionality')
def registration(driver):
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys("jkirwan.testing@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys("password")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()
    time.sleep(2)
    driver.find_element(By.ID, 'id_gender2').click()
    driver.find_element(By.ID, 'password').send_keys('Password123')

@then('I have registered as a website user')
def registered_user(driver):
