from os import link
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import time
import pytest

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "lkaq#@skdfjlvf")

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.add_to_cart()
        # ниже проверка на случай бот-капчи для промо страниц
        # page.solve_quiz_and_get_code()
        page.check_product_name_in_notification()
        page.check_product_in_cart_price()
        page.success_message_should_be()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_cart()
#    page.solve_quiz_and_get_code()
    page.check_product_name_in_notification()
    page.check_product_in_cart_price()
    page.success_message_should_be()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_cart()
    page.should_dissapear()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.check_if_the_cart_is_empty()

@pytest.mark.skip
def test_guest_see_product_in_basket_added_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_cart()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.check_if_the_cart_is_empty()