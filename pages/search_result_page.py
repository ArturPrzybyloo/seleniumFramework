from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)

    _sort_by_select = (By.ID, "selectProductSort")
    _add_to_cart_button = (By.XPATH, "//a[@title='Add to cart']")
    _more_button = (By.XPATH, "//a[@title='View']")

    def select_sort_by(self, sort_by):
        self.ca.wait_for_visibility(self._sort_by_select)
        self.ca.choose_dropdown(self._sort_by_select, sort_by)
