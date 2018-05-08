from datetime import date

from lxml import etree

from .helpers import process_text_element, process_date_element


class ReportItem:
    def __init__(self, properties):
        assert isinstance(properties, dict)
        self.__dict__.update(properties)

    @classmethod
    def from_etree(cls, elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'ReportItem'

        properties = {
            'port': elem.attrib.get('port'),
            'service_name': elem.attrib.get('svc_name'),
            'protocol': elem.attrib.get('protocol'),
            'severity': elem.attrib.get('severity'),
            'plugin_id': elem.attrib.get('pluginID'),
            'plugin_name': elem.attrib.get('pluginName'),
            'plugin_family': elem.attrib.get('pluginFamily'),
            'agent': process_text_element(elem.find('agent')),
            'risk_factor': process_text_element(elem.find('risk_factor')),
            'synopsis': process_text_element(elem.find('synopsis')),
            'description': process_text_element(elem.find('description')),
            'solution': process_text_element(elem.find('solution')),
            'plugin_output': process_text_element(elem.find('plugin_output')),
            'see_also': process_text_element(elem.find('see_also')),
            'cve': process_text_element(elem.find('cve')),
            'bid': process_text_element(elem.find('bid')),
            'xref': process_text_element(elem.find('xref')),
            'plugin_modification_date': process_date_element(elem.find('plugin_modification_date')),
            'plugin_publication_date': process_date_element(elem.find('plugin_publication_date')),
            'patch_publication_date': process_date_element(elem.find('patch_publication_date')),
            'vulnerability_publication_date': process_date_element(elem.find('vuln_publication_date')),
            'exploitability_ease': process_text_element(elem.find('exploitability_ease')),
            'exploit_available': process_text_element(elem.find('exploit_available')),
            'exploit_framework_canvas': process_date_element(
                elem.find('exploit_framework_canvas')),
            'exploit_framework_metasploit': process_date_element(
                elem.find('exploit_framework_metasploit')),
            'exploit_framework_core': process_date_element(
                elem.find('exploit_framework_core')),
            'metasploit_name': process_date_element(elem.find('metasploit_name')),
            'canvas_package': process_date_element(elem.find('canvas_package')),
            'cvss_vector': process_text_element(elem.find('cvss_vector')),
            'cvss_base_score': process_text_element(elem.find('cvss_base_score')),
            'cvss_temporal_score': process_text_element(
                elem.find('cvss_temporal_score')),
            'plugin_type': process_text_element(elem.find('plugin_type')),
            'plugin_version': process_text_element(elem.find('plugin_type')),
            'fname': process_text_element(elem.find('fname')),
            'script_version': process_text_element(elem.find('script_version')),
        }

        return ReportItem(properties)
