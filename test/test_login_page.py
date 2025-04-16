import time
from selenium import webdriver
from locators import Locators
import helpers

def test_login_via_main_page():
    driver = webdriver.Chrome()
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.implicitly_wait(10)
        driver.find_element(*Locators.account_login_button).click()
        driver.find_element(*Locators.field_email).send_keys("dima199768@gmail.com")
        driver.find_element(*Locators.password_field).send_keys("123456789")
        driver.find_element(*Locators.login_button).click()

    finally:
        driver.quit()


def test_login_via_personal_account_button():
    driver = webdriver.Chrome()
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.implicitly_wait(10)
        driver.find_element(*Locators.personal_account_button).click()
        driver.find_element(*Locators.field_email).send_keys("dima199768@gmail.com")
        driver.find_element(*Locators.password_field).send_keys("123456789")
        driver.find_element(*Locators.login_button).click()

    finally:
        driver.quit()


def test_registration_and_login():
    driver = webdriver.Chrome()
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.implicitly_wait(10)
        driver.find_element(*Locators.personal_account_button).click()
        driver.find_element(*Locators.register).click()
        random_name = helpers.generate_random_string()
        random_email = f"{helpers.generate_random_string()}@example.com"
        random_password = helpers.generate_random_string(length=12)
        driver.find_element(*Locators.name_registration).send_keys(random_name)
        driver.find_element(*Locators.email_registration).send_keys(random_email)
        driver.find_element(*Locators.password_registration).send_keys(random_password)
        driver.find_element(*Locators.registration_button).click()
        time.sleep(4)

    finally:
        driver.quit()


def test_password_recovery():
    driver = webdriver.Chrome()
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.implicitly_wait(10)
        driver.find_element(*Locators.personal_account_button).click()
        recovery_link = driver.find_element(*Locators.password_recovery)
        recovery_link.click()
        email_input = driver.find_element(*Locators.email_password_recovery)
        email_input.send_keys("dima199768@gmail.com")
        recovery_button = driver.find_element(*Locators.recover_button)
        recovery_button.click()
        time.sleep(4)
        assert "/reset-password" in driver.current_url

    finally:
        driver.quit()
