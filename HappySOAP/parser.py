# -*- coding: utf-8 -*-
from cStringIO import StringIO
from collections import namedtuple
import xml.etree.ElementTree as ET
import xml.parsers.expat
from .loggers import getLogger
from xml.etree.ElementTree import QName, Element
from .models import ApiBinding
import pipelines

logger = getLogger(__name__)


class SOAPParser(object):
    """
    SOAP Parser...
    """

    def __init__(self, wsdl_file, soap_version):
        self.soap = ApiBinding()
        self.xml = wsdl_file
        self.namespaces = []

        self._happy_parser()

    def _happy_parser(self):
        _file = StringIO(self.xml)

        for event, element in ET.iterparse(_file, events=('start-ns', 'end')):
            if event == 'start-ns':
                self.namespaces.append(element)
            if event == 'end':
                logger.debug('Element -->%s', element)

        xml = ET.fromstring(self.xml)

        namespace = 'http://schemas.xmlsoap.org/wsdl/'

        binding_tag = str(QName(namespace, 'binding'))
        messages_tag = str(QName(namespace, 'message'))

        bindings = xml.find(binding_tag)
        messages = xml.findall(messages_tag)

        print bindings
        print 'messages-->', messages

    def get_api_soap(self):
        return self.soap