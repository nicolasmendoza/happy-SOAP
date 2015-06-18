# -*- coding: utf8 -*-
import urllib

from . import getLogger

logger = getLogger(__name__)

class HTTPError(Exception):
    pass

class HTTPClient(object):
    user_agent = "Happy SOAP (from http://nicolasmendoza.org/happy-SOAP/) "

    def __init__(self,**kwargs):
        pass

    def open_url(self, url):
        """
        Open a simple URL....
        :param url:
        :return:
        """

        response = urllib.urlopen(url)

        if response.code != 200:
                logger.debug('Error opening WSDL Status: %i', response.code)

                raise HTTPError(
                    '[WSDL] Error opening webservice description, HTTP code:{0} , url:{1}'.format(
                        response.code,
                        self.url
                    )
                )

        return response
