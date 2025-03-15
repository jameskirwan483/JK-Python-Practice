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

@pytest.mark.popup
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

@pytest.mark.popup
@scenario(str(FEATURE_FILE), 'Confirm a close popup')
def test_alerts_popup():
    pass

@given('I navigate to the alerts page')
def alerts_page(driver):
    driver.get("https://practice-automation.com/popups/")

@when('I open the confirm popup')
def open_popup(driver):
    driver.find_element(By.XPATH, '//*[@id="confirm"]').click()
    time.sleep(2)
    alert = Alert(driver)
    alert.accept()
    time.sleep(2)

@then('I close the alert popup')
def alert_popup(driver):
    ok_confirm = driver.find_element(By.XPATH, '//*[@id="confirmResult"]')
    actual_text = ok_confirm.text
    expected_text = "OK it is!"
    assert actual_text == expected_text, f"Text does not match! Expected: '{expected_text}', Got: '{actual_text}'"

@pytest.mark.popup
@scenario(str(FEATURE_FILE), 'Cancel an alert popup')
def test_alerts_popup():
    pass

@given('I navigate to the alerts page')
def alerts_page(driver):
    driver.get("https://practice-automation.com/popups/")

@when('I open the confirm popup but cancel it')
def alert_popup(driver):
        driver.find_element(By.XPATH, '//*[@id="confirm"]').click()
        time.sleep(2)
        alert = Alert(driver)
        alert.dismiss()
        time.sleep(2)

@then('the pop-up has been closed')
def closed_popup(driver):
    cancel_popup = driver.find_element(By.ID, 'confirmResult')
    actual_text = cancel_popup.text
    expected_text = "Cancel it is!"
    assert actual_text == expected_text, f"Text does not match! Expected: '{expected_text}', Got: '{actual_text}'"

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

@scenario(str(FEATURE_FILE), 'Confirm that a file can be uploaded')
def test_upload():
    pass

@given('I want to upload a file')
def file_upload_page(driver):
    driver.get("https://practice-automation.com/file-upload/")

@when('I use the upload functionality')
def find_file(driver):
    file_input = driver.find_element(By.XPATH, '//*[@id="file-upload"]')
    file_path = 'C:/Users/racha_g15xclc/Desktop/test.txt'
    file_input.send_keys(file_path)
    driver.find_element(By.XPATH,'//*[@id="upload-btn"]').click()

@then('the file is successfully uploaded')
def confirm_upload(driver):
    wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds
    upload_message = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="wpcf7-f13587-p1037-o1"]/form/div[2]')))
    actual_text = upload_message.text
    expected_text = "Thank you for your message. It has been sent."
    assert actual_text == expected_text, f"Text does not match! Expected: '{expected_text}', Got: '{actual_text}'"

@scenario(str(FEATURE_FILE), 'Close the on-screen pop up')
def test_pop_up():
    pass

@given('I am viewing a page with a pop-up add')
def pop_up_page(driver):
    driver.get("https://practice-automation.com/ads/")

@when('I press the close button')
def close_pop_up(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popmake-1272"]/button'))).click()

@then('the pop-up add has disappeared')
def pop_up_gone(driver):
    wait = WebDriverWait(driver, 10)
    is_invisible = wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="element-id"]')))
    assert is_invisible, "The element is still visible!"

# @scenario(str(FEATURE_FILE), 'Search for data within a table')
#def test_table():
  #  pass

# @given('I am viewing a page showing a table')
#def table_page(driver):
  #  driver.get("https://practice-automation.com/tables/")

#@when('I am search for the results within a table')
#def data_search(driver):


# @then('the correct results are displayed')
#def correct_results(driver):

@scenario(str(FEATURE_FILE), 'Select a date using the calendar')
def test_table():
  pass

@given('I open the calendar page')
def calendar_page(driver):
    driver.get("https://practice-automation.com/calendars/")

@when('I select a date')
def open_calendar(driver):
    driver.find_element(By.XPATH, '//*[@id="g1065-2-1-selectorenteradate"]').click()
    driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[5]/a').click()
    driver.find_element(By.XPATH, '//*[@id="contact-form-1065-2-1"]/form/p[1]/button').click()

@then('the date is entered into the field')
def date_submitted(driver):
    expected_url = "https://practice-automation.com/calendars/#contact-form-1065-2-1"
    assert driver.current_url == expected_url, f"Expected URL {expected_url}, but got {driver.current_url}"

@scenario(str(FEATURE_FILE), 'Complete the form fields and submit')
def test_form():
  pass

@given('I am on the form completion page')
def completion_page(driver):
    driver.get("https://practice-automation.com/form-fields/")

@when('I complete the mandatory fields')
def mandatory_fields(driver):
    # Locate and fill mandatory fields
    name = driver.find_element(By.XPATH, '//*[@id="name-input"]')
    name.send_keys("Full Name")

    password = driver.find_element(By.XPATH, '//*[@id="feedbackForm"]/label[2]/input')
    password.send_keys("Password")

    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    email.send_keys("mail@mail.com")

    message = driver.find_element(By.XPATH, '//*[@id="message"]')
    message.send_keys("test message")

    # Locate and click the submit button
    submit_button = driver.find_element(By.XPATH, '//*[@id="submit-btn"]')
    # Use JavaScript to ensure the button is clicked even if intercepted
    driver.execute_script("arguments[0].click();", submit_button)


@then('I can submit the form')
def submitted_form(driver):
    try:
        # Wait for the alert pop-up to appear after form submission
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

        # Confirm that the alert is displayed and log its text
        assert alert is not None, "The pop-up alert did not appear after submitting the form."
        alert_text = alert.text
        print(f"Alert Text: {alert_text}")  # Log the alert message

        # OPTIONAL: Assert the alert text content (if expected text is known)
        expected_text = "Message received!"  # Replace with the actual text if applicable
        assert alert_text == expected_text, f"Unexpected alert text: {alert_text}"

        # Dismiss the alert
        alert.accept()
    except Exception as e:
        raise AssertionError(f"Failed to confirm the pop-up alert: {e}")




