from collections import UserList

from lxml import etree

from .report_item import ReportItem


class ReportHost(UserList):
    def __init__(self, elements, host_properties):
        super(ReportHost, self).__init__(elements)
        assert isinstance(host_properties, dict)
        self.__dict__.update(host_properties)

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def from_etree(elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'ReportHost'

        host_properties = {'name': elem.attrib.get('name')}
        report_items = [ReportItem.from_etree(el) for el in elem.findall('ReportItem')]

        return ReportHost(report_items, host_properties)
