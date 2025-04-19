from selenium.webdriver.common.by import By

class Locators:

    personal_account_button = By.XPATH, "//p[text()='Личный Кабинет']"  # Раздел "Личный кабинет". Главная страница

    account_login_button = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"  # Кнопка "Войти в аккаунт". Главная страница

    field_email = By.XPATH, "//input[contains(@class,'textfield') and @name='name']"  # Поле "Email". Страница "Вход"

    register = By.XPATH, "//a[@href='/register']"  # "Зарегистрироваться". Страница "Вход"

    password_field = By.XPATH, "//input[contains(@class,'input__textfield') and @type='password']"  # Поле "Пароль". Страница "Вход"

    login_button = By.XPATH, "//button[text() = 'Войти']"  # Кнопка "Войти" Страница "Вход"

    password_recovery = By.XPATH, "//a[text()='Восстановить пароль']"  # "Восстановить пароль". Страница "Вход"

    name_registration = By.XPATH, "//input[@type='text' and @name='name']"  # Поле "Имя". Страница "Регистрация"

    email_registration = By.XPATH, "(//input[@name='name'])[2]"  # Поле "Email". Страница "Регистрация"

    password_registration = By.XPATH, "//input[@type='password']"  # Поле "Пароль". Страница "Регистрация"

    registration_button = By.XPATH, "//button[text()='Зарегистрироваться']"  # Кнопка "Зарегистрироваться". Страница "Регистрация"

    incorrect_password = By.XPATH, "//p[text()='Некорректный пароль']"  # Сообщение об ошибки "Некорректный пароль". Страница "Регистрация"

    email_password_recovery = By.XPATH, "//input[@type='text' and @name='name']"  # Поле "Email". Страница "Восстановление пароля"

    recover_button = By.XPATH, "//button[text()='Восстановить']"  # Кнопка "Восстановить". Страница "Восстановление пароля"

    constructor = By.XPATH, "//p[text()='Конструктор']"  # Раздел "Конструктор" в шапке сайта.

    stellar_burgers_logo = By.XPATH, "//*[local-name()='svg']//*[local-name()='path'][1]"  # Логотип Stellar Burgers в шапке сайта

    exit_button = By.XPATH, "//button[text()='Выход']"  # Кнопка "Выход". Страница "Профиль"

    field_name = By.XPATH, "//input[@name='Name']"  # Поле "Имя". Страница "Профиль"

    field_login = By.XPATH, "(//input[contains(@class, 'input__textfield')])[2]" # Поле Логин. Страница "Профиль"

    field_password_profile = By.XPATH, "(//input[contains(@class, 'input__textfield')])[3]" # Поле Пароль. Страница "Профиль"

    bun_section = By.XPATH, "//span[.='Булки']" # Раздел "Булки"

    fluorescent_bun = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"  # Флюоресцентная булка

    section_sauces = By.XPATH, "//span[.='Соусы']"  # Раздел "Соусы"

    spicy_x = By.XPATH, "//a[contains(., 'Соус Spicy-X')]"  # Соус Spicy-X

    filling_section = By.XPATH, "//span[text()='Начинки']"  # Раздел "Начинки"

    beef_meteorite = By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']"  # "Говяжий метеорит(отбивная)"

    active_section_sauces = By.XPATH, "//span[.='Соусы']/parent::div" # активное состояние кнопки "Соусы" при табе

    active_bun_section = By.XPATH, "//span[.='Булки']/parent::div" # активное состояние кнопки "Булочки" при табе

    active_filling_section = By.XPATH, "//span[text()='Начинки']/parent::div" # активное состояние кнопки "Начинки" при табе
