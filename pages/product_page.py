from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def check_product_name_in_notification(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_H1).text
        product_in_cart_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_NOTIFY).text
        assert product_name == product_in_cart_name, "Wrong product in cart"

    def check_product_in_cart_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_DIV).text
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_NOTIFY).text
        assert product_price == product_price_in_cart, "Wrong price in cart"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
                "Success message is presented, but shouldn't be"

    def should_dissapear(self):
        assert self.is_dissapeared(*ProductPageLocators.SUCCESS_MESSAGE), \
                "Success message is presented, but had to dissapear"