from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site"

    def open(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def click_element(self, locator):
        element = self.find_element(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys_to_element(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_element_text(self, locator, time=10):
        element = self.find_element(locator, time)
        return element.text

    def get_element_attribute(self, locator, attribute, time=10):
        element = self.find_element(locator, time)
        return element.get_attribute(attribute)

    def wait_for_url_to_contain(self, text, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.url_contains(text),
            message=f"URL doesn't contain {text}"
        )

    def wait_for_element_to_disappear(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator),
            message=f"Element is still visible: {locator}"
        )