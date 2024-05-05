from locators import *


class TestConstructor:
    def test_constructor_buns(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()

        assert 'current' in driver.find_element(*Locators.BUNS_BUTTON).get_attribute(
            'class'
        )

    def test_constructor_sauces(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        assert 'current' in driver.find_element(*Locators.SAUCES_BUTTON).get_attribute(
            'class'
        )

    def test_constructor_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click()

        assert 'current' in driver.find_element(
            *Locators.FILLINGS_BUTTON).get_attribute('class')
