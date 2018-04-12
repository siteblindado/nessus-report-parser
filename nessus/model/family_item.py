from lxml import etree

from .helpers import process_text_element


class FamilyItem:
    def __init__(self, family_name, status):
        self.family_name = family_name
        self.status = status

    @classmethod
    def from_etree(cls, elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'FamilyItem'

        family_name = process_text_element(elem.find('FamilyName'))
        status = process_text_element(elem.find('Status'))

        return FamilyItem(family_name, status)
