# -*- coding: utf8 -*-

from StringIO import StringIO
import urllib
from xml.etree import ElementTree as ET
import urlparse

from . import getLogger

logger = getLogger(__name__)

class HTTPError(Exception):
    pass

class HTTPClient(object):
    user_agent = "Happy SOAP (from http://nicolasmendoza.org/happy-SOAP/) "

    def __init__(self, url, **kwargs):
        self.url = url
        self.scheme, self.netloc, self.uri, self.params, self.query, self.fragment = urlparse.urlparse(self.url)

        logger.info(
            'Scheme --> %s, '
            'host --> %s, '
            'url --> %s, '
            'params --> %s, '
            'query --> %s, fragment: %s', self.scheme, self.netloc, self.uri, self.params, self.query, self.fragment)

        if kwargs:
            logger.info('kwargs -->%s', kwargs)

    def read_wsdl(self):
        try:
            if self.query == 'wsdl':
                logger.info('WSDL present..')
            else:
                logger.warning('Missed WSDL path in your URL..trying resolve adding ?wsdl query')
                self.url += '?wsdl'

            wsdl = urllib.urlopen(self.url).read()

            _file = StringIO(wsdl)

            namespaces = []

            for event, element in ET.iterparse(_file, events=('start-ns','end')):
                logger.debug('event -->%s, element -->%s', event, element)

                if event == 'start-ns':
                    namespaces.append(element)

            logger.info('Namespaces -->%s', namespaces)

        except IOError:
            raise HTTPError("Cannot open WSDL, please verify that WSDl url is valid -->" + self.url)