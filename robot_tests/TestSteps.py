__author__ = 'lysenkoivan'

from github.Pages import *

from baseselenium.Driver import Driver


class TestSteps:

    def __init__(self):
        self.cur_page = None

    # @given('user is on "{page}"')
    def on_page(self, page):
        self.cur_page = open_page_by_name(page)
        Driver.wait_page_ready()

    # @when('user clicks on "{element}"')
    def click_on(self, element):
        self.cur_page.elements[element].click()

    # @then('user sees element "{element}"')
    def check_element(self, element):
        # context.cur_page.elements[element].is_displayed()
        Driver.wait_until(self.cur_page.elements[element].is_displayed)

    # @when('user types "{text}" in "{element}"')
    def type_in(self, text, element):
        self.cur_page.elements[element].send_keys(text)

    # @then('user sees text "{text}" in "{element}"')
    def check_text_in(self, text, element):
        Driver.wait_until(self.cur_page.elements[element].is_displayed)
        assert self.cur_page.elements[element].self_text == text