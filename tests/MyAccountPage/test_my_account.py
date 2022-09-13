from pages.main_page import MainPage
from pages.my_account_page import MyAccountPage
from pages.personal_info_page import PersonalInfoPage


class TestMyAccount:

    def test_my_personal_info(self, driver, login_with_user_credentials):
        main_page = MainPage(driver)
        account_page = MyAccountPage(driver)
        info_page = PersonalInfoPage(driver)
        main_page.go_to_my_account()
        account_page.click_information_button()
        info_page.verify_first_name("a")
        info_page.verify_day_of_birth("4", "May", "2016")
