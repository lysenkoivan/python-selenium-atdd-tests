import os
from xml.dom.minidom import parse
from yaml import load


class SeleniumParameters(object):
    #selenium parameters configured for all test suite
    _seleniumParameters = {}

    @classmethod
    def getProperty(cls, propertyName, defaultValue = None):
        if defaultValue == None:
            return cls._seleniumParameters[propertyName]
        else:
            return cls._seleniumParameters.get(propertyName, defaultValue)

    @classmethod
    def setProperty(cls, propertyName, propertyValue):
        cls._seleniumParameters[propertyName] = propertyValue

    @classmethod
    def loadParameters(cls, filename="config.yaml"):
        config = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r')
        yaml = load(config)

        def flat_list(original_dict, flat_dict_output, cur_key=[]):
            sort_keys = iter(sorted(original_dict.keys()))
            for key in sort_keys:
                if isinstance(original_dict[key], dict):
                    # if len(flat_dict_output.keys()) == 0:
                    #     cur_key = key
                    # else:
                    # cur_key.append(key)
                    flat_list(original_dict[key], flat_dict_output, cur_key)
                    # cur_key.pop(-1)
                else:
                    cur_key.append(key)
                    k = '/'.join(cur_key)
                    flat_dict_output[k] = original_dict[key]
                    cur_key.pop(-1)

        flat_list(yaml, cls._seleniumParameters)

    @classmethod
    def get_base_url(cls):
        return os.getenv('GD_SELENIUM_SUT_SERVER', cls.getProperty('baseURL'))