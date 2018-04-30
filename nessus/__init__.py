from io import StringIO

from lxml import etree

from nessus.model.nessus_client_data_v2 import NessusClientData
from .model.helpers import trim_encoding_declaration


def parse_nessus_file(xml_file):
    return NessusClientData.from_etree(etree.XML(open(xml_file).read()))


def parse_nessus_xml(xml):
    xml = trim_encoding_declaration(xml)
    elem = etree.parse(StringIO(xml)).getroot()
    return NessusClientData.from_etree(elem)