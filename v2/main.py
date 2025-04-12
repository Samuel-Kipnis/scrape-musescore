from start_driver import start_driver
import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    load_dotenv()
    driver = start_driver()
    # login(driver)

    time.sleep(1)  # Wait to confirm login or observe


if __name__ == "__main__":
    main()


def login(driver):
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    LOGIN_URL = "https://musescore.com/user/login"

    driver.get(LOGIN_URL)
    time.sleep(1)  # Let the page load

    # Locate and fill in the login form (adjust these selectors as needed)
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)

    time.sleep(1)  # Wait to confirm login or observe
