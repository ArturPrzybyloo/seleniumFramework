from selenium.webdriver.common.by import By
from config import config
from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage


class LoginPage(BasePage):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)

    _email_input = (By.ID, "email")
    _password_input = (By.ID, "passwd")
    _sign_in_button = (By.ID, "SubmitLogin")

    def enter_login_credentials(self):
        email_input = self.ca.wait_for_visibility(self._email_input)
        email_input.send_keys(config.APP_USER_LOGIN)
        password_input = self.ca.wait_for_visibility(self._password_input)
        password_input.send_keys(config.APP_USER_PASS)
        self.ca.wait_for_visibility(self._sign_in_button, click=True)
