from collections import UserDict

from lxml import etree

from .helpers import process_text_element


class HostProperties(UserDict):
    def __init__(self, properties):
        assert isinstance(properties, dict)
        self.data = properties

    @classmethod
    def from_etree(cls, elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'HostProperties'

        properties = {}
        for element in elem.findall('tag'):
            properties[element.attrib['name']] = element.text

        return HostProperties(properties)
