import logging
from re import match
from datetime import datetime

from lxml import etree


def trim_encoding_declaration(xml):
    lines = list(map(str.strip, xml.splitlines()))
    return '\n'.join(lines[1:]) if '<?xml' in lines[0] else '\n'.join(lines)


def process_nested_text_element(root, path):
    elem = root
    for path_elem in path.split('.'):
        if elem.find(path_elem) is None:
            return None
        elem = elem.find(path_elem)
    return process_text_element(elem)


def process_text_element(xml_element):
    if xml_element is None or not isinstance(xml_element, etree._Element):
        return None
    try:
        return xml_element.text.strip()
    except Exception as e:
        logging.error(xml_element.tag)
        logging.error(xml_element.text)
        logging.exception(e)
        return None


def process_datetime_element(xml_element):
    if xml_element is None or not isinstance(xml_element, etree._Element):
        return None
    try:
        text = xml_element.text.strip() if xml_element.text else None
        if not text:
            return text
        if text.endswith('AM') or text.endswith('PM'):
            return datetime.strptime(text, "%m/%d/%Y %I:%M:%S %p")
        if match('\d\d:\d\d:\d\d\s', text):
            return datetime.strptime(text, '%H:%M:%S %m/%d/%Y')
        if match('\d\d:\d\d:\d\d:\d\d\d\s', text):
            return datetime.strptime(text, '%H:%M:%S:%f %m/%d/%Y')
        return datetime.strptime(text, "%m/%d/%Y %H:%M:%S")
    except Exception as e:
        logging.error(xml_element.tag)
        logging.error(xml_element.text)
        logging.exception(e)
        return None


def process_date_element(xml_element):
    if xml_element is None or not isinstance(xml_element, etree._Element):
        return None
    text = xml_element.text.strip() if xml_element.text else None
    if not text:
        return text
    try:
        return datetime.strptime(text, "%Y/%m/%d").date()
    except ValueError as e:
        logging.error(xml_element.tag)
        logging.error(xml_element.text)
        logging.exception(e)
        return None
    except Exception as e:
        logging.error(xml_element.tag)
        logging.error(xml_element.text)
        logging.exception(e)
        return text


def process_int_element(xml_element):
    if xml_element is None or not isinstance(xml_element, etree._Element):
        return None
    try:
        if xml_element.text:
            return int(xml_element.text.strip())
        return None
    except Exception as e:
        logging.error(xml_element.tag)
        logging.error(xml_element.text)
        logging.exception(e)
        return xml_element.text