import unittest

from lxml import etree

from nessus_report_parser import HostProperties


class TestHostProperties(unittest.TestCase):
    def test_well_formed_node(self):
        node = '<HostProperties>' \
               '<tag name="HOST_END">Thu Apr 12 16:40:57 2018</tag>' \
               '<tag name="LastUnauthenticatedResults">1523562057</tag>' \
               '<tag name="Credentialed_Scan">false</tag>' \
               '<tag name="policy-used">Basic Network Scan</tag>' \
               '<tag name="patch-summary-total-cves">9</tag>' \
               '</HostProperties>'

        expected_dict = {'HOST_END': 'Thu Apr 12 16:40:57 2018',
                         'LastUnauthenticatedResults': '1523562057',
                         'Credentialed_Scan': 'false',
                         'policy-used': 'Basic Network Scan',
                         'patch-summary-total-cves': '9'}

        self.assertEqual(expected_dict,
                         HostProperties.from_etree(etree.XML(node)).__dict__)