import unittest
from datetime import date

from lxml import etree

from nessus.model.nessus_client_data_v2 import NessusClientData
from nessus.model.report import Report


class TestNessusFile(unittest.TestCase):
    def test_real_nessus_file(self):
        node = etree.XML(open('test_files/Epoca_ke6t29.nessus.xml').read())

        self.assertIsInstance(NessusClientData.from_etree(node).report,
                              Report)