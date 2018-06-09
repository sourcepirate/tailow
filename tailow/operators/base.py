
from tailow.fields.base import BaseField

class Operator(object):

    def get_value(self, field, value):
        if field is None or not isinstance(field, BaseField):
            return value
        return field.to_query(value)
    
    def to_query(self, field_name, value):
        return NotImplementedError()


class OperationRegistry(object):

    _registry = {}

    @classmethod
    def register(cls, name, opr):
        cls._registry[name] = opr

    @classmethod
    def values(cls):
        return cls._registry.values()
    
    @classmethod
    def get(cls, name):
        return cls._registry.get(name)
