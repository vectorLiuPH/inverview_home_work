
import appium.webdriver
from selenium.common import WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.tools import element_exception_handler


class BaseActions:
    def __init__(self, appium_driver):
        self.driver = appium_driver

    @element_exception_handler
    def click_element(self,
                      locator,
                      wait_time=5,
                      ):
        WebDriverWait(self.driver, wait_time).until(ec.element_to_be_clickable(locator)).click()

    @element_exception_handler
    def find_element(self,
                     locator,
                     wait_time=5,driver=None) -> appium.webdriver.WebElement:
        driver=self.driver if driver is None else driver
        element = WebDriverWait(driver, wait_time).until(ec.presence_of_element_located(locator))
        return element


    def is_element_exist(self,
                         locator,
                         wait_time=2,driver=None) -> bool:
        try:
            driver = self.driver if driver is None else driver
            WebDriverWait(driver, wait_time).until(ec.presence_of_element_located(locator))
            return True
        except WebDriverException:
            return False

    @element_exception_handler
    def get_text(self,
                 locator,
                 wait_time=5,driver=None):
        driver=self.driver if driver is None else driver
        return WebDriverWait(driver, wait_time).until(ec.presence_of_element_located(locator)).text

    @element_exception_handler
    def find_elements(self,
                      locator,
                      wait_time=5) -> [appium.webdriver.WebElement]:
        elements = WebDriverWait(self.driver, wait_time).until(ec.presence_of_all_elements_located(locator))
        return elements

    def get_texts(self,
                  locator,
                  wait_time=5):
        texts = []
        elements = self.find_elements(locator=locator,
                                      wait_time=wait_time)
        for element in elements:
            element_text = element.text
            texts.append(element_text)
        return texts
