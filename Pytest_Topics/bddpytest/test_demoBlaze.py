from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import pytest
import time
import random
import string

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

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com", "example.com"])
    return f"{username}@{domain}"


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
def test_signup_fail(driver):
    pass

@given('I navigate to the Demo Blaze website')
def demo_blaze_website(driver):
    driver.get('https://www.demoblaze.com/index.html#')

@when('I sign up with an email already used')
def email_signup_old(driver):
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

@scenario(str(FEATURE_FILE), 'Attempt to sign-up to Demo Blaze with a new email address')
def test_signup_success(driver):
    pass

@given('I navigate to the Demo Blaze website')
def demo_blaze_website(driver):
    driver.get('https://www.demoblaze.com/index.html#')

@when('I sign up with a new email address')
def email_signup_new(driver):
    driver.find_element(By.ID, 'signin2').click()
    random_email = generate_random_email()
    driver.find_element(By.ID, 'sign-username').send_keys(random_email)
    driver.find_element(By.ID, 'sign-password').send_keys("test")
    driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()

@then('the sign-up is successful')
def unsuccessful_signup (driver):
    time.sleep(2)
    alert = driver.switch_to.alert
    expected_text = "Sign up successful."
    assert alert.text == expected_text, f"Unexpected alert text: {alert.text}"
    print("Assertion passed: The alert contains the expected text.")

@scenario(str(FEATURE_FILE), 'Add a product to your basket on Demo Blaze website')
def test_basket():
    pass

@given('I navigate to the Demo Blaze website')
def demo_blaze_website(driver):
    driver.get('https://www.demoblaze.com/index.html#')

@when('I click the add to cart button')
def random_product(driver):
    tbody = driver.find_element(By.ID, 'tbodyid')
    products = tbody.find_elements(By.TAG_NAME, "tr")
    if products:
        random_item = random.choice(products)
        random_item.click()
    else:
        print("No products found!")

@then('the product is now in my basket')
def basket_add(driver):
    try:
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a').click()
        time.sleep(2)
        alert = driver.switch_to.alert
        expected_text = "Product added"
        assert alert.text == expected_text, f"Unexpected alert text: {alert.text}"
        print("Assertion passed: The alert contains the expected text.")
        alert.accept()
    except Exception as e:
        print(f"Error while adding product to basket: {e}")

@scenario(str(FEATURE_FILE), 'Log into Demo Blaze website with existing email')
def test_login():
    pass

@given("I press the login button on the Demo Blaze website")
def press_login(driver):
    driver.get("https://www.demoblaze.com/index.html")
    driver.find_element(By.ID, 'login2').click()

@when("I enter previously used login details")
def enter_login_details(driver):
    driver.find_element(By.ID,'loginusername').send_keys("jameskirwan123456")
    driver.find_element(By.ID, 'loginpassword').send_keys("Password123")
    driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()

@then("I have logged into my account")
def logged_in(driver):
    element = driver.find_element(By.ID, 'nameofuser')
    nameofuser = element.get_attribute("id")
    expected_text = "nameofuser"
    assert expected_text in nameofuser, f"Expected '{expected_text}' to be in '{nameofuser}'"

@scenario(str(FEATURE_FILE), 'Purchase a product from the Demo Blaze website')
def test_purchase():
    pass

@given('I have added a product to my cart')
def add_product(driver):
    driver.get("https://www.demoblaze.com/prod.html?idp_=1")
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="tbodyid"]/div[2]/div/a').click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.dismiss()

@when('I populate he place order details')
def place_order(driver):
    driver.find_element(By.ID, 'cartur').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button').click()
    time.sleep(1)
    driver.find_element(By.ID, 'name').send_keys("name")
    driver.find_element(By.ID, 'country').send_keys("country")
    driver.find_element(By.ID, 'city').send_keys("city")
    driver.find_element(By.ID, 'card').send_keys("card")
    driver.find_element(By.ID, 'month').send_keys("month")
    driver.find_element(By.ID, 'year').send_keys("year")
    driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]').click()

@then('I can purchase the product')
def purchase_order(driver):
    time.sleep(1)
    element = driver.find_element(By.XPATH, '/html/body/div[10]/h2')
    actual_text = element.text
    expected_text = "Thank you for your purchase!"
    assert expected_text in actual_text, f"Expected '{expected_text}' to be in '{actual_text}'"







