import unittest
from datetime import date

from lxml import etree

from nessus_report_parser import NessusClientData
from nessus_report_parser import Report


class TestNessusFile(unittest.TestCase):
    def test_real_nessus_file(self):
        node = etree.XML(open('tests/files/Epoca_ke6t29.nessus.xml').read())

        self.assertIsInstance(NessusClientData.from_etree(node).report,
                              Report)