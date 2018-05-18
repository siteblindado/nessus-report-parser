from unittest import TestCase

from lxml import etree

from nessus_report_parser.model.helpers import trim_encoding_declaration, process_text_element


class TestTrimEncodingDeclaration(TestCase):
    def test_multiline_xml(self):
        xml = '<?xml version="1.0" ?>\n' \
              '<NessusClientData_v2>\n' \
              '    <Policy>\n' \
              '        <policyName>Full</policyName>\n' \
              '    </Policy>\n' \
              '</NessusClientData_v2>'

        expected_xml = '<NessusClientData_v2>\n' \
                       '<Policy>\n' \
                       '<policyName>Full</policyName>\n' \
                       '</Policy>\n' \
                       '</NessusClientData_v2>'

        self.assertEqual(expected_xml,
                         trim_encoding_declaration(xml))

    def test_trim_one_line_xml(self):
        xml = '<?xml version="1.0" ?><NessusClientData_v2><Policy><policyName>' \
              'Full</policyName></Policy></NessusClientData_v2>'
        expected_xml = '<NessusClientData_v2><Policy><policyName>' \
                       'Full</policyName></Policy></NessusClientData_v2>'

        self.assertEqual(expected_xml,
                         trim_encoding_declaration(xml))

    def test_valid_xml_without_declaration(self):
        xml = '<Root><Name>This is Root!</Name></Root>'
        expected_xml = '<Root><Name>This is Root!</Name></Root>'

        self.assertEqual(expected_xml,
                         trim_encoding_declaration(xml))


class TestProcessTextElement(TestCase):
    def test_none(self):
        self.assertIsNone(process_text_element(None))

    def test_invalid_node_type(self):
        self.assertIsNone(process_text_element(123456))

    def test_invalid_text(self):
        xml = '<MyNonText></MyNonText>'
        node = etree.XML(xml)

        self.assertRaises(AttributeError, process_text_element, node)

    def test_valid_text(self):
        xml = '<MyNonText>My Valid Text</MyNonText>'
        node = etree.XML(xml)

        self.assertEqual('My Valid Text',
                         process_text_element(node))

