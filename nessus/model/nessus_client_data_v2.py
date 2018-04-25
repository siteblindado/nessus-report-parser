from lxml import etree

from nessus.model.report import Report


class NessusClientData:
    def __init__(self, properties):
        assert isinstance(properties, dict)
        self.__dict__.update(properties)

    @staticmethod
    def from_etree(elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'NessusClientData_v2'

        properties = {
            'report': Report.from_etree(elem.find('Report'))
        }

        return NessusClientData(properties)