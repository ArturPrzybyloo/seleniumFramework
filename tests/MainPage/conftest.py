import pytest

from config import config
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.my_account_page import MyAccountPage


@pytest.fixture()
def login_with_user_credentials(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    my_account_page = MyAccountPage(driver)

    base_url = config.APP_BASE_URL
    driver.get(base_url)
    main_page.click_login_button()
    login_page.enter_login_credentials()
    main_page.verify_signing_in()
    my_account_page.click_home_button()

