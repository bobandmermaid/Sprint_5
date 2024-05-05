import data
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSignIn:
    def test_sign_in_on_main_page(self, driver):
        driver.find_element(*Locators.MAIN_AUTH_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestDefaultData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestDefaultData.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

        assert driver.find_element(*Locators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_sign_in_from_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestDefaultData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestDefaultData.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

        assert driver.find_element(*Locators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_sign_in_from_register(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestDefaultData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestDefaultData.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

        assert driver.find_element(*Locators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_sign_in_from_reset_password(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.RESET_PASSWORD_LINK).click()
        driver.find_element(*Locators.RESET_LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestDefaultData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestDefaultData.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

        assert driver.find_element(*Locators.ORDER_BUTTON).text == 'Оформить заказ'
