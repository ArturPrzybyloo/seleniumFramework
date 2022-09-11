from selenium.webdriver.common.by import By
from pages.search_bar_region import SearchBarRegion
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)

    _sign_in_button = (By.XPATH, "//a[@class='login']")
    _sign_out_button = (By.XPATH, "//a[@class='logout']")

    def search(self, search_expression):
        search_bar = SearchBarRegion(self.driver)
        search_bar.search(search_expression)
        self.ca.wait_for_visibility(self._sign_in_button, click=True)

    def click_login_button(self):
        self.ca.wait_for_visibility(self._sign_in_button, click=True)

    def verify_signing_in(self):
        self.ca.wait_for_visibility(self._sign_out_button)

