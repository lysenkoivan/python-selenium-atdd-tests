import xml.etree.ElementTree as ET

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class WrapperFindOverride(object):
    def find_element(self, by=By.ID, value=None):
        # noinspection PyUnresolvedReferences
        web_el = super(WrapperFindOverride, self).find_element(by, value)
        return WebElementWrapper(web_el.parent, web_el.id, (by, value))

    def find_elements(self, by=By.ID, value=None):
        # noinspection PyUnresolvedReferences
        web_els = super(WrapperFindOverride, self).find_elements(by, value)
        result = []
        for index, web_el in enumerate(web_els):
            result.append(WebElementWrapper(web_el.parent, web_el.id, (by, value)))
        return result


class WebElementWrapper(WrapperFindOverride, WebElement):
    def __init__(self, parent, id_, locator):
        # noinspection PyArgumentList
        super(WebElementWrapper, self).__init__(parent, id_)
        self._locator = locator
        self._name = ""

    @property
    def is_link(self):
        return 'a' == self.tag_name

    @property
    def self_text(self):
        """ get text of the element only
        :rtype: str
        :return:
        """
        inner_html = u"<el>{0}</el>".format(self.get_attribute('innerHTML')).encode('utf-8')
        root = ET.fromstring(inner_html)
        text = root.text or ""
        for e in root.getchildren():
            text += e.tail or ""
        return text.strip()

    # place override methods below


class WebDriverWrapperFirefox(WrapperFindOverride, webdriver.Firefox):
    pass


class WebDriverWrapperChrome(WrapperFindOverride, webdriver.Chrome):
    pass


class WebDriverWrapperIe(WrapperFindOverride, webdriver.Ie):
    pass


class WebDriverWrapperSafari(WrapperFindOverride, webdriver.Safari):
    pass


class WebDriverWrapperRemote(WrapperFindOverride, webdriver.Remote):
    pass
