from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers
from data import TestData

class Testloginpage:

    def test_login_via_main_page(self, chrome_driver, open_chrome_site):
        open_chrome_site()
        chrome_driver.find_element(*Locators.account_login_button).click()
        chrome_driver.find_element(*Locators.field_email).send_keys(TestData.email)
        chrome_driver.find_element(*Locators.password_field).send_keys(TestData.password)
        chrome_driver.find_element(*Locators.login_button).click()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.field_name)
        )
        name = chrome_driver.find_element(*Locators.field_name)
        assert name.get_attribute('value') == TestData.name


    def test_login_via_personal_account_button(self, chrome_driver, open_chrome_site):
        open_chrome_site()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        chrome_driver.find_element(*Locators.field_email).send_keys(TestData.email)
        chrome_driver.find_element(*Locators.password_field).send_keys(TestData.password)
        chrome_driver.find_element(*Locators.login_button).click()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.field_name)
        )
        name = chrome_driver.find_element(*Locators.field_name)
        assert name.get_attribute('value') == TestData.name


    def test_registration_and_login(self, chrome_driver, open_chrome_site):

        open_chrome_site()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        chrome_driver.find_element(*Locators.register).click()
        random_name = helpers.generate_random_string()
        random_email = f"{helpers.generate_random_string()}@example.com"
        random_password = helpers.generate_random_string(length=12)
        chrome_driver.find_element(*Locators.name_registration).send_keys(random_name)
        chrome_driver.find_element(*Locators.email_registration).send_keys(random_email)
        chrome_driver.find_element(*Locators.password_registration).send_keys(random_password)
        chrome_driver.find_element(*Locators.registration_button).click()
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.login_button)
        )
        chrome_driver.find_element(*Locators.field_email).send_keys(
            random_email)
        chrome_driver.find_element(*Locators.password_field).send_keys(
            random_password)
        chrome_driver.find_element(*Locators.login_button).click()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.field_name)
        )
        name = chrome_driver.find_element(*Locators.field_name)
        assert name.get_attribute('value') == random_name


    def test_password_recovery(self, chrome_driver, open_chrome_site):
        open_chrome_site()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        recovery_link = chrome_driver.find_element(*Locators.password_recovery)
        recovery_link.click()
        email_input = chrome_driver.find_element(*Locators.email_password_recovery)
        email_input.send_keys(TestData.email)
        recovery_button = chrome_driver.find_element(*Locators.recover_button)
        recovery_button.click()
        WebDriverWait(chrome_driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/reset-password")
        )
        current_url = chrome_driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/reset-password"
        assert current_url == expected_url

