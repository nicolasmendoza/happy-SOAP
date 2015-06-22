from unittest import TestCase
from HappySOAP.client import Client

from .HappySOAP.loggers import getLogger

logger = getLogger(__name__)

class HTTPClientTest(TestCase):
    def setUp(self):
        self.api_url = 'https://api-citas.buenosaires.gob.ar'

    def test_http_connection(self):

        ws = []
        ws.append('http://appfuse.org/rpc/soap-axis/confluenceservice-v1?wsdl')

        for url in ws:
            client = Client(wsdl=url)
