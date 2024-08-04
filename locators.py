from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    # Главная страница
    MAIN_BUTTON_ACCOUNT = (By.XPATH, "//a[@href='/account']")  # Кнопка "Личный кабинет"
    MAIN_BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"

    # Страница "Вход"
    LOGIN_INPUT_EMAIL = (By.XPATH, "//div[contains(@class,'input_type_text')]/..//input")  # Текстовое поле "Email"
    LOGIN_INPUT_PASSWORD = (By.XPATH, "//div[contains(@class,'input_type_password')]/..//input")  # Текстовое поле "Пароль"
    LOGIN_BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    LOGIN_BUTTON_REGISTER = (By.XPATH, "//a[@href='/register']")  # Кнопка "Зарегистрироваться"
    LOGIN_BUTTON_FORGOT_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']") # Кнопка "Восстановить пароль"

    # Страница "Регистрация"
    REGISTER_INPUT_NAME = (By.XPATH, "//label[text()='Имя']/../input")  # Текстовое поле "Имя"
    REGISTER_INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/../input")  # Текстовое поле "Email"
    REGISTER_INPUT_PASSWORD = (By.XPATH, "//label[text()='Пароль']/../input")  # Текстовое поле "Пароль"
    REGISTER_BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON_LOGIN = (By.XPATH, "//a[text()='Войти']")  # Кнопка "Войти"
    REGISTER_PASSWORD_NOTIFICATION = (By.XPATH, "//p[text()='Некорректный пароль']")  # Уведомление "Некорректный пароль"

    # Страница "Восстановление пароля"
    FORGOT_BUTTON_LOGIN = (By.XPATH, "//a[text()='Войти']")  # Кнопка "Войти"
    FORGOT_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")  # Кнопка "Войти"

    # Страница "Личный кабинет"
    ACCOUNT_BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']/..")  # Кнопка "Конструктор"
    ACCOUNT_BUTTON_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a")  # Заголовок страницы/Логотип
    ACCOUNT_BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
    ACCOUNT_LOGIN = (By.XPATH, "//label[text()='Логин']/..//input")

    # Страница "Конструктор"
    CONSTRUCTOR_SAUCE = (By.XPATH, "//span[text()='Соусы']")  # Вкладка "Соусы"
    CONSTRUCTOR_FILLINGS = (By.XPATH, "//span[text()='Начинки']")  # Вкладка "Начинка"
    CONSTRUCTOR_BUNS = (By.XPATH, "//span[text()='Булки']")  # Вкладка "Булки"
    CONSTRUCTOR_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    CONSTRUCTOR_HIGHLIGHTED_SAUCE = (By.XPATH,
                                     "//div[contains(@class,'tab_tab_type_current__2BEPc')]/span[text()='Соусы']")  # Активен раздел "Соусы"
    CONSTRUCTOR_HIGHLIGHTED_FILLINGS = (By.XPATH,
                                     "//div[contains(@class,'tab_tab_type_current__2BEPc')]/span[text()='Начинки']")  # Активен раздел "Начинки"
    CONSTRUCTOR_HIGHLIGHTED_BUNS = (By.XPATH,
                                        "//div[contains(@class,'tab_tab_type_current__2BEPc')]/span[text()='Булки']")  # Активен раздел "Булки"
