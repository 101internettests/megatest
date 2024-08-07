import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
# from config import bot, chat_id, daily

load_dotenv()


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    if os.getenv("HEADLESS") == "True":
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    # driver.maximize_window()
    yield driver
    driver.quit()
