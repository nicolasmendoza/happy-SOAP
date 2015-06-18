from collections import namedtuple
import xml.etree.ElementTree as ET
import xml.parsers.expat
from .loggers import getLogger
from xml.etree.ElementTree import QName, Element

logger = getLogger(__name__)


class SOAPParserError(Exception):
    pass


class SoapElement(dict):
    """
    Soap Element..
    """
    def __init__(self, **kwargs):
        dict.__init__(self,kwargs)
        self.__dict__ = self

class SOAPParser(object):
    """
    SOAP Parser...
    """
    binding_tag = '{http://schemas.xmlsoap.org/wsdl/}binding'

    def __init__(self, wsdl_file, soap_version):
        self.soap = SoapElement(namespaces=[])
        self.wsdl_file = wsdl_file
        self._happy_parser()

    def _binding_parser(self, element):
        """
        Binding Parser...
        """
        logger.warning('Element -->%s', element.__dict__ )
        for element in element._children:
            logger.info('::::::::: ::::::::: ::::::::')

    def _happy_parser(self):
        soap = self.soap

        for event, element in ET.iterparse(self.wsdl_file, events=('start-ns', 'end', 'end-ns')):

            if event == 'start-ns':
                soap.namespaces.append(element)

            if event == "end":
                # todo
                if element.tag == self.binding_tag:
                    self._binding_parser(element)

    def get_soap_element(self):
        return self.soap

def start_element(name, attrs):
    nm = Element(QName(name))
    logger.info('Start --> %s,  %s', name, attrs)
    logger.info('Start <--> %s,  %s', type(name), type(attrs))

    return name, attrs


def end_element(tag):
    logger.info('End --> %s', tag)
    return tag

def char_data(text):
    logger.info('Data --> %s', repr(text))
    return text


def handler_element(attrs):
    logger.debug('Default hanlder --> %s', attrs)
    return attrs

def comment_hanlder(comment):
    logger.debug('Comment Hanlder -->%s', comment)
    return comment


class HappyParser(object):
    """
    Expat Parser....
    p =  HappyParser(xml_string)
    p.parse()
    """
    def __init__(self, xml_string):
        self.xml = xml_string
        self._parse = xml.parsers.expat.ParserCreate(namespace_separator='}')

    def parse(self, level=2):
        p = self._parse

        # callbacks
        p.DefaultHandlerExpand = handler_element
        p.StartElementHandler = start_element
        p.EndElementHandler = end_element
        p.CharacterDataHandler = char_data
        p.CommentHandler = comment_hanlder

        return p.Parse(self.xml, level)
