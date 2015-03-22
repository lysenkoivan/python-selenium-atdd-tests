__author__ = 'Ivan Lysenko'

from baseselenium.BaseObjects import BasePageObject
from Elements import *


class MainPage(BasePageObject):
    city_selector = CityCaret(By.CSS_SELECTOR, ".location")
    diseases = SimpleElement(By.CSS_SELECTOR, ".diseases")

    def check_city(self, city=u'Харьков'):
        return self.city_selector.current_city == city

