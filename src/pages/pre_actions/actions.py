from src.pages.base_actions import BaseActions
from src.pages.homePage.locators import HomePageLocators
from src.pages.pre_actions.locators import PreActionsLocators


class PreActions(BaseActions):
    pal = PreActionsLocators()
    hpl= HomePageLocators()
    def deal_with_disclaimer(self):
        if self.is_element_exist(self.pal.disclaimer_agree_button):
            self.click_element(self.pal.disclaimer_agree_button)

    def deal_with_PPS(self):
        if self.is_element_exist(self.pal.PPS_agree_button):
            self.click_element(self.pal.PPS_agree_button)

    def deal_with_send_notifications_dialog(self):
        if self.is_element_exist(self.pal.allow_all_the_time_button):
            self.click_element(self.pal.allow_all_the_time_button)

    def deal_with_access_location_dialog(self):
        if self.is_element_exist(self.pal.access_location_dialog_ok_button):
            self.click_element(self.pal.access_location_dialog_ok_button)

    def deal_with_access_location_info(self):
        if self.is_element_exist(self.pal.allow_while_using_button):
            self.click_element(self.pal.allow_while_using_button)

    def deal_with_allow_access_location_info(self):
        if self.is_element_exist(self.pal.allow_access_location_info):
            self.click_element(self.pal.allow_all_the_time_button)

    def select_english_language(self):
        self.click_element(self.hpl.right_top_options)
        self.click_element(self.hpl.switch_language_button)
        self.click_element(self.hpl.english_language_option)
