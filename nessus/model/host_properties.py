from lxml import etree

from .helpers import process_text_element


class HostProperties:
    def __init__(self, properties):
        assert isinstance(properties, dict)
        self.__dict__.update(properties)

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def from_etree(cls, elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'HostProperties'

        properties = {}
        for element in elem.findall('tag'):
            properties[element.attrib['name']] = element.text

        return HostProperties(properties)
