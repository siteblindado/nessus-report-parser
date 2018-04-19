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
            'description': process_text_element(elem.find('description')),
            'fname': process_text_element(elem.find('fname')),
            'plugin_modification_date': process_date_element(elem.find('plugin_modification_date')),
            'plugin_publication_date': process_date_element(elem.find('plugin_publication_date')),
            'plugin_type': process_text_element(elem.find('plugin_type')),
            'risk_factor': process_text_element(elem.find('risk_factor')),
            'script_version': process_text_element(elem.find('script_version')),
            'solution': process_text_element(elem.find('solution')),
            'synopsis': process_text_element(elem.find('synopsis')),
            'plugin_output': process_text_element(elem.find('plugin_output'))
        }

        return ReportItem(properties)
