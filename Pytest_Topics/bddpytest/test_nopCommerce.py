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
featureFile = 'nopCommerce.feature'  # Ensure the correct extension
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

# Fixture to initialize and close WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def register_user():
    def _register(driver):
        element = driver.find_element(By.XPATH, '//*[@id="customer.firstName"]')
        element.send_keys("First Name")
        element = driver.find_element(By.XPATH, '//*[@id="customer.lastName"]')
        element.send_keys("Last Name")
        element = driver.find_element(By.XPATH, '//*[@id="customer.address.street"]')
        element.send_keys("Street Name")
        element = driver.find_element(By.XPATH, '//*[@id="customer.address.city"]')
        element.send_keys("City Name")
        element = driver.find_element(By.XPATH, '//*[@id="customer.address.state"]')
        element.send_keys("State Name")
        element = driver.find_element(By.XPATH, '//*[@id="customer.address.zipCode"]')
        element.send_keys("Zip Code")
        element = driver.find_element(By.XPATH, '//*[@id="customer.phoneNumber"]')
        element.send_keys("123456789")
        element = driver.find_element(By.XPATH, '//*[@id="customer.ssn"]')
        element.send_keys("123456789")
        element = driver.find_element(By.XPATH, '//*[@id="customer.username"]')
        unique_username = f"username{int(time.time())}"
        element.send_keys(unique_username)
        element = driver.find_element(By.XPATH, '//*[@id="customer.password"]')
        element.send_keys("password")
        element = driver.find_element(By.XPATH, '//*[@id="repeatedPassword"]')
        element.send_keys("password")
        element = driver.find_element(By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input')
        element.click()
    return _register

@scenario(str(FEATURE_FILE), 'Open website and navigate to the Locations page')
def test_location():
    pass

@given('I want to search for Parabank locations')
def click_search_field(driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

@when('I click the locations link')
def click_locations(driver):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[5]/a')))
    element.click()

@then('I am taken to the locations page')
def location_page(driver):
    expected_title = "Automated Software Testing Solutions For Every Testing Need"
    actual_title = driver.title
    assert expected_title == actual_title, f"Expected title: {expected_title}, but got: {actual_title}"


@scenario(str(FEATURE_FILE), 'Open website and navigate to the Products page')
def test_product():
    pass

@given('I want to search for Parabank products')
def click_search_field(driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

@when('I click the products link')
def click_locations(driver):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[4]/a')))
    element.click()

@then('I am taken to the Products page')
def product_page(driver):
    expected_title = "Automated Software Testing Tools - Ensure Quality - Parasoft"
    actual_title = driver.title
    assert expected_title == actual_title, f"Expected title: {expected_title}, but got: {actual_title}"

@scenario(str(FEATURE_FILE), 'Send an email to Parabank via customer care')
def test_customer_care():
    pass

@given('I navigate to the Parabank contact page')
def click_search_field(driver):
    driver.get("https://parabank.parasoft.com/parabank/contact.htm")

@when('I complete the form customer care form')
def customer_care_form(driver):
    element = driver.find_element(By.XPATH, '//*[@id="name"]')
    element.send_keys("Name")
    element = driver.find_element(By.XPATH, '//*[@id="email"]')
    element.send_keys("test@email.com")
    element = driver.find_element(By.XPATH, '//*[@id="phone"]')
    element.send_keys("123456789")
    element = driver.find_element(By.XPATH, '//*[@id="message"]')
    element.send_keys("please help")
    element = driver.find_element(By.XPATH, '//*[@id="contactForm"]/table/tbody/tr[5]/td[2]/input')
    element.click()

@then('It is sent to the customer care team')
def form_completed(driver):
    element = driver.find_element(By.XPATH, '//*[@id="rightPanel"]/p[2]')
    actual_text = element.text
    expected_text = "A Customer Care Representative will be contacting you."
    assert actual_text == expected_text, f"Expected text: {expected_text}, but got: {actual_text}"

@scenario(str(FEATURE_FILE), 'Register for the Parabank website')
def test_registration():
    pass

@given('I navigate to the Parabank registration page')
def click_registration(driver):
    driver.get("https://parabank.parasoft.com/parabank/register.htm")

@when('I complete the registration form')
def registration_completion(driver, register_user):
    register_user(driver)

@then('I can register for the Parabank website')
def form_completed(driver):
    element = driver.find_element(By.XPATH, '//*[@id="rightPanel"]/p')
    actual_text = element.text
    expected_text = "Your account was created successfully. You are now logged in."
    assert actual_text == expected_text, f"Expected text: {expected_text}, but got: {actual_text}"
    if hasattr(pytest, 'cookiedata'):
        for cookie in pytest.cookiedata:
            driver.add_cookie(cookie)

@scenario(str(FEATURE_FILE), 'Log out of website')
def test_logout():
    pass

@given('I am logged into the website')
def logged_in(driver, register_user):
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    register_user(driver)

@when('I click the logout link')
def click_logout_link(driver):
    element = driver.find_element(By.XPATH, '//*[@id="leftPanel"]/ul/li[8]/a')
    element.click()

@then('I am successfully logged out')
def logged_out(driver):
    expected_title = "ParaBank | Welcome | Online Banking"
    actual_title = driver.title
    assert expected_title == actual_title, f"Expected title: {expected_title}, but got: {actual_title}"

@scenario(str(FEATURE_FILE), 'Applying for a loan')
def test_loan_apply():
    pass

@given('I am logged into the website')
def logged_in(driver, register_user):
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    register_user(driver)

@when('I populate the loan request details')
def loan_request(driver):
    element = driver.find_element(By.XPATH, '//*[@id="leftPanel"]/ul/li[7]/a')
    element.click()
    element = driver.find_element(By.XPATH, '//*[@id="amount"]')
    element.send_keys("1")
    element = driver.find_element(By.XPATH, '//*[@id="downPayment"]')
    element.send_keys("2")
    element = driver.find_element(By.XPATH, '//*[@id="requestLoanForm"]/form/table/tbody/tr[4]/td[2]/input')
    element.click()

@then('my loan request has been processed')
def loan_processed(driver):
    expected_title = "ParaBank | Loan Request"
    actual_title = driver.title
    assert expected_title == actual_title, f"Expected title: {expected_title}, but got: {actual_title}"

@scenario(str(FEATURE_FILE), 'Transfer funds to pay a bill')
def test_transfer_funds():
    pass

@given('I am logged into Robobank website')
def logged_in(driver, register_user):
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    register_user(driver)

@when('I select the transfer funds link')
def transfer_funds(driver):
    element = driver.find_element(By.XPATH, '//*[@id="leftPanel"]/ul/li[3]/a')
    element.click()
    element = driver.find_element(By.XPATH, '//*[@id="amount"]')
    element.send_keys("1")
    element = driver.find_element(By.XPATH, '//*[@id="transferForm"]/div[2]/input')
    element.click()

@then('I can transfer funds between accounts')
def funds_transferred(driver):
    element = driver.find_element(By.XPATH, '//*[@id="showResult"]')
    actual_text = element.text
    expected_text = ""
    assert actual_text == expected_text, f"Expected text: {expected_text}, but got: {actual_text}"

@scenario(str(FEATURE_FILE), 'Open a Savings Account')
def test_march_transactions():
    pass

@given('I have logged into Robobank website')
def logged_in(driver, register_user):
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    register_user(driver)

@when('I select the new account option')
def account_activity(driver):
    # Click on the account activity menu
    element = driver.find_element(By.XPATH, '//*[@id="leftPanel"]/ul/li[1]/a')
    element.click()

    # Wait until the month dropdown is visible
    dropdown_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="type"]'))
    )

    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("SAVINGS")

    # Wait until the submit button is clickable, then click it to apply filter
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="openAccountForm"]/form/div/input'))
    )
    element.click()

