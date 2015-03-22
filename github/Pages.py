__author__ = 'Ivan Lysenko'

import sys

from baseselenium.BaseObjects import BasePageObject, SimpleElement
from selenium.webdriver.common.by import By
# from Elements import *


def open_page_by_name(name):
    page = getattr(sys.modules[__name__], name)
    page().open()

    return page()


def get_page_by_name(name):
    page = getattr(sys.modules[__name__], name)
    return page()


class MainPage(BasePageObject):
    url = "/"

    name = "MainPage"

    explore = SimpleElement(By.XPATH, "//li[@class='header-nav-item']/a[text()='Explore']")
    signin = SimpleElement(By.XPATH, "//div[@class='header-actions']/a[text()='Sign In']")
    search = SimpleElement(By.NAME, "q")

    def __init__(self):
        super(BasePageObject, MainPage).__init__()
        self.elements = {
            "Explore": self.explore,
            "SignIn": self.signin,
            "Search": self.search,
        }


class SigninPage(BasePageObject):
    url = "/login"

    name = "LoginPage"

    username = SimpleElement(By.ID, "login_field")
    password = SimpleElement(By.ID, "password")
    btn_signin = SimpleElement(By.NAME, "commit")
    error_msg = SimpleElement(By.CSS_SELECTOR, ".flash-error")

    def __init__(self):
        super(BasePageObject, MainPage).__init__()
        self.elements = {
            "Username": self.username,
            "Password": self.password,
            "SignIn button": self.btn_signin,
            "Error message": self.error_msg,
        }

