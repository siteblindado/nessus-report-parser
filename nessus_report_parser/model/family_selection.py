from collections import UserList

from lxml import etree

from .family_item import FamilyItem


class FamilySelection(UserList):
    def __repr__(self):
        return str(self.data)

    @staticmethod
    def from_etree(elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'FamilySelection'

        assessments = [FamilyItem.from_etree(assessment) for assessment in
                       elem.findall('FamilyItem')]

        return FamilySelection(assessments)
