import re
from tailow.fields.base import BaseField

class StringField(BaseField):

    def __init__(self, max_length=None, **kwargs):
        super(StringField, self).__init__(**kwargs)
        self.max_length = max_length

    def from_son(self, value):
        return str(value)
    
    def to_son(self, value):
        return str(value)
    
    def validate(self, value):
        return isinstance(value, str) and len(value) <= self.max_length

class TextField(StringField):

    def validate(self, value):
        return isinstance(value, str)

class RegexField(StringField):

    def __init__(self, pattern=None, **kwargs):
        super(RegexField, self).__init__(**kwargs)
        self.pattern = re.compile(pattern) if pattern else None

    def validate(self, value):
        if self.pattern:
            m = self.pattern.match(value)
            return True if m else False
        return True