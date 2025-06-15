from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.recovery_url = f"{self.base_url}/forgot-password"

    def open_recovery_page(self):
        self.driver.get(self.recovery_url)

    def enter_email(self, email):
        self.send_keys_to_element(PasswordRecoveryLocators.EMAIL_FIELD, email)

    def click_recover_button(self):
        self.click_element(PasswordRecoveryLocators.RECOVER_BUTTON)

    def click_show_hide_password(self):
        self.click_element(PasswordRecoveryLocators.SHOW_HIDE_PASSWORD)

    def is_password_field_active(self):
        return self.is_element_visible(PasswordRecoveryLocators.PASSWORD_FIELD_ACTIVE)

    def go_to_login_page(self):
        self.click_element(PasswordRecoveryLocators.LOGIN_LINK)

    def is_recovery_page_displayed(self):
        return self.is_element_visible(PasswordRecoveryLocators.RECOVER_BUTTON)