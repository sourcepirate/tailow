from tailow.operators.base import Operator


class InOperator(Operator):
    def to_query(self, field_name, value):
        """ To query operator """
        return {"$in": value}

    def get_value(self, field, value):
        """ get value for the field """
        return [field.to_son(val) for val in value]
