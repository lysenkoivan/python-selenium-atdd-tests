__author__ = 'Ivan Lysenko'

from behave import *

from baseselenium.SeleniumParameters import SeleniumParameters
from baseselenium.Driver import Driver


def before_all(context):
    SeleniumParameters.loadParameters()


def before_scenario(context, scenario):
    context.driver = Driver.get_driver()


def after_scenario(context, scenario):
    Driver.tear_down()