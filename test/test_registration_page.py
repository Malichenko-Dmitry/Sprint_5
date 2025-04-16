import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import helpers


def test_successful_registration():
    driver = webdriver.Chrome()
    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")
        random_name = helpers.generate_random_string(10)
        random_email = helpers.generate_random_email()
        random_password = helpers.generate_random_password(10)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.name_registration)).send_keys(
            random_name)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_registration)).send_keys(
            random_email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.password_registration)).send_keys(
            random_password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.registration_button)).click()

        time.sleep(4)
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.personal_account_button)).is_displayed()

    finally:
        driver.quit()


def test_incorrect_password_registration():
    driver = webdriver.Chrome()
    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")
        random_name = helpers.generate_random_string(10)
        random_email = helpers.generate_random_email()
        incorrect_password = '123'

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.name_registration)).send_keys(
            random_name)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_registration)).send_keys(
            random_email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.password_registration)).send_keys(
            incorrect_password)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.registration_button)).click()
        time.sleep(4)
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.incorrect_password))
        assert error_message.is_displayed() and 'Некорректный пароль' in error_message.text

    finally:
        driver.quit()

