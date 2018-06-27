
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


def transform_query(fields, **queryargs):
    """ transforms the query to mongodb query """
    query_set = {}
    for key, value in queryargs.items():
        values = key.split("__")
        if len(values) > 1:
            operator, field_name = values[-1], values[0]
            opr = OperationRegistry.get(operator)
            if opr:
                opr = opr()
            field = fields.get(field_name)
            query_values = opr.to_query(field_name, opr.get_value(field, value))
            query_set[field_name] = query_values
        else:
            query_set[key] = value
    return query_set


class QBase(object):
    """ Base object of all query combination """
    
    def __init__(self, *qn):
        self.qs = qn

    def query(self, fields):
        return self.qs
    
    def __or__(self, other):
        return QCombination(self, other)

    def __and__(self, other):
        return QConjugation(self, other)

class QCombination(QBase):

    def query(self, fields):
        return {"$or": list(map(lambda x: x.query(fields), self.qs))}

class QConjugation(QBase):

    def query(self, fields):
        return {"$and": list(map(lambda x: x.query(fields), self.qs))}

class Q(QBase):

    def __init__(self, *qs, **fltr):
        self._transformed = fltr
        super(Q, self).__init__(qs)
    
    def query(self, fields):
        return transform_query(fields, **self._transformed)