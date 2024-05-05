import pytest
import data
import random
import string
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(data.TestUrls.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def random_email(char_num=7):
    return (''.join(random.choice(string.ascii_letters) for _ in range(char_num))
            + str(random.randint(1, 999)) + "@yandex.com")


@pytest.fixture
def random_password():
    return str(random.randint(100000, 999999))
