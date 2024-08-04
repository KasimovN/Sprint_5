from selenium.webdriver.support import expected_conditions
from data import Data
from locators import StellarBurgersLocators
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    def test_sauce_button(self, driver):
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

        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_SAUCE).click()

        highlighted_sauce = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                              CONSTRUCTOR_HIGHLIGHTED_SAUCE)
        WebDriverWait(driver, Data.WAIT_TIME).until(highlighted_sauce)

        assert driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_HIGHLIGHTED_SAUCE).is_displayed()

    def test_fillings_button(self, driver):
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

        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_FILLINGS).click()

        highlighted_fillings = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                 CONSTRUCTOR_HIGHLIGHTED_FILLINGS)
        WebDriverWait(driver, Data.WAIT_TIME).until(highlighted_fillings)

        assert driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_HIGHLIGHTED_FILLINGS).is_displayed()

    def test_buns_button(self, driver):
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

        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_FILLINGS).click()

        highlighted_fillings = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                                 CONSTRUCTOR_HIGHLIGHTED_FILLINGS)
        WebDriverWait(driver, Data.WAIT_TIME).until(highlighted_fillings)

        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_BUNS).click()

        highlighted_buns = expected_conditions.visibility_of_element_located(StellarBurgersLocators.
                                                                             CONSTRUCTOR_HIGHLIGHTED_BUNS)
        WebDriverWait(driver, Data.WAIT_TIME).until(highlighted_buns)

        assert driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_HIGHLIGHTED_BUNS).is_displayed()
