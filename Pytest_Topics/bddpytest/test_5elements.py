from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pytest
from selenium.webdriver.chrome.options import Options

featureFileDir = 'myfeatures'
featureFile = '5elements.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-blink-features=PasswordManagerDetection")
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerEnabled")
    options.add_argument("--incognito")  # Optional: avoids stored passwords
    options.add_argument("--user-data-dir=/tmp/test-profile")
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    yield driver
    driver.quit()
