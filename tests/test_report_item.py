import unittest
from datetime import date

from lxml import etree

from nessus_report_parser import ReportItem


class TestReportItem(unittest.TestCase):
    def test_well_formed_node(self):
        node = '<ReportItem port="0" svc_name="general" protocol="tcp" severity="0" pluginID="19506" pluginName="Nessus Scan Information" pluginFamily="Settings"><agent>all</agent>' \
               '<description>This plugin displays, for each tested host,\n' \
               'information about the scan itself :\n\n- The version of the' \
               ' plugin set.\n- The type of scanner (Nessus or Nessus Home).\n' \
               '- The version of the Nessus Engine.\n- The port scanner(s)' \
               ' used.\n- The port range scanned.\n- Whether credentialed or' \
               ' third-party patch management\nchecks are possible.\n- The' \
               ' date of the scan.\n- The duration of the scan.\n- The number' \
               ' of hosts scanned in parallel.\n- The number of checks done' \
               ' in parallel.</description><fname>scan_info.nasl</fname>' \
               '<plugin_modification_date>2017/10/26' \
               '</plugin_modification_date><plugin_name>Nessus Scan' \
               ' Information</plugin_name><plugin_publication_date>2005/08/26' \
               '</plugin_publication_date><plugin_type>summary</plugin_type>' \
               '<risk_factor>None</risk_factor><script_version>$Revision:' \
               ' 1.90 $</script_version><solution>n/a</solution><synopsis>' \
               'This plugin displays information about the Nessus scan.' \
               '</synopsis><plugin_output>Information about this scan :\n\n' \
               'Nessus version : 7.0.3\nPlugin feed version : 201804120615\n' \
               'Scanner edition used : Nessus\nScan type : Normal\nScan' \
               ' policy used : Basic Network Scan\nScanner IP :' \
               ' 10.168.69.130\nPort scanner(s) : nessus_syn_scanner\nPort' \
               ' range : default\nThorough tests : no\nExperimental tests :' \
               ' no\nParanoia level : 1\nReport verbosity : 1\nSafe checks :' \
               ' yes\nOptimize the test : yes\nCredentialed checks : no\n' \
               'Patch management checks : None\nCGI scanning : disabled\nWeb' \
               ' application tests : disabled\nMax hosts : 30\nMax checks :' \
               ' 4\nRecv timeout : 5\nBackports : None\nAllow post-scan' \
               ' editing: Yes\nScan Start Date : 2018/4/12 16:30 -03\nScan' \
               ' duration : 605 sec</plugin_output></ReportItem>'

        expected_dict = {
            'agent': 'all',
            'bid': None,
            'canvas_package': None,
            'cve': None,
            'cvss_base_score': None,
            'cvss_temporal_score': None,
            'cvss_vector': None,
            'port': '0',
            'service_name': 'general',
            'protocol': 'tcp',
            'severity': '0',
            'plugin_id': '19506',
            'plugin_name': 'Nessus Scan Information',
            'plugin_family': 'Settings',
            'description': 'This plugin displays, for each tested host,\ninformation about the scan itself :\n\n- The version of the plugin set.\n- The type of scanner (Nessus or Nessus Home).\n- The version of the Nessus Engine.\n- The port scanner(s) used.\n- The port range scanned.\n- Whether credentialed or third-party patch management\nchecks are possible.\n- The date of the scan.\n- The duration of the scan.\n- The number of hosts scanned in parallel.\n- The number of checks done in parallel.',
            'exploit_available': None,
            'exploit_framework_canvas': None,
            'exploit_framework_core': None,
            'exploit_framework_metasploit': None,
            'exploitability_ease': None,
            'fname': 'scan_info.nasl',
            'metasploit_name': None,
            'patch_publication_date': None,
            'plugin_modification_date': date(2017, 10, 26),
            'plugin_publication_date': date(2005, 8, 26),
            'plugin_type': 'summary',
            'plugin_version': 'summary',
            'risk_factor': 'None',
            'script_version': '$Revision: 1.90 $',
            'see_also': None,
            'solution': 'n/a',
            'synopsis': 'This plugin displays information about the Nessus scan.',
            'plugin_output': 'Information about this scan :\n\nNessus version : 7.0.3\nPlugin feed version : 201804120615\nScanner edition used : Nessus\nScan type : Normal\nScan policy used : Basic Network Scan\nScanner IP : 10.168.69.130\nPort scanner(s) : nessus_syn_scanner\nPort range : default\nThorough tests : no\nExperimental tests : no\nParanoia level : 1\nReport verbosity : 1\nSafe checks : yes\nOptimize the test : yes\nCredentialed checks : no\nPatch management checks : None\nCGI scanning : disabled\nWeb application tests : disabled\nMax hosts : 30\nMax checks : 4\nRecv timeout : 5\nBackports : None\nAllow post-scan editing: Yes\nScan Start Date : 2018/4/12 16:30 -03\nScan duration : 605 sec',
            'vulnerability_publication_date': None,
            'xref': None
        }

        self.assertEqual(expected_dict,
                         ReportItem.from_etree(etree.XML(node)).__dict__)