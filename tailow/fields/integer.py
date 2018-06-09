
from tailow.fields.base import BaseField

class IntegerField(BaseField):

    def __init__(self, min_value=None, max_value=None, **kwargs):
        super(IntegerField, self).__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value
    
    def _to_int(self, value):
        return int(value) if value else int(self.default)
    
    def from_son(self, value):
        return self._to_int(value)
    
    def to_son(self, value):
        return self._to_int(value)

    def to_query(self, value):
        return self._to_int(value)
    
    def validate(self, value):
        val = self._to_int(value)
        
        if val < self.min_value:
            return False
        if val > self.max_value:
            return False
        
        return True