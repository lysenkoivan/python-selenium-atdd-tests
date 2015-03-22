from behave_tests import *
from unittest import TestCase
from selenium.common.exceptions import NoSuchElementException
from github.Pages import *

__author__ = 'lysenkoivan'


@given('user is on "{page}"')
def step_impl(context, page):
    context.cur_page = get_page_by_name(page)
    context.cur_page().open()


@when("user clicks on {element}")
def step_impl(context, element):
    context.cur_page.elements[element].click()


@then("user sees {element}")
def step_impl(context, element):
    context.cur_page.elements[element].is_displayed()


@when("user types {text} in {element}")
def step_impl(context, text, element):
    context.cur_page.elements[element].type(text)