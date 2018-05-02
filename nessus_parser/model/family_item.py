from lxml import etree

from .helpers import process_text_element


class FamilyItem:
    def __init__(self, properties):
        assert isinstance(properties, dict)
        self.__dict__.update(properties)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def from_etree(cls, elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'FamilyItem'

        properties = {
            'family_name': process_text_element(elem.find('FamilyName')),
            'status': process_text_element(elem.find('Status'))
        }

        return FamilyItem(properties)
