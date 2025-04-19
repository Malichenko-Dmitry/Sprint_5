import pytest
from selenium import webdriver


@pytest.fixture()
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_chrome_site(chrome_driver):
    def _open_site():
        chrome_driver.get("https://stellarburgers.nomoreparties.site/")
    yield _open_site