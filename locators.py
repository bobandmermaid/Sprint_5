from selenium.webdriver.common.by import By


class Locators:
    # Поле ввода имени на странице регистрации
    REG_NAME_INPUT = (
        By.XPATH,
        '//label[text()="Имя"]/following-sibling::*'
    )

    # Поле ввода email на странице регистрации
    REG_EMAIL_INPUT = (
        By.XPATH,
        '//label[text()="Email"]/following-sibling::*'
    )

    # Поле ввода пароля на странице регистрации
    REG_PASSWORD_INPUT = (
        By.XPATH,
        './/input[@name = "Пароль"]'
    )

    # Кнопка "Зарегистрироваться" на странице регистрации
    REG_BUTTON = (
        By.XPATH,
        './/button[text() = "Зарегистрироваться"]'
    )

    # Ошибка при вводе некорректного пароля на странице регистрации
    WRONG_PASSWORD_ERROR = (
        By.XPATH,
        './/p[@class="input__error text_type_main-default"]'
    )

    # Кнопка "Войти в аккаунт" на главной странице
    MAIN_AUTH_BUTTON = (
        By.XPATH,
        './/button[text()="Войти в аккаунт"]'
    )

    # Кнопка "Личный кабинет" в хедере
    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        './/p[text()="Личный Кабинет"]'
    )

    # Поле ввода email на странице авторизации
    LOGIN_EMAIL = (
        By.XPATH,
        './/input[@name = "name"]'
    )

    # Поле ввода пароля на странице авторизации
    LOGIN_PASSWORD = (
        By.XPATH,
        './/input[@name = "Пароль"]'
    )

    # Кнопка "Войти" на странице авторизации
    LOGIN_BUTTON = (
        By.XPATH,
        './/button[text()="Войти"]'
    )

    # Кнопка "Оформить заказ" на главной странице
    ORDER_BUTTON = (
        By.XPATH,
        './/button[text()="Оформить заказ"]'
    )

    # Ссылка "Зарегистрироваться" на странице авторизации
    REG_LINK = (
        By.XPATH,
        './/a[text() = "Зарегистрироваться"]'
    )

    # Ссылка "Войти" на странице регистрации
    LOGIN_LINK = (
        By.XPATH,
        './/a[text()="Войти"]'
    )

    # Ссылка "Восстановить пароль" на странице авторизации
    RESET_PASSWORD_LINK = (
        By.XPATH,
        './/a[text()="Восстановить пароль"]'
    )

    # Ссылка "Войти" на странице сброса пароля
    RESET_LOGIN_LINK = (
        By.XPATH,
        './/a[@class="Auth_link__1fOlj"]'
    )

    # Кнопка "Профиль" в личном кабинете
    PROFILE_BUTTON = (
        By.XPATH,
        './/a[text()="Профиль"]'
    )

    # Кнопка "Конструктор" в хедере
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        './/p[text()="Конструктор"]'
    )

    # Кнопка лого в хедере
    LOGO_BUTTON = (
        By.XPATH,
        './/a[@href="/"]'
    )

    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (
        By.XPATH,
        './/button[text()="Выход"]'
    )

    # Кнопка "Булки" в конструкторе
    BUNS_BUTTON = (
        By.XPATH,
        '//span[text()="Булки"]/parent::*'
    )

    # Кнопка "Соусы" в конструкторе
    SAUCES_BUTTON = (
        By.XPATH,
        '//span[text()="Соусы"]/parent::*'
    )

    # Кнопка "Начинки" в конструкторе
    FILLINGS_BUTTON = (
        By.XPATH,
        '//span[text()="Начинки"]/parent::*'
    )
