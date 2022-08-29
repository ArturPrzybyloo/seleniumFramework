from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)

    _search_bar = (By.NAME, "search_query")
    _sign_in_button = (By.XPATH, "//a[@class='login']")
    _sign_out_button = (By.XPATH, "//a[@class='logout']")

    def search(self):
        self.ca.wait_for_visibility(self._search_bar)

    def click_login_button(self):
        self.ca.wait_for_visibility(self._sign_in_button, click=True)

    def verify_signing_in(self):
        self.ca.wait_for_visibility(self._sign_out_button)

