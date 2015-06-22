from StringIO import StringIO
import urlparse
from .http import HTTPClient
from .loggers import getLogger
from .parser import SOAPParser
logger = getLogger(__name__)

class SoapClientError(Exception):
    pass

class Client(object):
    """
    Soap Client...
    """
    http = HTTPClient()

    def __init__(self, wsdl=None, parser=None, soap_version="1.1"):
        self.soap_version = soap_version or self.soap_version
        self.wsdl_location = wsdl or self.wsdl

        if parser is None:
            self.parser = SOAPParser

        self._call()

    def _get_wsdl(self):
        """
        Get WSDL..
        :return:
        """
        scheme, netloc, uri, params, query, fragment = urlparse.urlparse(self.wsdl_location)

        if query.lower() == 'wsdl':
            logger.info('WSDL present..')

        else:
            logger.warning('Missed WSDL path in your URL..trying resolve adding ?wsdl query')
            self.wsdl_location += '?wsdl'

        wsdl_string_response = self.http.open_url(self.wsdl_location)

        logger.info('WSDL location --> %s', self.wsdl_location)

        try:
            response = wsdl_string_response.read()

            return response

        except IOError:
            raise SoapClientError("Cannot open WSDL, please verify that WSDl url is valid -->" + self.url)

        raise SoapClientError('Error reading WSDL..')

    def _call(self):
        self.soap = self.parser(self._get_wsdl(), self.soap_version).get_api_soap()
        return True
