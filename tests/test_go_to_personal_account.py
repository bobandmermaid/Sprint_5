import data
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestGoToPersonalAccount:
    def test_go_to_personal_account(self, driver):
        driver.get(data.TestUrls.LOGIN_PAGE)
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestDefaultData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestDefaultData.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON)
        )

        assert data.TestUrls.PERSONAL_ACCOUNT_PAGE == driver.current_url
