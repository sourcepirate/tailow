class BaseField(object):
    def __init__(self, required=True, default=None, unique=False):
        self.required = required
        self.default = default
        self.unique = unique

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
        return hasattr(self, "_is_reference")
