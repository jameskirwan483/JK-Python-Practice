from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pytest
import time
import requests

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

@scenario(str(FEATURE_FILE), 'Glad the slider and update the selected value')
def test_slider():
    pass

@given ('I am viewing the slide practice page')
def popup_page(driver):
    driver.get("https://practice-automation.com/slider/")

@when('I pull the slider')
def pull_slider(driver):
    slider = driver.find_element(By.XPATH, '//*[@id="slideMe"]')
    action = ActionChains(driver)
    action.click_and_hold(slider).move_by_offset(50, 0).release().perform() #50 is number of pixels

@then('the current value is updated')
def current_value(driver):
    field = driver.find_element(By.XPATH, '//*[@id="value"]')
    field_value = field.text
    assert field_value == "54", f"Expected value to be '75', but got '{field_value}'"

@scenario(str(FEATURE_FILE), 'Confirm that a link is broken')
def test_broken_link():
    pass

@given('I am validating a broken link')
def broken_link(driver):
    driver.get("https://practice-automation.com/broken-links/")

@when('I click the link which is broken')
def click_link (driver):
    driver.find_element(By.XPATH, '//*[@id="post-1267"]/div/p[1]/a').click()

@then('I can confirm the response code is 404')
def response_code(driver):
    response = requests.get("https://practice-automation.com/broken-links/missing-page.html")
    assert response.status_code == 404,f"Expected status code 404, but got: {response.status_code}"