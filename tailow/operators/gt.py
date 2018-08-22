from tailow.operators.base import Operator

class GTOperator(Operator):
    """ Greater than operator """

    def to_query(self, field_name, value):

        return {
            "$gt": value
        }

    def get_value(self, field, value):
        return field.to_son(value)

class GTEOperator(Operator):

    def to_query(self, field_name, value):
        return {
            "$gte": value
        }

    def get_value(self, field, value):
        return field.to_son(value)