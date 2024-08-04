from selenium.webdriver.support import expected_conditions
from data import Data
from locators import StellarBurgersLocators
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_login_account_button(self, driver):
        main_button_account = driver.find_element(*StellarBurgersLocators.MAIN_BUTTON_ACCOUNT)
        main_button_account.click()

        visible_register = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                             LOGIN_BUTTON_REGISTER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register)

        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_EMAIL).send_keys(Data.REGISTERED_EMAIL)
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_PASSWORD).send_keys(Data.REGISTERED_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOGIN).click()

        visible_order_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                 CONSTRUCTOR_ORDER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_order_button)

        main_button_account.click()

        visible_logout_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                  ACCOUNT_BUTTON_LOGOUT)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_logout_button)

        login = driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN).get_attribute('value')

        assert login == Data.REGISTERED_EMAIL

    def test_login_login_button(self, driver):
        main_button_login = driver.find_element(*StellarBurgersLocators.MAIN_BUTTON_LOGIN)
        main_button_login.click()

        visible_register = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                             LOGIN_BUTTON_REGISTER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register)

        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_EMAIL).send_keys(Data.REGISTERED_EMAIL)
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_PASSWORD).send_keys(Data.REGISTERED_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOGIN).click()

        visible_order_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                 CONSTRUCTOR_ORDER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_order_button)

        main_button_account = driver.find_element(*StellarBurgersLocators.MAIN_BUTTON_ACCOUNT)
        main_button_account.click()

        visible_logout_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                  ACCOUNT_BUTTON_LOGOUT)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_logout_button)

        login = driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN).get_attribute('value')

        assert login == Data.REGISTERED_EMAIL

    def test_login_register_form(self, driver):
        main_button_login = driver.find_element(*StellarBurgersLocators.MAIN_BUTTON_LOGIN)
        main_button_login.click()

        visible_register = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                             LOGIN_BUTTON_REGISTER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_REGISTER).click()

        visible_register_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                    REGISTER_BUTTON_REGISTER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register_button)

        driver.find_element(*StellarBurgersLocators.REGISTER_BUTTON_LOGIN).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register)

        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_EMAIL).send_keys(Data.REGISTERED_EMAIL)
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_PASSWORD).send_keys(Data.REGISTERED_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOGIN).click()

        visible_order_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                 CONSTRUCTOR_ORDER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_order_button)

        main_button_account = driver.find_element(*StellarBurgersLocators.MAIN_BUTTON_ACCOUNT)
        main_button_account.click()

        visible_logout_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                  ACCOUNT_BUTTON_LOGOUT)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_logout_button)

        login = driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN).get_attribute('value')

        assert login == Data.REGISTERED_EMAIL

    def test_login_forgot_password_form(self, driver):
        main_button_account = driver.find_element(*StellarBurgersLocators.MAIN_BUTTON_ACCOUNT)
        main_button_account.click()

        visible_register = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                             LOGIN_BUTTON_REGISTER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register)

        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_FORGOT_PASSWORD).click()

        visible_forgot_password = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                    FORGOT_TITLE)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_forgot_password)

        driver.find_element(*StellarBurgersLocators.FORGOT_BUTTON_LOGIN).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register)

        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_EMAIL).send_keys(Data.REGISTERED_EMAIL)
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_PASSWORD).send_keys(Data.REGISTERED_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOGIN).click()

        visible_order_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                 CONSTRUCTOR_ORDER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_order_button)

        main_button_account.click()

        visible_logout_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                  ACCOUNT_BUTTON_LOGOUT)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_logout_button)

        login = driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN).get_attribute('value')

        assert login == Data.REGISTERED_EMAIL
