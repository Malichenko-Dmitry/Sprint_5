from locators import Locators
import helpers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Testconstructor:

    def test_bun_section(self, chrome_driver, open_chrome_site):

        open_chrome_site()
        helpers.click_element(chrome_driver, Locators.constructor)
        helpers.click_element(chrome_driver, Locators.section_sauces)
        helpers.click_element(chrome_driver, Locators.bun_section)
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.active_bun_section)
        )
        element = chrome_driver.find_element(*Locators.active_bun_section)
        assert 'tab_tab_type_current__2BEPc' in element.get_attribute('class')


    def test_sauce_section(self, chrome_driver, open_chrome_site):
        open_chrome_site()
        helpers.click_element(chrome_driver, Locators.constructor)
        helpers.click_element(chrome_driver, Locators.section_sauces)
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.active_section_sauces)
        )
        element = chrome_driver.find_element(*Locators.active_section_sauces)
        assert 'tab_tab_type_current__2BEPc' in element.get_attribute('class')



    def test_fillings_section(self, chrome_driver, open_chrome_site):

        open_chrome_site()
        helpers.click_element(chrome_driver, Locators.constructor)
        helpers.click_element(chrome_driver, Locators.filling_section)
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.active_filling_section)
        )
        element = chrome_driver.find_element(*Locators.active_filling_section)
        assert 'tab_tab_type_current__2BEPc' in element.get_attribute('class')

