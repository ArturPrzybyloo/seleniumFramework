from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchBarRegion(BasePage):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)
        self.loaded()

    _search_bar = (By.NAME, "search_query")
    _search_button = (By.NAME, "submit_search")
    _women_button = (By.XPATH, "//a[@title='Women']")
    _dresses_button = (By.XPATH, "//a[@title='Dresses']")
    _t_shirts_button = (By.XPATH, "//a[@title='T-shirts']")

    def loaded(self):
        self.ca.wait_for_visibility(self._search_bar)

    def search(self, search_expression):
        self.ca.wait_for_visibility(self._search_bar).send_keys(search_expression)
        self.ca.wait_for_visibility(self._search_button, click=True)
