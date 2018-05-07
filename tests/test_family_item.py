import unittest

from lxml import etree

from nessus_report_parser import FamilyItem


class TestFamilyItem(unittest.TestCase):
    def test_well_formed_node(self):
        node = "<FamilyItem>" \
               "<FamilyName>Scientific Linux Local Security Checks</FamilyName>" \
               "<Status>enabled</Status>" \
               "</FamilyItem>"

        expected_dict = {'family_name': 'Scientific Linux Local Security Checks',
                         'status': 'enabled'}

        self.assertEqual(expected_dict,
                         FamilyItem.from_etree(etree.XML(node)).__dict__
                         )