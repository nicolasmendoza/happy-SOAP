# -*- coding: utf-8 -*-

__all__ = ['ApiBinding', 'ApiRequest', 'ApiOperation']


class ApiRequest(object):
    pass

class ApiOperation(object):
    name = ''
    use = ''
    one_way = ''
    action = ''
    request = ApiRequest()

class ApiBinding(object):
    wsdl_url = ''
    cache = False
    namespaces = []
    binding_soap = ''
    soap_version = ''
    style = ''
    operations = {}