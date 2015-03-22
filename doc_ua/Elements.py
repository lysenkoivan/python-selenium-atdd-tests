__author__ = 'Ivan Lysenko'

from selenium.webdriver.common.by import By

from baseselenium.BaseObjects import SimpleElement, PageBlock


class CityCaret(PageBlock):
    selector = SimpleElement(By.CSS_SELECTOR, ".select7__caret")
    city = PageBlock(By.CSS_SELECTOR, ".select7__drop-list > li")
    current_city = SimpleElement(By.CSS_SELECTOR, ".select7__current-value")

    def select_city(self, city=u"Харьков"):
        self.selector.click()
        for item in self.find_elements(self.city.locator):
            if item.self_text == city:
                item.click()
                break