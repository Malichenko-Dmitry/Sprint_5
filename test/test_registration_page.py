from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import helpers

class Testregistration:

    def test_successful_registration(self, chrome_driver, open_chrome_site):
        open_chrome_site()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        chrome_driver.find_element(*Locators.register).click()
        random_name = helpers.generate_random_string(10)
        random_email = helpers.generate_random_email()
        random_password = helpers.generate_random_password(10)
        WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located(Locators.name_registration)).send_keys(
            random_name)
        WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located(Locators.email_registration)).send_keys(
            random_email)
        WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located(Locators.password_registration)).send_keys(
            random_password)
        WebDriverWait(chrome_driver, 10).until(EC.element_to_be_clickable(Locators.registration_button)).click()
        assert WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located(Locators.personal_account_button)).is_displayed()



    def test_incorrect_password_registration(self, chrome_driver, open_chrome_site):
        open_chrome_site()
        chrome_driver.find_element(*Locators.personal_account_button).click()
        chrome_driver.find_element(*Locators.register).click()
        random_name = helpers.generate_random_string(10)
        random_email = helpers.generate_random_email()
        incorrect_password = '123'
        WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located(Locators.name_registration)).send_keys(
            random_name)
        WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located(Locators.email_registration)).send_keys(
            random_email)
        WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located(Locators.password_registration)).send_keys(
            incorrect_password)
        WebDriverWait(chrome_driver, 10).until(EC.element_to_be_clickable(Locators.registration_button)).click()
        error_message = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located(Locators.incorrect_password))
        assert error_message.is_displayed() and 'Некорректный пароль' in error_message.text


