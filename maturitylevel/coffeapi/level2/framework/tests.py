from django.test import Client
from functools import partialmethod

from coffeapi.level2.framework.http import DEFAULT_CT
from coffeapi.level2.framework.serializers import MyJsonEncoder, MyJsonDecoder

APIClient = type('APIClient',
                 (Client,),
                 {
                     '__init__': partialmethod(Client.__init__, json_encoder=MyJsonEncoder),
                     '_parse_json': partialmethod(Client._parse_json, cls=MyJsonDecoder),
                     **{verb: partialmethod(getattr(Client, verb), content_type=DEFAULT_CT)
                        for verb in ('post', 'get', 'put', 'delete')},
                 }
            )