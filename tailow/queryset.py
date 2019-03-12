from tailow.connection import Connection
from tailow.operators.base import QBase, Q


class QuerySet(object):
    def __init__(self, klass, limit=100, skip=0):
        self.klass = klass
        self._skip = skip
        self._offset = 0
        self._limit = limit
        self._orders = []
        self._q = None

    def coll(self):
        return Connection.get_collection(self.klass._collection)

    def skip(self, num):
        self._skip = num
        return self

    def limit(self, num):
        self._limit = num
        return self

    def offset(self, num):
        self._offset = num
        return self

    def filter(self, *q, **kwargs):
        if len(q) > 0 and isinstance(q[0], QBase):
            if self._q:
                self._q = self._q & q[0]
            else:
                self._q = q[0]
        else:
            _filters = {}
            for field_name, value in kwargs.items():
                if field_name not in self.klass._fields:
                    raise ValueError(
                        "Invalid field being queried: {}".format(field_name)
                    )
                field = self.klass._fields[field_name]
                _filters[field_name] = field.to_son(value)
                if self._q:
                    self._q = self._q & Q(**_filters)
                else:
                    self._q = Q(**_filters)
        return self

    def order(self, field_name, direction=None):
        self._orders.append((field_name, direction))
        return self

    def _get_safe_query(self):
        return self._q or Q()

    async def all(self):
        """ Find all value regarding the filters """
        qry = self._get_safe_query()
        values = self.coll().find(qry.query(self.klass._fields))
        if self._skip:
            values = values.skip(self._skip)
        if self._orders:
            values = values.sort(self._orders)
        values = await values.to_list(length=self._limit)
        return map(lambda x: self.klass(**x), values)

    async def get(self):
        qry = self._get_safe_query()
        values = await self.coll().find_one(qry.query(self.klass._fields))
        if values:
            return self.klass(**values)
        return None

    async def count(self):
        qry = self._get_safe_query()
        values = await self.coll().find(qry.query(self.klass._fields)).count()
        return values
