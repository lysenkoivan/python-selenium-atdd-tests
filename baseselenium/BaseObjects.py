"""
Created on Nov 7, 2014

@author: oskliarov
"""
from copy import copy

from selenium.common.exceptions import NoSuchElementException

from baseselenium.Driver import Driver
from baseselenium.SeleniumWrappers import WebElementWrapper


class BasePageObject(object):
    """
    Base class for all page objects.
    All child should define self url
    """
    url = None

    def __init__(self):
        self.driver = Driver.get_driver()

        self.elements = {}

    def open(self, parameters=()):
        """
        :rtype: self
        :return:
        """
        print "open url " + (self.url % parameters)
        Driver.open_page(self.url, parameters)
        return self


class BaseWebElement(WebElementWrapper):
    """ Base element for 'page object' pattern.
    Encapsulate logic of driver setup and changing of context of element usage.

    It is supposed that an element is part of a page object, or another element.
    Page object class should have 'driver' attribute with instance of selenium web driver object.

    Example:

    class SomePageObject(object):
        element = BaseWebElement(By.XPATH, "//tag")

        def __init__(self):
            self.driver = webdriver.Firefox()
    """
    # noinspection PyMissingConstructor
    def __init__(self, by, selector, name=None, owner=None):
        self._locator = (by, selector)
        self._name = name
        if owner:
            if isinstance(owner, BaseWebElement):
                self._parent = owner.parent
                self._owner = owner
            else:
                self._parent = owner.driver
                self._owner = owner.driver
            we = self._owner.find_element(*self._locator)
            self._id = we._id

    def __get__(self, owner, cls):
        if isinstance(owner, BaseWebElement):
            self._parent = owner.parent
            self._owner = owner
        else:
            self._parent = owner.driver
            self._owner = owner.driver
        we = self._owner.find_element(*self._locator)
        # noinspection PyProtectedMember
        self._id = we._id
        return self

    @property
    def locator(self):
        return self._locator


class PageBlock(BaseWebElement):
    """
    Successor is container for another web elements.
    """

    def is_child_element_displayed(self, name):
        Driver.implicitly_wait(0)
        try:
            res = self.__getattribute__(name).is_displayed()
        except NoSuchElementException:
            res = False
        Driver.implicitly_wait()
        return res

    def all_elements(self):
        """returns all PageElements grouped by this block, or it parent(s)
        :rtype: list[(str, PageElement)]
        """
        classes = [type(self)]
        fields = set()
        while len(classes) > 0:
            bases = []
            for c in classes:
                bases.extend(list(c.__bases__))
                fields.update(k for k, v in vars(c).items() if not k.startswith("_") and isinstance(v, BaseWebElement))
            classes = bases
        res = []
        for k in fields:
            e = getattr(self, k)
            if e is not None:
                res.append((k, e))
        return res


class SimpleElement(BaseWebElement):
    pass