import time
from selenium import webdriver
from locators import Locators
import helpers


def test_bun_section():
    driver = webdriver.Chrome()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        helpers.click_element(driver, Locators.constructor)
        time.sleep(4)
        helpers.click_element(driver, Locators.bun_section)
        time.sleep(4)
        assert "Булки" in driver.page_source

    finally:
        driver.quit()


def test_sauce_section():
    driver = webdriver.Chrome()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        helpers.click_element(driver, Locators.constructor)
        time.sleep(4)
        helpers.click_element(driver, Locators.section_sauces)
        time.sleep(4)
        assert "Соусы" in driver.page_source

    finally:
        driver.quit()


def test_fillings_section():
    driver = webdriver.Chrome()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        helpers.click_element(driver, Locators.constructor)
        time.sleep(4)
        helpers.click_element(driver, Locators.filling_section)
        time.sleep(4)
        assert "Начинки" in driver.page_source

    finally:
        driver.quit()
