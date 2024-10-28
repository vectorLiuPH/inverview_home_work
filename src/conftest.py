
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from src.pages.homePage.actions import HomePageActions
from src.pages.pre_actions.actions import PreActions

def pytest_addoption(parser):
    parser.addoption(
        "--noReset",action='store',default=True,help='please add argument "--noReset==False" if you want to reset app'
    )
@pytest.fixture(scope="session")
def my_opt(request):
    no_reset=request.config.getoption("--noReset")
    return no_reset

@pytest.fixture(scope="function")
def init_appium_driver(my_opt):
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        appPackage='hko.MyObservatory_v1_0',
        appActivity='.AgreementPage',
        language='en',
        locale='US',
        noReset=my_opt
    )
    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    driver.terminate_app('hko.MyObservatory_v1_0')
    driver.quit()


@pytest.fixture(scope="function")
def init_with_dealing_dialog(init_appium_driver):
    home_page_actions = HomePageActions(init_appium_driver)
    if not init_appium_driver.capabilities['noReset']:
        pa = PreActions(init_appium_driver)
        pa.deal_with_disclaimer()
        pa.deal_with_PPS()
        pa.deal_with_send_notifications_dialog()
        pa.deal_with_access_location_dialog()
        pa.deal_with_access_location_info()
        pa.deal_with_allow_access_location_info()
        init_appium_driver.implicitly_wait(10)
        home_page_actions.close_background_image()
        pa.select_english_language()
    else:
        init_appium_driver.implicitly_wait(10)
        home_page_actions.close_background_image()
    yield init_appium_driver
