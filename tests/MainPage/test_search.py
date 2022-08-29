from pages.main_page import MainPage
from tests.base_test import BaseTest


class TestSearch(BaseTest):

    def test_search(self, driver, login_with_user_credentials):
        main_page = MainPage(driver)
        main_page.search()
