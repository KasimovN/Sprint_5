from selenium.webdriver.support import expected_conditions
from data import Data
from helpers import RandomCreds
from locators import StellarBurgersLocators
from selenium.webdriver.support.wait import WebDriverWait


class TestRegister:
    def test_register_success(self, driver):
        generated_email = RandomCreds.random_email()
        generated_password = RandomCreds.random_password()

        main_button_account = driver.find_element(*StellarBurgersLocators.MAIN_BUTTON_ACCOUNT)
        main_button_account.click()

        visible_register = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                             LOGIN_BUTTON_REGISTER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_REGISTER).click()

        visible_register_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                    REGISTER_BUTTON_REGISTER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register_button)

        driver.find_element(*StellarBurgersLocators.REGISTER_INPUT_NAME).send_keys(Data.TEST_NAME)
        driver.find_element(*StellarBurgersLocators.REGISTER_INPUT_EMAIL).send_keys(generated_email)
        driver.find_element(*StellarBurgersLocators.REGISTER_INPUT_PASSWORD).send_keys(generated_password)

        driver.find_element(*StellarBurgersLocators.REGISTER_BUTTON_REGISTER).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register)

        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_EMAIL).send_keys(generated_email)
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_PASSWORD).send_keys(generated_password)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOGIN).click()

        visible_order_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                 CONSTRUCTOR_ORDER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_order_button)

        main_button_account.click()

        visible_logout_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                  ACCOUNT_BUTTON_LOGOUT)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_logout_button)

        registered_login = driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN).get_attribute('value')

        assert registered_login == generated_email

    def test_register_mistake(self, driver):
        main_button_account = driver.find_element(*StellarBurgersLocators.MAIN_BUTTON_ACCOUNT)
        main_button_account.click()

        visible_register = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                             LOGIN_BUTTON_REGISTER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_REGISTER).click()

        visible_register_button = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                    REGISTER_BUTTON_REGISTER)
        WebDriverWait(driver, Data.WAIT_TIME).until(visible_register_button)

        driver.find_element(*StellarBurgersLocators.REGISTER_INPUT_NAME).send_keys(Data.TEST_NAME)
        driver.find_element(*StellarBurgersLocators.REGISTER_INPUT_EMAIL).send_keys('test.wrong.password@ya.ru')
        driver.find_element(*StellarBurgersLocators.REGISTER_INPUT_PASSWORD).send_keys('12345')

        driver.find_element(*StellarBurgersLocators.REGISTER_BUTTON_REGISTER).click()

        password_notification = driver.find_element(*StellarBurgersLocators.REGISTER_PASSWORD_NOTIFICATION).text
        assert password_notification == 'Некорректный пароль'
