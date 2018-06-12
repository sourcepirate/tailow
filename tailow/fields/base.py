
class BaseField(object):

    def __init__(self, required=True, 
                       unique=True, 
                       sparse=True,
                       default=None):
        self.required = required
        self.unique = unique
        self.sparse = sparse
        self.default = default
    
    def is_empty(self, value):
        return value is None
    
    def get_value(self, value):
        return value
    
    def to_son(self, value):
        return value

    def from_son(self, value):
        return value
    
    def to_query(self, value):
        return self.to_son(value)
    
    def validate(self, value):
        return True

    @property
    def is_reference(self):
        return hasattr(self, '_is_reference')