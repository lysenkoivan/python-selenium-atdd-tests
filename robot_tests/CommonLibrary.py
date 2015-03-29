__author__ = 'lysenkoivan'

from baseselenium.SeleniumParameters import SeleniumParameters
from baseselenium.Driver import Driver

SeleniumParameters.loadParameters()


class CommonLibrary:
    def load_parameters(self):
        SeleniumParameters.loadParameters()
        self.init_driver()

    def init_driver(self):
        Driver.get_driver()

    def driver_teardown(self):
        Driver.tear_down()