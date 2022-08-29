import pytest

from config import config
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture()
def login_with_user_credentials(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    base_url = config.APP_BASE_URL
    driver.get(base_url)
    main_page.click_login_button()
    login_page.enter_login_credentials()
    main_page.verify_signing_in()

