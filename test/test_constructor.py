import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


def click_element(driver, locator):

    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(locator))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)


def test_bun_section():
    driver = webdriver.Chrome()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        click_element(driver, Locators.constructor)
        time.sleep(4)
        click_element(driver, Locators.bun_section)
        time.sleep(4)
        assert "Булки" in driver.page_source

    finally:
        driver.quit()


def test_sauce_section():
    driver = webdriver.Chrome()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        click_element(driver, Locators.constructor)
        time.sleep(4)
        click_element(driver, Locators.section_sauces)
        time.sleep(4)
        assert "Соусы" in driver.page_source

    finally:
        driver.quit()


def test_fillings_section():
    driver = webdriver.Chrome()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        click_element(driver, Locators.constructor)
        time.sleep(4)
        click_element(driver, Locators.filling_section)
        time.sleep(4)
        assert "Начинки" in driver.page_source

    finally:
        driver.quit()
