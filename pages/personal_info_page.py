from selenium.webdriver.common.by import By

from helpers.custom_wait import AttributeHasValue
from pages.base_page import BasePage
from assertpy import assert_that


class PersonalInfoPage(BasePage):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)

    _first_name = (By.ID, "firstname")
    _last_name = (By.ID, "lastname")
    _email = (By.ID, "email")
    _current_password = (By.ID, "old_passwd")
    _new_password = (By.ID, "passwd")
    _confirmation = (By.ID, "confirmation")
    _save_button = (By.NAME, "submitIdentity")
    _current_birth_day = (By.XPATH, "//select[@id='days']//option[@selected]")
    _current_birth_month = (By.XPATH, "//select[@id='months']//option[@selected]")
    _current_birth_year = (By.XPATH, "//select[@id='years']//option[@selected]")

    def verify_first_name(self, first_name):
        AttributeHasValue(self._first_name, "value", first_name)

    def verify_last_name(self, last_name):
        AttributeHasValue(self._last_name, "value", last_name)

    def verify_email(self, email):
        AttributeHasValue(self._email, "value", email)

    def verify_day_of_birth(self, day, month, year):
        AttributeHasValue(self._current_birth_day, "value", day)
        month = self.driver.find_element(*self._current_birth_month)
        assert_that(month.text).contains(month)
        AttributeHasValue(self._current_birth_year, "value", year)
