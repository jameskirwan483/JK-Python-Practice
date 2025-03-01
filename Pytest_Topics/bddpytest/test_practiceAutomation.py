from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pytest
import time

featureFileDir = 'myfeatures'
featureFile = 'practiceAutomation.feature'  # Ensure the correct extension
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def automation_url():
    return "https://practice-automation.com/"

@scenario(str(FEATURE_FILE), 'Close an alert popup')
def test_close_popup():
    pass

@given('I navigate to the alerts page')
def alerts_page(driver):
    driver.get("https://practice-automation.com/popups/")

@when('I open the alert popup')
def open_popup(driver):
    driver.find_element(By.XPATH, '//*[@id="alert"]').click()
    time.sleep(2)

@then('I can close the popup')
def close_popup(driver):
    alert = Alert(driver)
    alert.accept()
    time.sleep(2)
    try:
        alert = Alert(driver)
        alert.text
        assert False, "Alert did not disappear!"
    except Exception:
        print("Alert successfully closed and no longer present.")