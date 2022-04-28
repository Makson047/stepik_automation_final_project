from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def verify_is_basket_empty(self):
        self.should_not_be_products_basket()
        self.should_be_text_about_empty_basket()

    def should_not_be_products_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Basket items is presented, but should not be"
