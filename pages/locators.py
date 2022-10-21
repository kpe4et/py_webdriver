from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form [type='submit']")
    PRODUCT_NAME_H1 = (By.CSS_SELECTOR, "h1")
    PRODUCT_NAME_NOTIFY = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner strong")
    PRODUCT_PRICE_DIV = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_PRICE_NOTIFY = (By.CSS_SELECTOR, "#messages > div:nth-child(3) p:nth-child(1) strong")