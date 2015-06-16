from unittest import TestCase
from HappySOAP.client import Client

class HTTPClientTest(TestCase):
    def setUp(self):
        self.api_url = 'https://api-citas.buenosaires.gob.ar'

    def test_http_connection(self):
        client = Client(wsdl=self.api_url)

