from unittest import TestCase
from HappySOAP.client import Client

from .HappySOAP.loggers import getLogger

logger = getLogger(__name__)

class HTTPClientTest(TestCase):
    def setUp(self):
        self.api_url = 'https://api-citas.buenosaires.gob.ar'

    def test_http_connection(self):

        ws = []
        ws.append('http://suaci-gcba.buenosaires.gov.ar/suaci/services/suaciWebServices?wsdl')
        ws.append('https://api-citas.buenosaires.gob.ar')
        #ws.append('http://www.w3schools.com/webservices/tempconvert.asmx?WSDL')
        #ws.append('http://10.10.5.221:12345/PagoVoluntarioWS/PagoVoluntarioWS?WSDL')
        #ws.append('https://api-citas.buenosaires.gob.ar')
        #ws.append('http://suaci-gcba.buenosaires.gov.ar/suaci/services/bandejaDeEntrada?wsdl')
        #ws.append('http://suaci-gcba.buenosaires.gov.ar/suaci/services/cenat?wsdl')
        #ws.append('http://suaci-gcba.buenosaires.gov.ar/suaci/services/contacto?wsdl')
        #ws.append('http://suaci-gcba.buenosaires.gov.ar/suaci/services/integracionConSap?wsdl')
        #ws.append('http://suaci-gcba.buenosaires.gov.ar/suaci/services/licencias?wsdl')
        #ws.append('http://suaci-gcba.buenosaires.gov.ar/suaci/services/operadorCiudadano?wsdl')
        #ws.append('http://suaci-gcba.buenosaires.gov.ar/suaci/services/turno?wsdl')

        for url in ws:
            client = Client(wsdl=url)

