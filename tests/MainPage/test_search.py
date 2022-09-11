from pages.main_page import MainPage


class TestSearch:

    def test_search(self, driver, login_with_user_credentials):
        """ Tests search for specific word and verify results"""
        main_page = MainPage(driver)
        main_page.search("Dress")
        # BUG : searching for dress returns also t-shirt and blouse
        main_page.verify_search_results("Dress")
