from selenium import webdriver
from selenium.webdriver.common.by import By
import time

personal_account_button_1 = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")  # Раздел "Личный кабинет". Главная страница
personal_account_button_2 = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # Раздел "Личный кабинет". Главная страница
account_login_button = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт". Главная страница
field_email = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")  # Поле "Email". Страница "Вход"
password_field = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")  # Поле "Пароль". Страница "Вход"
login_button = (By.XPATH, "//button[contains(text(), 'Войти')]")  # Кнопка "Войти" Страница "Вход"
name_registration = (By.XPATH, "//*[@id='root']//input[@name='name']")  # Поле "Имя". Страница "Регистрация"
constructor = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")  # Раздел "Конструктор" в шапке сайта.
stellar_burgers_logo = (By.CSS_SELECTOR, "#root header nav div a svg")  # Логотип Stellar Burgers в шапке сайта
exit_button = (By.XPATH, "//*[@id='root']//main//nav//ul//li[3]//button")  # Кнопка "Выход". Страница "Профиль"
field_name = (By.CSS_SELECTOR, "#root>div>main>div>div>div>ul>li:nth-child(1)>div>div>input")  # Окно "Имя". Страница "Профиль"


def setup_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

def test_login_and_check_name():
    driver = setup_driver()
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*personal_account_button_1).click()
        driver.find_element(*field_email).send_keys("dima199768@gmail.com")
        driver.find_element(*password_field).send_keys("123456789")
        driver.find_element(*login_button).click()
        driver.find_element(*personal_account_button_1).click()
        time.sleep(4)
    finally:
        driver.quit()


def test_login_and_navigate_to_constructor():
    driver = setup_driver()
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*personal_account_button_1).click()
        driver.find_element(*field_email).send_keys("dima199768@gmail.com")
        driver.find_element(*password_field).send_keys("123456789")
        driver.find_element(*login_button).click()
        driver.find_element(*constructor).click()
        time.sleep(4)

    finally:
        driver.quit()

def test_navigate_to_constructor_via_logo():
    driver = setup_driver()
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*personal_account_button_1).click()
        driver.find_element(*field_email).send_keys("dima199768@gmail.com")
        driver.find_element(*password_field).send_keys("123456789")
        driver.find_element(*login_button).click()
        driver.find_element(*stellar_burgers_logo).click()
        time.sleep(4)

    finally:
        driver.quit()

def test_logout():
    driver = setup_driver()
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*personal_account_button_1).click()
        driver.find_element(*field_email).send_keys("dima199768@gmail.com")
        driver.find_element(*password_field).send_keys("123456789")
        driver.find_element(*login_button).click()
        time.sleep(2)
        driver.find_element(*personal_account_button_2).click()
        driver.find_element(*exit_button).click()
        time.sleep(3)
    finally:
        driver.quit()
