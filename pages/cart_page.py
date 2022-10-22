from .locators import CartPageLocators
from .base_page import BasePage

#Да, я принципиально называю корзину CART, а не BASKET =) Хотя в названиях тестов оставил BASKET, для удобства ревьюера
class CartPage(BasePage):
    def check_is_this_cart(self):
        cur_title = self.browser.find_element(*CartPageLocators.CART_H1)
        assert cur_title.text == "Basket", "We are not in the basket, man!"

    def check_if_the_cart_is_empty(self):
        assert self.is_element_present(*CartPageLocators.CART_EMPTY_INDICATION), "Cart is not empty"