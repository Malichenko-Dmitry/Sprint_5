from locators import Locators
from data import TestData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Testpersonalaccount:

    def test_login_and_check_name(self, chrome_driver, open_chrome_site):

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



    def test_login_and_navigate_to_constructor(self, chrome_driver, open_chrome_site):

        open_chrome_site()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        chrome_driver.find_element(*Locators.field_email).send_keys(TestData.email)
        chrome_driver.find_element(*Locators.password_field).send_keys(TestData.password)
        chrome_driver.find_element(*Locators.personal_account_button).click()
        chrome_driver.find_element(*Locators.constructor).click()
        current_url = chrome_driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url


    def test_navigate_to_constructor_via_logo(self, chrome_driver, open_chrome_site):

        open_chrome_site()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        chrome_driver.find_element(*Locators.field_email).send_keys(TestData.email)
        chrome_driver.find_element(*Locators.password_field).send_keys(TestData.password)
        chrome_driver.find_element(*Locators.personal_account_button).click()
        chrome_driver.find_element(*Locators.stellar_burgers_logo).click()
        current_url = chrome_driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url


    def test_logout(self, chrome_driver, open_chrome_site):

        open_chrome_site()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        chrome_driver.find_element(*Locators.field_email).send_keys(TestData.email)
        chrome_driver.find_element(*Locators.password_field).send_keys(TestData.password)
        chrome_driver.find_element(*Locators.login_button).click()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.exit_button)
        ).click()
        WebDriverWait(chrome_driver, 20).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
        current_url = chrome_driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/login"
        assert current_url == expected_url

