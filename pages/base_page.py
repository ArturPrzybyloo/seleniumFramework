from pypom import Page
from faker import Faker
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from config import config
from helpers.common_actions import CommonActions


class BasePage(Page):

    def __init__(self, driver, **url):
        super().__init__(driver, **url)
        self.wait = WebDriverWait(driver, config.MAX_WAIT)
        self.ec = ec
        self.fake = Faker()
        self.ca = CommonActions(driver)

