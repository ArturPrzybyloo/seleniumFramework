from datetime import datetime
import time
from config import config
import pytest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from config.config import HEADLESS, DISABLE_NOTIFICATIONS, FULLSCREEN
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.my_account_page import MyAccountPage


@pytest.fixture()
def driver(request):
    wd = _prepare_chrome_driver()
    session = request.node
    cls = session.getparent(pytest.Class)
    setattr(cls.obj, "driver", wd)
    request.addfinalizer(wd.quit)
    return wd

@pytest.fixture()
def login_with_user_credentials(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    my_account_page = MyAccountPage(driver)

    base_url = config.APP_BASE_URL
    driver.get(base_url)
    main_page.click_login_button()
    login_page.enter_login_credentials()
    main_page.verify_signing_in()
    my_account_page.click_home_button()


def _prepare_chrome_driver():
    chrome_options, d = _prepare_chrome_options()
    wd = webdriver.Chrome(options=chrome_options, desired_capabilities=d)
    return wd


def _prepare_chrome_options():
    browser_options = webdriver.ChromeOptions()
    if HEADLESS:
        browser_options.add_argument("--headless")
        browser_options.add_argument('--no-sandbox')
        browser_options.add_argument('--window-size=1920,1200')
        browser_options.add_argument('--disable-gpu')
        browser_options.add_argument('--disable-dev-shm-usage')
    if FULLSCREEN:
        browser_options.add_argument("--start-fullscreen")
    if DISABLE_NOTIFICATIONS:
        browser_options.add_argument("--disable-notifications")
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'WARNING'}
    d['perfLoggingPrefs'] = {'enableNetwork': 'true'}
    d['goog:loggingPrefs'] = {'performance': 'ALL'}
    return browser_options, d


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


# Create screenshot on test fail
@pytest.fixture(scope="function", autouse=True)
def screenshot_on_fail(driver, request):
    yield
    if request.node.rep_setup.failed:
        print('Test setup failed for test: ' + request.node._nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            take_screenshot(driver, request)
            print("Executing test failed. Taking screenshot.", request.node.nodeid)


# Save screenshot
def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    driver.save_screenshot(file_name)
