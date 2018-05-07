from unittest import TestCase
from nessus_report_parser import parse_nessus_file, parse_nessus_xml, NessusClientData


class TestNessusFile(TestCase):
    def test_valid_file(self):
        nessus_file = 'tests/files/Epoca_ke6t29.nessus.xml'

        self.assertIsInstance(parse_nessus_file(nessus_file), NessusClientData)


class TestNessusXml(TestCase):
    def test_valid_xml(self):
        nessus_xml = open('tests/files/Epoca_ke6t29.nessus.xml').read()

        self.assertIsInstance(parse_nessus_xml(nessus_xml), NessusClientData)
