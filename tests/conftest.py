import pytest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from config.config import HEADLESS, DISABLE_NOTIFICATIONS


@pytest.fixture()
def driver(request):
    wd = _prepare_chrome_driver()
    session = request.node
    cls = session.getparent(pytest.Class)
    setattr(cls.obj, "driver", wd)
    request.addfinalizer(wd.quit)
    return wd


def _prepare_chrome_driver():
    chrome_options, d = _prepare_chrome_options()
    wd = webdriver.Chrome(options=chrome_options, desired_capabilities=d)
    return wd


def _prepare_chrome_options(FULLSCREEN=None):
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


# @pytest.fixture
# def screenshot_on_fail(driver, request):
#     yield
#     if request.node.report_setup.failed:
#         print('Test setup failed for test: ' + request.node._nodeid)
#     elif request.node.report_setup.passed:
#         if request.node.report_call.failed:
#             take_screenshot(driver, request)
