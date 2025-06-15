from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_locators import BaseLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_ingredients(self):
        return self.find_elements(MainPageLocators.INGREDIENTS)

    def go_to_personal_account(self):
        self.click_element(BaseLocators.PERSONAL_ACCOUNT_BUTTON)

    def go_to_constructor(self):
        self.click_element(BaseLocators.CONSTRUCTOR_BUTTON)

    def go_to_order_feed(self):
        self.click_element(BaseLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self, index=0):
        ingredients = self.get_ingredients()
        if index < len(ingredients):
            ingredients[index].click()
        else:
            raise IndexError(f"Index {index} out of range, only {len(ingredients)} ingredients available")

    def close_ingredient_modal(self):
        self.click_element(BaseLocators.CLOSE_MODAL_BUTTON)

    def add_ingredient_to_order(self, ingredient_index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENTS)
        ingredients[ingredient_index].click()

    def drag_ingredient_to_constructor(self, ingredient_index=0):
        ingredients = self.get_ingredients()
        if ingredient_index < len(ingredients):
            constructor = self.find_element(MainPageLocators.CONSTRUCTOR_AREA)
            action = ActionChains(self.driver)
            action.drag_and_drop(ingredients[ingredient_index], constructor).perform()
        else:
            raise IndexError(f"Index {ingredient_index} out of range, only {len(ingredients)} ingredients available")

    def get_ingredient_counter(self, ingredient_index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENTS)
        if len(ingredients) > ingredient_index:
            try:
                counter_element = ingredients[ingredient_index].find_element(*MainPageLocators.INGREDIENT_COUNTER)
                return int(counter_element.text)
            except:
                return 0
        return 0

    def place_order(self):
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    def is_ingredient_modal_open(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)

    def is_order_confirmation_modal_opened(self):
        return self.is_element_visible(MainPageLocators.ORDER_CONFIRMATION_MODAL)

    def click_bun_tab(self):
        self.click_element(MainPageLocators.BUN_TAB)

    def click_sauce_tab(self):
        self.click_element(MainPageLocators.SAUCE_TAB)

    def click_filling_tab(self):
        self.click_element(MainPageLocators.FILLING_TAB)

    def is_constructor_area_visible(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_AREA)

    def is_ingredient_details_modal_opened(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_HEADER)