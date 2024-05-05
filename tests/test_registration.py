import data
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    def test_registration_positive(self, driver, random_email, random_password):
        driver.get(data.TestUrls.REG_PAGE)

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys(data.TestDefaultData.NAME)
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(random_email)
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys(random_password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )

        assert data.TestUrls.LOGIN_PAGE == driver.current_url

    def test_registration_negative_password(self, driver):
        driver.get(data.TestUrls.REG_PAGE)

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys(data.TestDefaultData.NAME)
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(data.TestDefaultData.EMAIL)
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys(data.TestDefaultData.INCORRECT_PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()

        assert (
                driver.find_element(*Locators.WRONG_PASSWORD_ERROR).text
                == 'Некорректный пароль'
        )
