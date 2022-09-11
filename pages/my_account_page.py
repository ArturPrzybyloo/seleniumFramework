from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MyAccountPage(BasePage):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)

    _order_history_button = (By.XPATH, "//a[@title='Orders']")
    _credit_slips_button = (By.XPATH, "//a[@title='Credit slips']")
    _my_address_button = (By.XPATH, "//a[@title='Addresses']")
    _my_personal_info_button = (By.XPATH, "//a[@title='Information']")
    _my_wishlist_button = (By.XPATH, "//a[@title='My wishlists']")
    _home_button = (By.XPATH, "//a[@title='Home']")

    def loaded(self):
        self.ca.wait_for_visibility(self._order_history_button)

    def click_order_button(self):
        self.ca.wait_for_visibility(self._order_history_button, click=True)

    def click_credit_button(self):
        self.ca.wait_for_visibility(self._credit_slips_button, click=True)

    def click_address_button(self):
        self.ca.wait_for_visibility(self._my_address_button, click=True)

    def click_information_button(self):
        self.ca.wait_for_visibility(self._my_personal_info_button, click=True)

    def click_wishlist_button(self):
        self.ca.wait_for_visibility(self._my_wishlist_button, click=True)

    def click_home_button(self):
        self.ca.wait_for_visibility(self._home_button, click=True)
