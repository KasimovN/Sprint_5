from selenium.webdriver.support import expected_conditions
from data import Data
from locators import StellarBurgersLocators
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    def test_logout_button(self, driver):
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

        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON_LOGOUT).click()

        assert WebDriverWait(driver, Data.WAIT_TIME).until(visible_register)
