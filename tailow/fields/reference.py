""" reference field """

from bson.objectid import ObjectId
from .base import BaseField


class ReferenceField(BaseField):
    """ Reference field property """

    def __init__(self, kls, *args, **kwargs):
        self.kls = kls
        self._is_reference = True
        self._partialy_loaded = kwargs.pop("_is_partialy_loaded", False)
        super(ReferenceField, self).__init__(*args, **kwargs)

    def validate(self, value):
        """ validate if it is a valid field """
        from tailow.document import Document

        if isinstance(value, (self.kls, Document)):
            return True
        return False

    def to_son(self, value):
        if value is None:
            return None
        if isinstance(value, ObjectId):
            return value
        return value._id if hasattr(value, "_id") else value.id

    def from_son(self, value):
        val = self.kls(id=value, _is_partialy_loaded=True)
        return val