@then('I can open a savings account')
def no_transaction(driver):
    element = driver.find_element(By.XPATH, '//*[@id="newAccountId"]')
    element_id = element.get_attribute("id")
    expected_id = "newAccountId"
    assert element_id == expected_id

@scenario(str(FEATURE_FILE), 'Pay my bill')
def test_march_transactions():
    pass

@given('I have logged into Robobank website')
def logged_in(driver, register_user):
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    register_user(driver)

@when ('I fill out the online form')
def bill_form(driver):
    element = driver.find_element(By.XPATH, '//*[@id="leftPanel"]/ul/li[4]/a')
    element.click()
    element = driver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[1]/td[2]/input')
    element.send_keys("Payee Name")
    element = driver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[2]/td[2]/input')
    element.send_keys("Address")
    element = driver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[3]/td[2]/input')
    element.send_keys("City")
    element = driver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[4]/td[2]/input')
    element.send_keys("State")
    element = driver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[5]/td[2]/input')
    element.send_keys("Zip Code")
    element = driver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[6]/td[2]/input')
    element.send_keys("Phone")
    element = driver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[8]/td[2]/input')
    element.send_keys("Account")
    element = driver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[9]/td[2]/input')
    element.send_keys("Account")
    element = driver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[11]/td[2]/input')
    element.send_keys("123")
    element = driver.find_element(By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[14]/td[2]/input')
    element.click()

@then ('I can pay the bill online')
def bill_paid(driver):
    expected_title = "ParaBank | Bill Pay"
    actual_title = driver.title
    assert expected_title == actual_title, f"Expected title: {expected_title}, but got: {actual_title}"


@scenario(str(FEATURE_FILE), 'Update my profile')
def test_update_profile():
    pass

@given('I have logged into Robobank website')
def logged_in(driver, register_user):
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    register_user(driver)

@when('I fill out the update profile section')
def profile_form(driver):
    element = driver.find_element(By.XPATH, '//*[@id="leftPanel"]/ul/li[6]/a')
    element.click()
    element = driver.find_element(By.XPATH, '//*[@id="customer.firstName"]')
    element.send_keys("Update First Name")
    element = driver.find_element(By.XPATH, '//*[@id="customer.lastName"]')
    element.send_keys("Update Last Name")
    element = driver.find_element(By.XPATH, '//*[@id="customer.address.street"]')
    element.send_keys("New Street Name")
    element = driver.find_element(By.XPATH, '//*[@id="customer.address.city"]')
    element.send_keys("New Address Name")
    element = driver.find_element(By.XPATH, '//*[@id="customer.address.state"]')
    element.send_keys("New State")
    element = driver.find_element(By.XPATH, '//*[@id="customer.address.zipCode"]')
    element.send_keys("New Zip")
    element = driver.find_element(By.XPATH, '//*[@id="customer.phoneNumber"]')
    element.send_keys("111222333")
    element = driver.find_element(By.XPATH, '//*[@id="updateProfileForm"]/form/table/tbody/tr[8]/td[2]/input')
    element.click()

@then ('my profile is successfully updated')
def profile_updated (driver):
    element = driver.find_element(By.XPATH, '//*[@id="updateProfileResult"]')
    element_id = element.get_attribute("id")
    expected_id = "updateProfileResult"
    assert element_id == expected_id





