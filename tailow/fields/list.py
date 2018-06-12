
from tailow.fields.base import BaseField

class ListField(BaseField):

    def __init__(self, sub_field=None, **kwargs):
        super(ListField, self).__init__(**kwargs)
        if not sub_field:
            raise ValueError("ListField subtype not mentioned")
        self.sub_field = sub_field
    
    def from_son(self, value):
        return map(lambda x: self.sub_field.from_son(x), value)
    
    def to_son(self, value):
        return map(lambda x: self.sub_field.to_son(x), value)