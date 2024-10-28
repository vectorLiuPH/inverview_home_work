from src.pages.base_actions import BaseActions
from src.pages.homePage.locators import HomePageLocators


class HomePageActions(BaseActions):
    hpl = HomePageLocators()

    def open_navigator(self):
        self.click_element(self.hpl.navigator)

    def open_forecast_warning_services(self):
        self.click_element(self.hpl.forecast_warning_services_drop_down)

    def close_background_image(self):
        if self.is_element_exist(self.hpl.background_image):
            self.driver.press_keycode(keycode='4')
