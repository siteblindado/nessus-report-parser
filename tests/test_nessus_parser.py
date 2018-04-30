from unittest import TestCase
from lxml import etree
from nessus import parse_nessus_file, parse_nessus_xml

from nessus.model.nessus_client_data_v2 import NessusClientData


class TestNessusFile(TestCase):
    def test_valid_file(self):
        nessus_file = 'test_files/Epoca_ke6t29.nessus.xml'

        self.assertIsInstance(parse_nessus_file(nessus_file), NessusClientData)


class TestNessusXml(TestCase):
    def test_valid_xml(self):
        nessus_xml = open('test_files/Epoca_ke6t29.nessus.xml').read()

        self.assertIsInstance(parse_nessus_xml(nessus_xml), NessusClientData)
