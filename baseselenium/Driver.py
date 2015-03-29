__author__ = 'lysenkoivan'

import threading
from urlparse import urljoin

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

from baseselenium.SeleniumParameters import SeleniumParameters
from baseselenium.SeleniumWrappers import WebDriverWrapperFirefox, WebDriverWrapperChrome, WebDriverWrapperIe, \
    WebDriverWrapperSafari, WebDriverWrapperRemote


class Driver(object):
    # attribute to save single instance of Driver
    _obj = None
    _webDriverStorage = threading.local()

    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls, *args, **kwargs)
        return cls._obj

    @classmethod
    def _init_driver(cls):
        driver_type = SeleniumParameters.getProperty('browser', 'firefox')
        if driver_type == 'firefox':
            cls._webDriverStorage.driver = WebDriverWrapperFirefox()
        elif driver_type == 'chrome':
            cls._webDriverStorage.driver = WebDriverWrapperChrome()
        elif driver_type == 'ie':
            cls._webDriverStorage.driver = WebDriverWrapperIe()
        elif driver_type == 'safari':
            cls._webDriverStorage.driver = WebDriverWrapperSafari()
        elif driver_type == 'remote':
            cls._webDriverStorage.driver = WebDriverWrapperRemote(
                command_executor=SeleniumParameters.getProperty('command_executor'),
                desired_capabilities=DesiredCapabilities.FIREFOX)
        else:
            raise Exception('Unsupported browser: ' + driver_type)

        if SeleniumParameters.getProperty('browser.window.state', 'maximize') == 'maximize':
            cls._webDriverStorage.driver.maximize_window()

        cls._webDriverStorage.driver.implicitly_wait(SeleniumParameters.getProperty('timeout', '0'))

    @classmethod
    def get_driver(cls):
        """
        :rtype: selenium.webdriver.remote.webdriver.WebDriver
        :return:
        """
        initialized = getattr(cls._webDriverStorage, 'driver', None)
        if initialized is None:
            cls._init_driver()
        return cls._webDriverStorage.driver

    @classmethod
    def tear_down(cls):
        cls._webDriverStorage.driver.quit()
        cls._webDriverStorage.driver = None

    @classmethod
    def open_page(cls, url=None, url_parameters=()):
        if url is None:
            full_url = SeleniumParameters.get_base_url()
        elif url.startswith("http://") or url.startswith("https://"):
            full_url = url
        else:
            full_url = urljoin(SeleniumParameters.get_base_url(), url)

        cls.get_driver().get(full_url % url_parameters)

    @classmethod
    def implicitly_wait(cls, timeout=None):
        if timeout is None:
            timeout = SeleniumParameters.getProperty('timeout', '0')
        cls.get_driver().implicitly_wait(timeout)

    @classmethod
    def wait_until(cls, method, timeout=20):
        try:
            Driver.implicitly_wait(0)
            wait = WebDriverWait(cls.get_driver(), timeout)
            wait.until(method)
        finally:
            Driver.implicitly_wait()

    @classmethod
    def wait_until_not(cls, method, timeout=20):
        try:
            Driver.implicitly_wait(0)
            wait = WebDriverWait(cls.get_driver(), timeout)
            wait.until_not(method)
        finally:
            Driver.implicitly_wait()

    @classmethod
    def wait_page_ready(cls, timeout=90):
        """
        Wait Ajax loading and wait ready state
        """
        wait = WebDriverWait(cls.get_driver(), timeout)
        wait.until(lambda x: cls.get_driver().execute_script(
            "return ((document.readyState == 'complete') && ((typeof($) === 'undefined') ? true : !$.active));"))

