from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BUTTON)
        btn_add_to_basket.click()

    def verify_added_product(self):
        self.should_be_the_same_product_name()
        self.should_be_the_same_price_basket_as_product()

    # Проверка, что товар в корзине соответствует выбранному товару
    def should_be_the_same_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name_in_basket == product_name, "In basket lying another product than you added"

    # Проверка, что стоимость корзины соответствует стоимости товара
    def should_be_the_same_price_basket_as_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price in basket_price, "Price is not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but must disappeared"
