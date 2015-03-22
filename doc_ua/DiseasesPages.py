__author__ = 'Ivan Lysenko'

from selenium.webdriver.common.by import By

from baseselenium.BaseObjects import BasePageObject, SimpleElement, PageBlock


class DiseaseListPage(BasePageObject):
    alphas_picker = SimpleElement(By.CSS_SELECTOR, ".diseases-directory__alphabet > li > a > span")
    diseases_picker = SimpleElement(By.XPATH, "//*[@id='disease-item-0'/ul/div/li/a")

    def select_alpha(self, alpha="б"):
        for item in self.alphas_picker.find_elements(self.alphas_picker.locator):
            if item.self_text == alpha:
                item.click()
                break

    def select_diseas(self, title):
        for item in self.diseases_picker.find_elements(self.diseases_picker.locator):
            if item.self_text == title:
                item.click()
                break

