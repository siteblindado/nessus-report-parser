from lxml import etree

from nessus.model.report_host import ReportHost


class Report:
    def __init__(self, properties):
        assert isinstance(properties, dict)
        self.__dict__.update(properties)

    @staticmethod
    def from_etree(elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'Report'

        properties = {
            'name': elem.attrib.get('name'),
            'host': ReportHost.from_etree(elem.find('ReportHost'))
        }

        return Report(properties)
