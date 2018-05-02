from io import StringIO

from lxml import etree

from .model.nessus_client_data_v2 import NessusClientData
from .model.helpers import trim_encoding_declaration
from .model.family_item import FamilyItem
from .model.family_selection import FamilySelection
from .model.host_properties import HostProperties
from .model.report import Report
from .model.report_host import ReportHost
from .model.report_item import ReportItem


def parse_nessus_file(xml_file):
    return NessusClientData.from_etree(etree.XML(open(xml_file).read()))


def parse_nessus_xml(xml):
    xml = trim_encoding_declaration(xml)
    elem = etree.parse(StringIO(xml)).getroot()
    return NessusClientData.from_etree(elem)