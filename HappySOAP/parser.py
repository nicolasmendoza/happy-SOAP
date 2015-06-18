import xml.etree.ElementTree as ET
import xml.parsers.expat
from .loggers import getLogger
from xml.etree.ElementTree import QName, Element

logger = getLogger(__name__)


class SOAPParserError(Exception):
    pass

class WSDLElement(object):
    def __init__(self):
        self.namespaces = []


class SOAPParser(object):
    """
    SOAP Parser...
    """
    def __init__(self, wsdl_file):
        self.wsdl_file = wsdl_file
        self.happy_parser()

    def happy_parser(self):
        wsdl = WSDLElement()

        for event, element in ET.iterparse(self.wsdl_file, events=('start-ns', 'end')):
            logger.debug('event -->%s, element -->%s', event, element)
            if event == 'start-ns':
                wsdl.namespaces.append(element)

        logger.info('Namespaces -->%s', wsdl.namespaces)


def start_element(name, attrs):
    nm = Element(QName(name))
    logger.debug('QNAME DICT--> %s', nm.__dict__)

    attrs = attrs or {'NADA': 'NADA'}
    logger.info('Start --> %s,  %s', name, attrs)
    logger.info('Start <--> %s,  %s', type(name), type(attrs))

    return name, attrs


def end_element(tag):
    logger.info('End --> %s', tag)
    return tag

def char_data(text):
    logger.debug('Type of QData --> %s', text)
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
