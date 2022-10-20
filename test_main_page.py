from .pages.main_page import MainPage
from .pages.login_page import LoginPage

LINK = "http://selenium1py.pythonanywhere.com/"
LOGINLINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

def test_guest_can_go_to_login_page(browser): 
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    

def test_should_see_login_link(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_login_link()

def test_should_be_login_page(browser):
    page = LoginPage(browser, LOGINLINK)
    page.open()
    page.should_be_login_page()