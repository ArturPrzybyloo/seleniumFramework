from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from config import config


class CommonActions:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.MAX_WAIT)
        self.ec = ec

    def clear_input_element(self, input_element):
        while input_element.get_attribute('value') != '':
            input_element.click()
            input_element.send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE + Keys.BACKSPACE)
        return self

    def wait_for_visibility(self, locator_tuple, click=False):
        element = self.wait.until(self.ec.visibility_of_element_located(locator_tuple))
        if click:
            element.click()
        return element

    def refresh_page(self):
        self.driver.refresh()

    def close_tab(self):
        self.driver.close()

    def choose_dropdown(self, locator, value):
        self.locator = locator
        self.value = value

        select = Select(locator)
        select.select_by_visible_text(value)







