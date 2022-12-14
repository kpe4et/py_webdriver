from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".basket-mini  a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD_FIELD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    PASSWORD_FIELD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form [type='submit']")
    PRODUCT_NAME_H1 = (By.CSS_SELECTOR, "h1")
    PRODUCT_NAME_NOTIFY = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner strong")
    PRODUCT_PRICE_DIV = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_PRICE_NOTIFY = (By.CSS_SELECTOR, "#messages > div:nth-child(3) p:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert")

class CartPageLocators():
    CART_H1 = (By.CSS_SELECTOR, "h1")
    CART_EMPTY_INDICATION = (By.CSS_SELECTOR, "#content_inner > p > a")