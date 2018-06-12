
from datetime import datetime
from tailow.fields.base import BaseField

DEFAULT_FORMAT = "%Y-%m-%d-%H-%M-%S"

class DateTimeField(BaseField):
    
    FORMAT = DEFAULT_FORMAT

    def __init__(self, date_format=None, **kwargs):
        super(DateTimeField, self).__init__(**kwargs)
        self.FORMAT = date_format or self.__class__.FORMAT
    
    def to_son(self, value):
        return value.strftime(self.FORMAT)
    
    def from_son(self, value):
        return datetime.strptime(value, self.FORMAT)
    
    def validate(self, value):
        return isinstance(value, datetime)
