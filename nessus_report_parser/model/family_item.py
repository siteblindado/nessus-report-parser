from collections import UserDict

from lxml import etree

from .helpers import process_text_element


class FamilyItem(UserDict):
    def __init__(self, properties):
        assert isinstance(properties, dict)
        assert all(key in properties.keys() for key in ['family_name', 'status'])
        self.data = properties

    @classmethod
    def from_etree(cls, elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'FamilyItem'

        properties = {
            'family_name': process_text_element(elem.find('FamilyName')),
            'status': process_text_element(elem.find('Status'))
        }

        return FamilyItem(properties)
