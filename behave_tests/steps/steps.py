from behave import given, then, when
# from behave_tests import *
from github.Pages import *

__author__ = 'lysenkoivan'


@given('user is on "{page}"')
def step_impl(context, page):
    context.cur_page = open_page_by_name(page)
    Driver.wait_page_ready()


@then('user checks he is on "{page}"')
def step_impl(context, page):
    context.cur_page = get_page_by_name(page)
    Driver.wait_page_ready()
    assert context.cur_page.url in Driver.get_driver().current_url


@when('user clicks on "{element}"')
def step_impl(context, element):
    context.cur_page.elements[element].click()


@then('user sees element "{element}"')
def step_impl(context, element):
    # context.cur_page.elements[element].is_displayed()
    Driver.wait_until(lambda d: context.cur_page.elements[element].is_displayed())


@when('user types "{text}" in "{element}"')
def step_impl(context, text, element):
    context.cur_page.elements[element].send_keys(text)


@then('user sees text "{text}" in "{element}"')
def step_impl(context, text, element):
    Driver.wait_until(lambda d: context.cur_page.elements[element].is_displayed())
    assert context.cur_page.elements[element].self_text == text