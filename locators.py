from selenium.webdriver.common.by import By

class Locators:

    personal_account_button_1 = By.XPATH, "//*[@id='root']/div/header/nav/a/p"  # Раздел "Личный кабинет". Главная страница

    personal_account_button_2 = By.XPATH, "//p[contains(text(), 'Личный Кабинет'"  # Раздел "Личный кабинет". Главная страница

    account_login_button = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"  # Кнопка "Войти в аккаунт". Главная страница

    field_email = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"  # Поле "Email". Страница "Вход"

    register = By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a"  # "Зарегистрироваться". Страница "Вход"

    password_field = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"  # Поле "Пароль". Страница "Вход"

    login_button = By.XPATH, "//button[contains(text(), 'Войти')]"  # Кнопка "Войти" Страница "Вход"

    password_recovery = By.XPATH, "//*[@id='root']/div/main/div/div/p[2]/a"  # "Восстановить пароль". Страница "Вход"

    name_registration = By.XPATH, "//*[@id='root']//input[@name='name']"  # Поле "Имя". Страница "Регистрация"

    email_registration = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"  # Поле "Email". Страница "Регистрация"

    password_registration = By.XPATH, "//*[@id='root']//input[@name='Пароль']"  # Поле "Пароль". Страница "Регистрация"

    registration_button = By.XPATH, "//*[@id='root']/div/main/div/form/button"  # Кнопка "Зарегистрироваться". Страница "Регистрация"

    incorrect_password = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p"  # Сообщение об ошибки "Некорректный пароль". Страница "Регистрация"

    email_password_recovery = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset/div/div/input"  # Поле "Email". Страница "Восстановление пароля"

    recover_button = By.XPATH, "//*[@id='root']/div/main/div/form/button"  # Кнопка "Восстановить". Страница "Восстановление пароля"

    constructor = By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p"  # Раздел "Конструктор" в шапке сайта.

    stellar_burgers_logo = By.CSS_SELECTOR, "#root header nav div a svg"  # Логотип Stellar Burgers в шапке сайта

    exit_button = By.XPATH, "//*[@id='root']//main//nav//ul//li[3]//button"  # Кнопка "Выход". Страница "Профиль"

    field_name = By.CSS_SELECTOR, "#root>div>main>div>div>div>ul>li:nth-child(1)>div>div>input"  # Окно "Имя". Страница "Профиль"

    bun_section = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]/span"  # Раздел "Булки"

    fluorescent_bun = By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]/img"  # Флюоресцентная булка

    section_sauces = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]"  # Раздел "Соусы"

    spicy_x = By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[2]/a[1]"  # Соус Spicy-X

    filling_section = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span"  # Раздел "Начинки"

    beef_meteorite = By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[3]/a[2]/img"  # "Говяжий метеорит(отбивная)"

