from locators import Locators
import helpers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Testconstructor:

    def test_bun_section(self, chrome_driver, open_chrome_site):

        open_chrome_site()
        helpers.click_element(chrome_driver, Locators.constructor)
        helpers.click_element(chrome_driver, Locators.bun_section)
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.fluorescent_bun)
        )
        assert 'Флюоресцентная булка R2-D3' in chrome_driver.page_source


    def test_sauce_section(self, chrome_driver, open_chrome_site):

        open_chrome_site()
        helpers.click_element(chrome_driver, Locators.constructor)
        helpers.click_element(chrome_driver, Locators.section_sauces)
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.spicy_x)
        )
        assert 'Соус Spicy-X' in chrome_driver.page_source



    def test_fillings_section(self, chrome_driver, open_chrome_site):

        open_chrome_site()
        helpers.click_element(chrome_driver, Locators.constructor)
        helpers.click_element(chrome_driver, Locators.filling_section)
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(Locators.beef_meteorite)
        )
        assert 'Говяжий метеорит (отбивная)' in chrome_driver.page_source

