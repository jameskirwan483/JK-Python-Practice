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

featureFileDir = 'myfeatures'
featureFile = 'automationExercise.feature'  # Ensure the correct extension
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

# Fixture to initialize and close WebDriver
@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@scenario(str(FEATURE_FILE), 'Register User on Automation Exercise Website')
def test_registraton():
    pass


@given('I have opened the automation practice website')
def automation_practice(driver):
    driver.get('https://www.automationexercise.com/login')

    try:
        # Wait for the pop-up to become visible before interacting
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )

        # Click the consent button
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")


@when('I use the registration functionality')
def registration(driver):
    unique_id = uuid.uuid4().hex[:8]
    email = f"user_{unique_id}@testmail.com"
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys("jkirwan")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button').click()
    time.sleep(2)
    driver.find_element(By.ID, 'id_gender2').click()
    driver.find_element(By.ID, 'password').send_keys('Password123')
    driver.find_element(By.ID, 'id_gender1').click()
    driver.find_element(By.ID, 'password').send_keys('Password123')
    dropdown = driver.find_element(By.ID, 'days')
    select = Select(dropdown)
    select.select_by_index(10)
    dropdown = driver.find_element(By.ID, 'months')
    select = Select(dropdown)
    select.select_by_index(10)
    dropdown = driver.find_element(By.ID, 'years')
    select = Select(dropdown)
    select.select_by_index(30)
    time.sleep(2)
    driver.find_element(By.ID, 'first_name').send_keys('test')
    driver.find_element(By.ID, 'last_name').send_keys('test')
    driver.find_element(By.ID, 'address1').send_keys('test')
    driver.find_element(By.ID, 'state').send_keys('test')
    driver.find_element(By.ID, 'city').send_keys('test')
    driver.find_element(By.ID, 'zipcode').send_keys('test')
    driver.find_element(By.ID, 'mobile_number').send_keys('123456789')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button').click()

@then('I have registered as a website user')
def registered_user(driver):
    expected_url = "https://www.automationexercise.com/account_created"
    assert driver.current_url == expected_url, f"Expected '{expected_url}', but got '{driver.current_url}'"

@scenario(str(FEATURE_FILE), 'Log into Automation Exercise with existing credentials')
def test_login():
    pass

@given('I want to log into the automation exercise website')
def automation_practice(driver):
    driver.get('https://www.automationexercise.com/login')

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when('I enter my login credentials')
def login_credentials(driver):
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys('jameskirwan483@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys('K9g5zn2X!')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()

@then('I have logged into the website')
def logged_in(driver):
    logout_element = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    assert "Logout" in logout_element.text, "Logout link text is missing or incorrect"

@scenario(str(FEATURE_FILE), 'Log into Automation Exercise with incorrect credentials')
def test_login_incorrect():
    pass

@given('I want to log into the automation exercise website')
def automation_practice(driver):
    driver.get('https://www.automationexercise.com/login')

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when('I enter incorrect login credentials')
def login_credentials(driver):
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys('jameskirwan483@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys('password')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()

@then('I am unable to log into the website')
def cant_login(driver):
    element = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/p')
    expected_text = "Your email or password is incorrect!"
    assert expected_text in element.text, f"Expected '{expected_text}', but found '{element.text}'"

@scenario(str(FEATURE_FILE), 'Verify Test Cases Page')
def test_page_verification():
    pass

@given('I have opened the automation practice website')
def automation_practice(driver):
    driver.get('https://www.automationexercise.com/')

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        )
        consent_button.click()

    except Exception as e:
        print(f"Cookie pop-up not interactable: {e}")

@when('I click the test cases button')
def test_cases_button(driver):
    driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a').click()

@then('I have navigated to the test cases page')
def test_case_page(driver):
    expected_url = "https://www.automationexercise.com/test_cases"
    actual_url = driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, but got {actual_url}"

