import abc
from datetime import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder

class IMySerializable(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, 'vars') and
            classmethod(subclass.vars)
        )

    @abc.abstractclassmethod
    def vars(self):
        pass
    

def serialize(obj):
    return json.dumps(obj, cls=MyJsonEncoder)

def deserialize(s):
    return json.loads(s, cls=MyJsonDecoder)

class MyJsonEncoder(DjangoJSONEncoder):
    def encode(self, o):
        if isinstance(o, IMySerializable):
            o = o.vars()
        return super().encode(o)

class MyJsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(object_hook=self.hook, *args, **kwargs)

    @staticmethod
    def hook(source):
        d ={}
        for k, v in source.items():
            if isinstance(v, str) and not v.isdigit():
                try:
                    d[k] = datetime.fromisoformat(v)
                except (ValueError, TypeError):
                    d[k] = v
            else:
                d[k] = v

        return d
