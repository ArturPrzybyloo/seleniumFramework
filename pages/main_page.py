from selenium.webdriver.common.by import By
from pages.search_bar_region import SearchBarRegion
from pages.base_page import BasePage
from assertpy import assert_that


class MainPage(BasePage):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)

    _sign_in_button = (By.XPATH, "//a[@class='login']")
    _sign_out_button = (By.XPATH, "//a[@class='logout']")
    _found_products = (By.XPATH, "//div[@class='product-container']//a[@class='product-name']")
    _my_account_button = (By.XPATH, "//a[@title='View my customer account']")

    def search(self, search_expression):
        search_bar = SearchBarRegion(self.driver)
        search_bar.search(search_expression)

    def click_login_button(self):
        self.ca.wait_for_visibility(self._sign_in_button, click=True)

    def verify_signing_in(self):
        self.ca.wait_for_visibility(self._sign_out_button)

    def verify_search_results(self, searched_expression):
        elements = self.driver.find_elements(*self._found_products)
        for element in elements:
            assert_that(element.text).contains(searched_expression)

    def go_to_my_account(self):
        self.ca.wait_for_visibility(self._my_account_button, click=True)


